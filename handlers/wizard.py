from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data import constraints as c
from data import questionnaire as q
from data.session_manager import SessionManager
from keyboards import builders as kb
from states import WizardStates

router = Router()
sessions = SessionManager()


async def _answers(state: FSMContext) -> dict:
    data = await state.get_data()
    return data.get("answers", {})


async def _save(state: FSMContext, key: str, value) -> dict:
    data = await state.get_data()
    answers = data.get("answers", {})
    answers[key] = value
    answers = c.reset_dependent_answers(key, answers)
    await state.update_data(answers=answers)
    sid = data.get("session_id")
    if sid:
        sessions.update_session(sid, {"answers": answers})
    return answers


@router.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    sid = sessions.create_session(message.from_user.id)
    await state.clear()
    await state.update_data(session_id=sid, answers={})
    await state.set_state(WizardStates.segment)
    await message.answer("Let's begin. Pick a segment:",
                         reply_markup=kb.single_select(q.SEGMENTS, "segment", back=False))


@router.callback_query(WizardStates.segment, F.data.startswith("segment:"))
async def pick_segment(cb: CallbackQuery, state: FSMContext) -> None:
    await _save(state, "segment", cb.data.split(":", 1)[1])
    await state.set_state(WizardStates.category)
    await cb.message.edit_text("Category:", reply_markup=kb.single_select(q.CATEGORIES, "category"))
    await cb.answer()


@router.callback_query(WizardStates.category, F.data.startswith("category:"))
async def pick_category(cb: CallbackQuery, state: FSMContext) -> None:
    category = cb.data.split(":", 1)[1]
    await _save(state, "category", category)
    groups = c.get_available_groups(category)
    await state.set_state(WizardStates.group)
    await cb.message.edit_text("Group:", reply_markup=kb.from_keys(groups, q.GROUPS, "group"))
    await cb.answer()


@router.callback_query(WizardStates.group, F.data.startswith("group:"))
async def pick_group(cb: CallbackQuery, state: FSMContext) -> None:
    group = cb.data.split(":", 1)[1]
    await _save(state, "group", group)
    await _save(state, "item_a_selected", {})
    await state.set_state(WizardStates.item_a)
    items = {k: q.ITEMS["a"][k] for k in c.get_available_items("a", group)}
    await cb.message.edit_text("Choose options (tap to include / exclude):",
                               reply_markup=kb.multi_select(items, {}, "item_a"))
    await cb.answer()


@router.callback_query(WizardStates.item_a, F.data.startswith("item_a:"))
async def toggle_item_a(cb: CallbackQuery, state: FSMContext) -> None:
    key = cb.data.split(":", 1)[1]
    data = await state.get_data()
    selected = data.get("item_a_selected", {})
    # unset -> include -> exclude -> unset
    nxt = {None: "include", "include": "exclude", "exclude": None}[selected.get(key)]
    if nxt is None:
        selected.pop(key, None)
    else:
        selected[key] = nxt
    await state.update_data(item_a_selected=selected)
    group = (await _answers(state)).get("group")
    items = {k: q.ITEMS["a"][k] for k in c.get_available_items("a", group)}
    await cb.message.edit_reply_markup(reply_markup=kb.multi_select(items, selected, "item_a"))
    await cb.answer()


@router.callback_query(WizardStates.item_a, F.data == kb.NAV_DONE)
async def finish_item_a(cb: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    selected = data.get("item_a_selected", {})
    await _save(state, "item_a_include", [k for k, v in selected.items() if v == "include"])
    await _save(state, "item_a_exclude", [k for k, v in selected.items() if v == "exclude"])
    await state.set_state(WizardStates.priority)
    await cb.message.edit_text("Priority:", reply_markup=kb.single_select(q.PRIORITIES, "priority"))
    await cb.answer()


@router.callback_query(WizardStates.priority, F.data.startswith("priority:"))
async def pick_priority(cb: CallbackQuery, state: FSMContext) -> None:
    priority = cb.data.split(":", 1)[1]
    await _save(state, "priority", priority)
    tracks = c.get_available_tracks(priority)
    await state.set_state(WizardStates.track)
    await cb.message.edit_text("Track:", reply_markup=kb.from_keys(tracks, q.TRACKS, "track"))
    await cb.answer()


@router.callback_query(WizardStates.track, F.data.startswith("track:"))
async def pick_track(cb: CallbackQuery, state: FSMContext) -> None:
    track = cb.data.split(":", 1)[1]
    answers = await _answers(state)
    await _save(state, "track", track)
    options = c.get_available_options(answers.get("priority"), track)
    await state.set_state(WizardStates.option_final)
    await cb.message.edit_text("Final option:",
                               reply_markup=kb.from_keys(options, q.OPTIONS_FINAL, "option_final"))
    await cb.answer()


@router.callback_query(WizardStates.option_final, F.data.startswith("option_final:"))
async def pick_option_final(cb: CallbackQuery, state: FSMContext) -> None:
    await _save(state, "option_final", cb.data.split(":", 1)[1])
    await state.set_state(WizardStates.notes)
    await cb.message.edit_text("Any notes? Send a message, or /skip.")
    await cb.answer()


@router.message(WizardStates.notes)
async def take_notes(message: Message, state: FSMContext) -> None:
    await _save(state, "notes", message.text or "")
    await _finish(message, state)


@router.message(WizardStates.notes, Command("skip"))
async def skip_notes(message: Message, state: FSMContext) -> None:
    await _finish(message, state)


async def _finish(message: Message, state: FSMContext) -> None:
    answers = await _answers(state)
    from services.export import answers_to_row
    row = answers_to_row(answers)
    await state.clear()
    await message.answer("Saved. " + str(len([c for c in row if c])) + " fields filled.")

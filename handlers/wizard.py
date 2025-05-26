from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from data import questionnaire as q
from keyboards import builders as kb
from states import WizardStates

router = Router()


async def _save(state: FSMContext, key: str, value) -> dict:
    data = await state.get_data()
    answers = data.get("answers", {})
    answers[key] = value
    await state.update_data(answers=answers)
    return answers


@router.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.update_data(answers={})
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
    await _save(state, "category", cb.data.split(":", 1)[1])
    await state.set_state(WizardStates.group)
    await cb.message.edit_text("Group:", reply_markup=kb.single_select(q.GROUPS, "group"))
    await cb.answer()


@router.callback_query(WizardStates.group, F.data.startswith("group:"))
async def pick_group(cb: CallbackQuery, state: FSMContext) -> None:
    await _save(state, "group", cb.data.split(":", 1)[1])
    await state.set_state(WizardStates.notes)
    await cb.message.edit_text("Any notes? Send a message, or /skip.")
    await cb.answer()


@router.message(WizardStates.notes)
async def take_notes(message: Message, state: FSMContext) -> None:
    answers = await _save(state, "notes", message.text or "")
    await state.clear()
    await message.answer("Saved. " + str(len(answers)) + " answers.")

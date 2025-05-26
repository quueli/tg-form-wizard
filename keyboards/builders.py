from typing import Iterable

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

NAV_BACK = "nav:back"
NAV_SKIP = "nav:skip"


def _nav_row(*, back: bool = True, skip: bool = False) -> list[InlineKeyboardButton]:
    row: list[InlineKeyboardButton] = []
    if back:
        row.append(InlineKeyboardButton(text="< Back", callback_data=NAV_BACK))
    if skip:
        row.append(InlineKeyboardButton(text="Skip", callback_data=NAV_SKIP))
    return row


def single_select(options: dict[str, str], prefix: str, *, columns: int = 2,
                  back: bool = True) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for key, label in options.items():
        kb.button(text=label, callback_data=f"{prefix}:{key}")
    kb.adjust(columns)
    nav = _nav_row(back=back)
    if nav:
        kb.row(*nav)
    return kb.as_markup()


def from_keys(keys: Iterable[str], labels: dict[str, str], prefix: str,
              **kwargs) -> InlineKeyboardMarkup:
    subset = {k: labels[k] for k in keys if k in labels}
    return single_select(subset, prefix, **kwargs)

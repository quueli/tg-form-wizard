from aiogram.fsm.state import StatesGroup, State


class WizardStates(StatesGroup):
    segment = State()
    category = State()
    group = State()
    variant = State()
    item_a = State()
    item_b = State()
    item_c = State()
    size = State()
    level = State()
    speed = State()
    tags = State()
    priority = State()
    track = State()
    option_final = State()
    notes = State()
    flags = State()
    customer_type = State()
    contact = State()
    fulfillment = State()

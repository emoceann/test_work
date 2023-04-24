from aiogram.dispatcher.filters.state import StatesGroup, State


class LogicStates(StatesGroup):
    get_currency = State()
    get_weather = State()
    poll_question = State()
    poll_choice = State()

from aiogram.dispatcher.filters.state import StatesGroup, State


class Location(StatesGroup):
    location = State()

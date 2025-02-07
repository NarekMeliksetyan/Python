import api_requests as api
import inline
from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext
from location import get_location
from states import Location


# Commands
async def cmd_temperature(message: types.Message, state: FSMContext):
    location = await get_location(state)
    msg = api.get_temperature(location)
    await message.answer(msg, reply_markup=inline.TEMPERATURE)


async def cmd_wind(message: types.Message, state: FSMContext):
    location = await get_location(state)
    msg = api.get_wind(location)
    await message.answer(msg, reply_markup=inline.WIND)


async def cmd_suntime(message: types.Message, state: FSMContext):
    location = await get_location(state)
    msg = api.get_suntime(location)
    await message.answer(msg, reply_markup=inline.SUNTIME)


# Callbaks
async def call_temperature(callback: types.CallbackQuery, state: FSMContext):
    location = await get_location(state)
    msg = api.get_temperature(location)
    await callback.message.answer(msg, reply_markup=inline.TEMPERATURE)


async def call_wind(callback: types.CallbackQuery, state: FSMContext):
    location = await get_location(state)
    msg = api.get_wind(location)
    await callback.message.answer(msg, reply_markup=inline.WIND)


async def call_suntime(callback: types.CallbackQuery, state: FSMContext):
    location = await get_location(state)
    msg = api.get_suntime(location)
    await callback.message.answer(msg, reply_markup=inline.SUNTIME)


def register_weather(dp: Dispatcher):
    dp.register_message_handler(cmd_temperature, commands=["temperature"], state=Location.location)
    dp.register_message_handler(cmd_wind, commands=["wind"], state=Location.location)
    dp.register_message_handler(cmd_suntime, commands=["suntime"], state=Location.location)

    dp.register_callback_query_handler(call_temperature, text="temperature", state=Location.location)
    dp.register_callback_query_handler(call_wind, text="wind", state=Location.location)
    dp.register_callback_query_handler(call_suntime, text="suntime", state=Location.location)

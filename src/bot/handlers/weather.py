from aiogram.dispatcher import FSMContext

from src.bot.deps import dp, bot, types
from src.openweatherapi import services as weather_services
from aiogram.dispatcher.filters import Text
from src.bot.states import LogicStates


@dp.message_handler(Text(equals='Погода', ignore_case=True))
async def get_city(msg: types.Message):
    await msg.reply('Введите название города')
    await LogicStates.get_weather.set()


@dp.message_handler(state=LogicStates.get_weather)
async def weather(msg: types.Message, state: FSMContext):
    message = await weather_services.get_weather_by_city_name(msg.text)
    if message:
        await msg.reply(text=message)
        await state.finish()
    else:
        await msg.reply(text="Неправильное название города")

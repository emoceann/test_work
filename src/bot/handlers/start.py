from src.bot.deps import dp, bot, types
from src.openweatherapi import services as weather_services


@dp.message_handler(commands='start')
async def hello_world(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True
    ).add('Погода', 'Курс обмена', 'Милота', 'Создать опрос')
    await msg.reply(
        text='Привет добро пожаловать в моего тестового бота выбери что нибудь',
        reply_markup=markup
    )




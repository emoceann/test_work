from src.bot.deps import dp, bot, types
from src.bot.states import LogicStates
from src.exchangeratesapi import services as exchanger_services
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals='Курс обмена', ignore_case=True))
async def rates(msg: types.Message):
    await msg.reply(text='Введи следующие данные' \
                                                  ':имя валюты, цену которой он хочет узнать:'
                                                  ':имя валюты, в которой надо узнать цену первой валюты:'
                                                  ':количество первой валюты:'
                                                  'Вводи аббревиатуру валют латиницей'
                           )
    await LogicStates.get_currency.set()


@dp.message_handler(state=LogicStates.get_currency)
async def result(msg: types.Message, state: FSMContext):
    values = msg.text.split(' ')
    error = 'Ошибка, соблюдайте формат ввода'
    if len(values) > 3:
        await msg.reply(text=error)
    cur1, cur2, amount = values
    if cur1 == cur2:
        await msg.reply(text=error)

    total_base = await exchanger_services.get_exchange_rates(cur1, cur2, float(amount))
    await msg.reply(text=total_base['result'])
    await state.finish()

from src.bot.handlers import dp, bot
from src.bot.deps import app
from aiogram import Bot, Dispatcher, types
from src.exchangeratesapi.services import get_dict_currencies


@app.post("/internal")
async def webhook(update: dict):
    Bot.set_current(value=bot)
    Dispatcher.set_current(value=dp)
    await dp.process_update(update=types.Update(**update))


@app.get('/rwre')
async def sdfsd():
    return await get_dict_currencies()

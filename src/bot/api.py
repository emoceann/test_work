from src.bot.handlers import dp, bot
from src.bot.deps import app
from aiogram import Bot, Dispatcher, types


@app.post("/internal")
async def webhook(update: dict):
    Bot.set_current(value=bot)
    Dispatcher.set_current(value=dp)
    await dp.process_update(update=types.Update(**update))


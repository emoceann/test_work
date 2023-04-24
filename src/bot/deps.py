from fastapi import APIRouter
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings import settings

app = APIRouter(tags=["Telegram"])
bot: Bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp: Dispatcher = Dispatcher(bot=bot, storage=storage)


@app.on_event("startup")
async def on_startup():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=settings.TELEGRAM_BOT_WEBHOOK)


@app.on_event("shutdown")
async def on_shutdown():
    await dp.storage.wait_closed()

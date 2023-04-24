from src.bot.deps import dp, bot, types
from aiogram.dispatcher.filters import Text
from src.cuteanimalsapi import services as cute_services


@dp.message_handler(Text(equals='Милота', ignore_case=True))
async def get_animal(msg: types.Message):
    photo = await cute_services.get_cute_animal()
    await msg.reply_photo(photo=photo)

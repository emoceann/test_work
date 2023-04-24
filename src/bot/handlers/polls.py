from aiogram.dispatcher import FSMContext

from src.bot.deps import dp, bot, types
from aiogram.dispatcher.filters import Text
from src.bot.states import LogicStates


@dp.message_handler(Text(equals='Создать опрос', ignore_case=True))
async def poll_start(msg: types.Message):
    if msg.from_user.id == msg.chat.id:
        await msg.reply('В лс со мной нельзя создать опрос, попробуйте с группы где я есть')
    else:
        await msg.reply('Отправь вопрос для опроса')
        await LogicStates.poll_question.set()


@dp.message_handler(state=LogicStates.poll_question)
async def poll_question(msg: types.Message, state: FSMContext):
    await state.update_data(question_poll=msg.text)
    await msg.reply('А теперь введи варианты через пробел')
    await LogicStates.poll_choice.set()


@dp.message_handler(state=LogicStates.poll_choice)
async def poll_choice(msg: types.Message, state: FSMContext):
    choices = msg.text.split(' ')
    if len(choices) <= 1:
        await msg.reply('Неправильный ввод, повторите')
    else:
        question_poll = (await state.get_data())['question_poll']
        await msg.reply_poll(question=question_poll, options=choices)
        await state.finish()

import datetime

from data.config import GROUP_ID
from keyboards.inline.inlineKeyboard import send_conf
from loader import dp, bot
from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.statesper import quesions


@dp.callback_query_handler(text='section_queries')
async def quest_func1(msg: types.CallbackQuery):
    await msg.message.answer('Отправьте вопрос:')
    await quesions.question.set()


@dp.message_handler(state=quesions.question)
async def quest_func2(msg: types.Message,state=FSMContext):
    async with state.proxy() as data:
        data['question']=msg.text
    await msg.answer(f'<b>Вопрос!</b>\n'
                     f'Пользователь: {msg.from_user.full_name}\n'
                     f"Вопрос: {data['question']}\n\n"
                     f"Отправить?",reply_markup=send_conf, parse_mode='html')
    await quesions.next()


@dp.message_handler(content_types=types.ContentType.ANY, state=quesions.question)
async def err_ques(mess: types.ContentType):
    await mess.answer('Отправить только вопрос!!!')


@dp.callback_query_handler(lambda a: 'query_' in a.data,state=quesions.confirm)
async def quest_func3(msg: types.CallbackQuery,state=FSMContext):
    await msg.message.delete()
    ans = msg.data.split('_')[1]
    await msg.message.answer('Отлично!', reply_markup=ReplyKeyboardRemove())
    if ans == 'True':
        data = await state.get_data()
        ques = data.get('question')
        await state.finish()
        await bot.send_message(chat_id=GROUP_ID,text=f'<b>Вопрос!</b>\n'
                                                           f'User_id:{msg.from_user.id}\n'
                         f'Пользователь: {msg.from_user.full_name}\n'
                         f"Вопрос: {ques}\n\n", parse_mode='html')
    else:
        await state.finish()

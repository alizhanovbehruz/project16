import asyncio
import datetime

from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.admin_keyb import start_admin
from keyboards.inline.inlineKeyboard import start_keyboard
from loader import dp
from utils.db_api.excel import send_excel
from utils.db_api.sqlite import sendex
from filters.private_chat import IsPrivate

@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    l_user = list(map(lambda a: int(a[0]), sendex('select user_id from users')))
    if (message.from_user.id) not in l_user:
        sendex(f"""INSERT INTO users (user_id,full_name, username, time_created) 
                       VALUES ('{message.from_user.id}','{message.from_user.full_name}',
                       '{message.from_user.username}','{datetime.datetime.now()}' ) 
                        returning *""")
        send_excel('users',[message.from_user.id, message.from_user.full_name,
                            message.from_user.username, datetime.datetime.now()])
    if (message.from_user.id in ADMINS()):
        await message.answer('Добро пожаловать Admin',reply_markup=start_admin)
    else:
        await message.answer(f"Это бот-секретарь сообщества DocNet. Рад приветствовать.\n\n"
                            f"Выберите интересующий Вас вопрос, обсудим. Ниже это кнопки", reply_markup=start_keyboard)


@dp.message_handler(IsPrivate(), text='◀Вернуться в главный меню', state="*")
async def bot(msg:types.Message, state=FSMContext):
    await msg.answer('Отлично!', reply_markup=types.ReplyKeyboardRemove())
    await bot_start(msg)
    await state.finish()
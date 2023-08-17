from keyboards.inline.admin_keyb import admin_set ,start_admin
from loader import dp, bot
from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from utils.db_api.excel import send_excel
from keyboards.default.menuStart import back
from utils.db_api.sqlite import sendex
from states.statesper import admins_add, admins_remove, admins_post
"""setting admin"""


@dp.callback_query_handler(text='startsett_admin')
async def admin_func1(msg: types.CallbackQuery):
    await msg.message.delete()
    await msg.message.answer('Добавить/Удалить админа',reply_markup=admin_set)


@dp.callback_query_handler(lambda a: 'admins_' in a.data)
async def admin_func2(msg: types.CallbackQuery):
    ans = msg.data.split('_')[1]
    await msg.message.delete()
    await msg.message.answer('Введите user_id,name в формате (12345678,name)', reply_markup=back)
    print(ans)
    if ans == 'add':
        await admins_add.info.set()
    else:
        await admins_remove.info.set()

@dp.message_handler(state=admins_add.info)
async def admin_func3(msg: types.Message, state=FSMContext):
    await state.finish()
    try:
        user_id, name = msg.text.split(',')
        sendex(f'''INSERT INTO admins (user_id,full_name) values ('{user_id}','{name}')''')
        await msg.answer('Успешно!', reply_markup=start_admin)
    except:
        await msg.answer('Ошибка!',reply_markup=admin_set)


@dp.message_handler(state=admins_remove.info)
async def admin_func4(msg: types.Message, state=FSMContext):
    await state.finish()
    await msg.delete()
    if msg.text == str(msg.from_user.id):
        await msg.answer('Вы не можете удалить себя!!', reply_markup=admin_set)
    else:
        try:
            user_id = msg.text
            sendex(f'''DELETE FROM admins where (user_id='{user_id}')''')
            await msg.answer('Успешно!',reply_markup=start_admin)
        except:
            await msg.answer('Ошибка!',reply_markup=admin_set)

        """ end setting admin"""

        """post"""
@dp.callback_query_handler(text='startset_post')
async def admin_func5(msg: types.CallbackQuery):
    await msg.message.answer('Отправьте текст', reply_markup=back)
    await admins_post.info.set()


@dp.message_handler(state=admins_post.info)
async def admin_func6(msg: types.Message):
    if msg.text == 'нет':
        await msg.answer('Успешно не отправлено!', reply_markup=start_admin)
    else:
        for i in sendex('''select user_id from users'''):
            try:
                await bot.send_message(chat_id=i[0], text=msg.text)
            except:
                await msg.answer(f'{i[0]} покинул!')
        await msg.answer('Успешно отправлено!', reply_markup=start_admin)
        """end post"""


        """statistic"""
@dp.callback_query_handler(text='startsett_statistic')
async def admin_func7(msg: types.Message):
    await bot.send_document(chat_id=msg.from_user.id,document=open('table.xlsx','rb'))
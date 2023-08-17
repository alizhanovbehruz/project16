import datetime

from handlers.users.start import bot_start
from loader import dp, bot
from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
import re
from states.statesper import doctor_info
from keyboards.default.menuStart import number, method_con, back
from keyboards.inline.inlineKeyboard import skills_menu, cert_, consul, usepc, cons_lang
from utils.db_api.excel import send_excel
from utils.db_api.sqlite import sendex

email_re = '''[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'''
phone_re = """^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"""


@dp.callback_query_handler(text='section_doctors')
async def doctors_func(msg: types.CallbackQuery):
    await msg.message.answer('Давайте знакомиться!\n\nВнесите свои ФИО⬇', reply_markup=back)
    await doctor_info.full_name.set()


@dp.message_handler(state=doctor_info.full_name)
async def doctors_func1(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['full_name'] = msg.text
    await msg.answer('Отправьте адрес электронной почты', reply_markup=back)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.email)
async def doctors_func2(msg: types.Message, state=FSMContext):
    txt = msg.text
    if not re.search(email_re,txt):
        await msg.answer('Пожалуйста, введите элетронную почту в правильном формате!:')
    else:
        async with state.proxy() as data:
            data['email'] = txt
        await msg.answer('Отправьте username от Instagram', reply_markup=back)
        await doctor_info.next()


@dp.message_handler(state=doctor_info.account)
async def doctors_func3(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['account'] = msg.text
    await msg.answer('Отправьте номер телефона', reply_markup=number)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.number_phone,content_types=ContentType.CONTACT)
async def doctor4_1(msg: types.ContentTypes, state=FSMContext):
    txt= msg['contact']['phone_number']
    async with state.proxy() as data:
        data['number'] = txt
    await msg.answer('Пришлите вашу дату рождения', reply_markup=back)
    await doctor_info.next()

@dp.message_handler(state=doctor_info.number_phone)
async def doctors_func4(msg: types.Message, state=FSMContext):
    txt = msg.text
    if not re.search(phone_re,txt):
        await msg.answer('Пожалуйста, введите  телефон в международном формате!:')
    else:
        async with state.proxy() as data:
            data['number'] = txt
        await msg.answer('Пришлите вашу дату рождения', reply_markup=back)
        await doctor_info.next()


@dp.message_handler(state=doctor_info.date_of_birth)
async def doctors_func5(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['date_birth'] = msg.text
    await msg.answer('Ваша общий врачебный стаж:',reply_markup=skills_menu)
    await doctor_info.next()


@dp.callback_query_handler(lambda a: a.data.startswith('skillss_'), state=doctor_info.skill)
async def doctors_func5(msg: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['skills'] = msg.data.split('_')[1]
    await msg.message.delete()
    await msg.message.answer('Ваша специализация:', reply_markup=back)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.sphere)
async def doctors_func6(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['sphere'] = msg.text
    await msg.answer('Действующий ли у Вас сертификат специалиста?', reply_markup=cert_)
    await doctor_info.next()


@dp.callback_query_handler(lambda a: a.data.startswith('cert_'), state=doctor_info.cert_b)
async def doctors_func7(msg: types.CallbackQuery, state=FSMContext):
    ans = msg.data.split('_')[1]
    async with state.proxy() as data:
        data['cert_b'] = ans
    await msg.message.delete()
    await msg.message.answer('Есть ли у Вас врачебная категория? Если да, какая?', reply_markup=back)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.med_cat)
async def doctors_func8(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['med_cat'] = msg.text
    await msg.answer('Есть ли у Вас научная степень? Если есть, какая?', reply_markup=back)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.degree_a)
async def doctors_func9(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['degree_a']=msg.text
    await msg.answer('Консультируете ли Вы онлайн?',reply_markup=consul)
    await doctor_info.next()


@dp.callback_query_handler(lambda a: a.data.startswith('consul_'), state=doctor_info.consult_b)
async def doctors_func10(msg: types.CallbackQuery, state=FSMContext):
    ans = msg.data.split('_')[1]
    async with state.proxy() as data:
        data['consult_b'] = ans
    await msg.message.delete()
    await msg.message.answer('На каком языке вы предпочитаете проводить консультацию?', reply_markup=cons_lang)
    await doctor_info.next()


@dp.callback_query_handler(lambda a: a.data.startswith('conlang_'), state=doctor_info.consult_lang)
async def doctors_func10(msg: types.CallbackQuery, state=FSMContext):
    ans = msg.data.split('_')[1]
    async with state.proxy() as data:
        data['consult_lang'] = ans
    await msg.message.delete()
    await msg.message.answer('Пользование Компьютером', reply_markup=usepc)
    await doctor_info.next()


@dp.callback_query_handler(lambda a: a.data.startswith('usepc_'), state=doctor_info.use_pc)
async def doctors_func11(msg: types.CallbackQuery, state=FSMContext):
    ans = msg.data.split('_')[1]
    async with state.proxy() as data:
        data['use_pc'] = ans
    await msg.message.delete()
    await msg.message.answer('Благодарим за ответы, администратор свяжется с Вами. '
                             'Какая связь удобна для Вас ?(если нет подходяшего варианта,'
                             ' то пишите в ручную)',reply_markup=method_con)
    await doctor_info.next()


@dp.message_handler(state=doctor_info.method_conn)
async def doctors_func12(msg: types.Message, state=FSMContext):
    await msg.answer('Отлично!', reply_markup=ReplyKeyboardRemove())
    await bot_start(msg)
    data = await state.get_data()
    full_name = data.get('full_name')
    email = data.get('email')
    account = data.get('account')
    number = data.get('number')
    date_birth = data.get('date_birth')
    skills = data.get('skills')
    sphere = data.get('sphere')
    cert_b = data.get('cert_b')
    med_cat = data.get('med_cat')
    degree_a = data.get('degree_a')
    consult_b= data.get('consult_b')
    use_pc = data.get('use_pc')
    consult_lang = data.get('consult_lang')
    method = msg.text
    await state.finish()
    sendex(f'''INSERT INTO doctors (chat_id,full_name,email,account,number,date_birth,skills,
sphere,cert_b,med_cat,degree_a,consult_b, consult_lang, use_pc,method,time_created) values ("{msg.from_user.id}",
"{full_name}","{email}","{account}","{number}","{date_birth}","{skills}","{sphere}","{cert_b}","{med_cat}",
"{degree_a}","{consult_b}", "{consult_lang}", "{use_pc}","{method}","{datetime.datetime.now()}")''')
    send_excel('doctor', [msg.from_user.id, full_name, email, account, number, date_birth,
                             skills, sphere, cert_b, med_cat,
                            degree_a, consult_b, consult_lang, use_pc, method, datetime.datetime.now()])

from handlers.users.start import bot_start
from keyboards.inline.deals import type_clin, type_cl, profile_
from loader import dp, bot
from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove
from utils.db_api.excel import send_excel
from utils.db_api.sqlite import sendex
from aiogram.dispatcher import FSMContext
import datetime
from states.statesper import deals
from keyboards.default.menuStart import number, back
from filters.private_chat import IsPrivate ,IsPrivate_Call

@dp.callback_query_handler(IsPrivate_Call(),text='section_deals')
async def deals_func1(msg: types.CallbackQuery):
    await msg.message.answer('Введите название клиники:', reply_markup=back)
    await deals.clinic_name.set()


@dp.message_handler(state=deals.clinic_name)
async def deals_func2(msg: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['clinic_name'] = msg.text
        data['type_clinic'] =[]
    await msg.answer('Вид медицинской помощи',reply_markup=type_clin)
    await deals.next()


@dp.callback_query_handler(state=deals.type_clinic)
async def deals_func3(msg: types.CallbackQuery, state=FSMContext):
    if msg.data == 'typeofclin_success':
        await msg.message.delete()
        await msg.message.answer('Введите график работы', reply_markup=back)
        await deals.sch_work.set()
    elif msg.data =='typeofclin_another':
        await msg.message.delete()
        await msg.message.answer('Введите вид медицинской помощи:', reply_markup=back)
        await deals.next()
    else:
        keyb, remov = await type_cl(msg.data, msg.message.reply_markup)
        if remov:
            async with state.proxy() as data:
                data['type_clinic'].remove(remov[1:])
            await msg.message.edit_reply_markup(keyb)
        else:
            async with state.proxy() as data:
                data['type_clinic'].append(msg.data.split('_')[1])
            await msg.message.edit_reply_markup(keyb)


@dp.message_handler(state=deals.type_clinic2)
async def deals_func3_1(msg: types.Message, state=FSMContext):
    async with state.proxy()as data:
        data['type_clinic'].append(msg.text)
    await msg.answer('Введите график работы', reply_markup=back)
    await deals.next()


@dp.message_handler(state=deals.sch_work)
async def deals_func4(msg: types.Message, state=FSMContext):
    async with state.proxy()as data:
        data['sch_work'] = msg.text
    await msg.answer('Введите адрес', reply_markup=back)
    await deals.next()


@dp.message_handler(state=deals.location)
async def deals_func5(msg: types.Message, state=FSMContext):
    async with state.proxy()as data:
        data['location'] = msg.text
    await msg.answer('Ваши контакты',reply_markup=number)
    await deals.next()


@dp.message_handler(state=deals.contact,content_types=ContentType.CONTACT)
async def doctor6(msg: types.ContentTypes, state=FSMContext):
    txt= msg['contact']['phone_number']
    async with state.proxy() as data:
        data['number'] = txt
        data['profile'] =[]
    await msg.answer('Отлично!', reply_markup=back)
    await msg.answer('Профиль', reply_markup=profile_)
    await deals.next()


@dp.message_handler(state=deals.contact)
async def doctors_func6_1(msg: types.Message, state=FSMContext):
    txt = msg.text
    async with state.proxy() as data:
        data['number'] = txt
        data['profile'] =[]
    await msg.answer('Отлично!', reply_markup=back)
    await msg.answer('Профиль', reply_markup=profile_)
    await deals.next()


@dp.callback_query_handler(state=deals.profile)
async def deals_func7(msg: types.CallbackQuery, state=FSMContext):
    if msg.data == 'profilede_success':
        await msg.message.delete()
        await msg.message.answer('Введите Ф.И.О. и контакты руководителя / ответственного лица:', reply_markup=back)
        await deals.name_of_owner.set()
    elif msg.data =='profilede_another':
        await msg.message.delete()
        await msg.message.answer('Введите профиль:', reply_markup=back)
        await deals.next()
    else:
        keyb, remov = await type_cl(msg.data, msg.message.reply_markup)
        if remov:
            async with state.proxy() as data:
                data['profile'].remove(remov[1:])
            await msg.message.edit_reply_markup(keyb)
        else:
            async with state.proxy() as data:
                data['profile'].append(msg.data.split('_')[1])
            await msg.message.edit_reply_markup(keyb)


@dp.message_handler(state=deals.profile2)
async def deals_func7_1(msg: types.Message, state=FSMContext):
    async with state.proxy()as data:
        data['profile'].append(msg.text)
    await msg.answer('Введите Ф.И.О. и контакты руководителя / ответственного лица:', reply_markup=back)
    await deals.next()


@dp.message_handler(state=deals.name_of_owner)
async def doctors_func8(msg: types.Message, state=FSMContext):
    txt = msg.text
    async with state.proxy() as data:
        data['name_of_owner'] = txt
    await msg.answer('Что хотели бы подчеркнуть в профиле клиники', reply_markup=back)
    await deals.next()


@dp.message_handler(state=deals.wants)
async def doctors_func12(msg: types.Message, state=FSMContext):
    await msg.answer('Отлично!', reply_markup=ReplyKeyboardRemove())
    await bot_start(msg)
    data = await state.get_data()
    clinic_name= data.get('clinic_name')
    clinic_name = clinic_name
    type_clinic= str(data.get('type_clinic')).replace('[','').replace("'",'').replace(']','')
    sch_work = data.get('sch_work')
    location = data.get('location')
    contact = data.get('number')
    profile = str(data.get('profile')).replace('[','').replace("'",'').replace(']','')
    name_of_owner = data.get('name_of_owner')
    wants = msg.text
    await state.finish()
    sendex(f'''INSERT INTO deals (user_id, clinic_name, type_clinic, sch_work, location, contact, profile,
name_of_owner, wants,time_created) values ("{msg.from_user.id}","{clinic_name}","{type_clinic}","{sch_work}",
"{location}","{contact}","{profile}","{name_of_owner}","{wants}","{datetime.datetime.now()}")''')
    send_excel('сотрудничество', [msg.from_user.id, clinic_name, type_clinic, sch_work, location, contact,
                             profile, name_of_owner, wants, datetime.datetime.now()])
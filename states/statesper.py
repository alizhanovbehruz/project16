from aiogram.dispatcher.filters.state import StatesGroup, State


class doctor_info(StatesGroup):
    full_name = State()
    email = State()
    account = State()
    number_phone = State()
    date_of_birth = State()
    skill = State()
    sphere = State()
    cert_b = State()
    med_cat = State()
    degree_a = State()
    consult_b = State()
    consult_lang = State()
    use_pc = State()
    method_conn = State()


class deals(StatesGroup):
    clinic_name = State()
    type_clinic = State()
    type_clinic2 =State()
    sch_work = State()
    location = State()
    contact = State()
    profile = State()
    profile2 =State()
    name_of_owner = State()
    wants = State()


class quesions(StatesGroup):
    question = State()
    confirm = State()


class admins_add(StatesGroup):
    info = State()


class admins_remove(StatesGroup):
    info = State()


class admins_post(StatesGroup):
    info = State()
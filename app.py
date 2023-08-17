from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api.sqlite import sendex
# from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

# sendex('Drop table "doctors";')
# sendex('''CREATE TABLE "doctors" (
# 	            "id"	INTEGER NOT NULL,
# 	            "chat_id"	TEXT ,
# 	            "full_name" TEXT,
# 	            "email" TEXT,
# 	            "account" TEXT,
# 	            "number" TEXT,
# 	            "date_birth" TEXT,
# 	            "skills" TEXT,
# 	            "sphere" TEXT,
# 	            "cert_b" TEXT,
# 	            "med_cat" TEXT,
# 	            "degree_a" TEXT,
# 	            "consult_b" TEXT,
# 	            "consult_lang" TEXT,
# 	            "use_pc" TEXT,
# 	            "method" TEXT,
# 	            "time_created" TEXT,
# 	            PRIMARY KEY("id" AUTOINCREMENT)
# );
# ''')
# sendex('''CREATE TABLE "admins" (
# 	            "id"	INTEGER NOT NULL,
# 	            "user_id"	TEXT ,
# 	            "full_name" TEXT,
# 	            PRIMARY KEY("id" AUTOINCREMENT) );
# ''')
# sendex('''CREATE TABLE "users" (
# 	            "id"	INTEGER NOT NULL,
# 	            "user_id"	TEXT ,
# 	            "full_name" TEXT,
# 	            "username" TEXT,
# 	            "time_created",
# 	            PRIMARY KEY("id" AUTOINCREMENT) );
# ''')
# sendex('''CREATE TABLE "deals" (
# 	            "id"	INTEGER NOT NULL,
# 	            "user_id"	TEXT ,
#                 "clinic_name" TEXT,
# 	            "type_clinic" TEXT,
# 	            "sch_work" TEXT,
# 	            "location" TEXT,
# 	            "contact" TEXT,
# 	            "profile" TEXT,
# 	            "name_of_owner" TEXT,
# 	            "wants" TEXT,
# 	            "time_created" TEXT,
# 	            PRIMARY KEY("id" AUTOINCREMENT) );
# ''')

async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

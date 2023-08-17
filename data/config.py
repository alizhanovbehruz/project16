# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
from utils.db_api.sqlite import sendex

BOT_TOKEN='5330260074:AAG8Bzuhy-sRYzBjYnoPPvbyhFk7mzcyjg8'
GROUP_ID = -1001735697853
ADMINS = lambda : ([int(i[0]) for i in sendex('select user_id from admins')])
print((ADMINS()))
IP = 'localhost'
# import os
# BOT_TOKEN = str(os.environ.get("BOT_TOKEN")) #botimiz tokeni
# ADMINS = list(os.environ.get("ADMINS")) # adminlar
# IP = str(os.environ.get("ip")) # hosting ip manzili
# PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))



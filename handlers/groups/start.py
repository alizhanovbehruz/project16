from loader import dp, bot
from aiogram import types
from filters.group_filter import IsGroup


@dp.message_handler(IsGroup())
async def exo(msg: types.Message):
    try:
        id = int(msg.reply_to_message.text.split('\n')[1].split(':')[1])
        await msg.answer(id)
        await bot.send_message(chat_id=id, text=msg.text)
    except:
        await msg.answer('В группе надо только отвечать на вопросы!!!')
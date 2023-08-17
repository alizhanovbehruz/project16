from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поделиться номер телефоном', request_contact=True)
        ],
        [
            KeyboardButton(text='◀Вернуться в главный меню')
        ],
    ],
    resize_keyboard=True
)


back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='◀Вернуться в главный меню')
        ],
    ],
    resize_keyboard=True
)

method_con = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Телефон')
        ],
        [
            KeyboardButton('Instagram')
        ],
        [
            KeyboardButton('Telegram')
        ],
        [
            KeyboardButton('WhatsApp')
        ]
    ]
)
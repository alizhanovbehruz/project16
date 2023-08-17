from aiogram.types import InlineKeyboardButton ,InlineKeyboardMarkup

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🧑🏼‍⚕️Раздел для врачей и специалистов', callback_data='section_doctors'),
        ],
        [
            InlineKeyboardButton(text='🤝Предложения о сотрудничестве', callback_data='section_deals'),
        ], 
        [
            InlineKeyboardButton(text='💎Раздел для рекламодателей', url='https://t.me/alieva_photography'),
        ],
        [
            InlineKeyboardButton(text='❓Задать вопрос', callback_data='section_queries'),
        ],

    ]
)


skills_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='До 5 лет', callback_data='skillss_do-5'),
        ],
        [
            InlineKeyboardButton(text='5 - 10 лет', callback_data='skillss_5-10'),
        ],
        [
            InlineKeyboardButton(text='10 - 15 лет', callback_data='skillss_10-15'),
        ],
        [
            InlineKeyboardButton(text='Более 15 лет', callback_data='skillss_15-bol'),
        ],

    ]
)

cert_ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Да', callback_data='cert_да'),
        ],
        [
            InlineKeyboardButton('Нет, просрочен', callback_data='cert_Нет-просрочен'),
        ],
        [
            InlineKeyboardButton('Обновляю',callback_data='cert_Обновляю')
        ]
    ]
)

consul = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Да', callback_data='consul_Да')
        ],
        [
            InlineKeyboardButton('Нет', callback_data='consul_Нет')
        ]
    ]
)
cons_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Русском',callback_data='conlang_Русском'),
        ],
        [
            InlineKeyboardButton('Узбекском',callback_data='conlang_Узбекском')
        ],
        [
            InlineKeyboardButton('Не важно', callback_data='conlang_Не-важно')
        ]
    ]
)

usepc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Уверенный',callback_data='usepc_Уверенный'),
        ],
        [
            InlineKeyboardButton('Только по необходимости',callback_data='usepc_Только-по-необходимости')
        ],
        [
            InlineKeyboardButton('Использую очень редко', callback_data='usepc_Использую-очень-редко')
        ]
    ]
)

send_conf = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('◀Вернуться в главный меню',callback_data='query_False'),
            InlineKeyboardButton('Отправить✅',callback_data='query_True')
        ]
    ]
)

from aiogram.types import InlineKeyboardButton ,InlineKeyboardMarkup

type_clin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Амбулаторно-поликлинический прием', callback_data='typeofclin_Амбулаторно')
        ],
        [
            InlineKeyboardButton('Дневной-стационар', callback_data='typeofclin_Дневной-стационар')
        ],
        [
            InlineKeyboardButton('Стационар', callback_data='typeofclin_Стационар')
        ],
        [
            InlineKeyboardButton('Диагностический-центр', callback_data='typeofclin_Диагностический-центр')
        ],
        [
            InlineKeyboardButton('Реабилитация', callback_data='typeofclin_Реабилитация')
        ],
        [
            InlineKeyboardButton('Патронажные-службы', callback_data='typeofclin_Патронажные-службы')
        ],
        [
            InlineKeyboardButton('Лаборатория', callback_data='typeofclin_Лаборатория')
        ],
        [
            InlineKeyboardButton('Другое', callback_data='typeofclin_another')
        ],
        [
            InlineKeyboardButton('Готово', callback_data='typeofclin_success')
        ],
    ],
)

profile_ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Терапевтический',callback_data='profilede_Терапевтический')
        ],
        [
            InlineKeyboardButton('Хирургический',callback_data='profilede_Хирургический')
        ],
        [
            InlineKeyboardButton('Стоматологический',callback_data='profilede_Стоматологический')
        ],
        [
            InlineKeyboardButton('Педиатрический',callback_data='profilede_Педиатрический')
        ],
        [
            InlineKeyboardButton('Многопрофильный',callback_data='profilede_Многопрофильный')
        ],
        [
            InlineKeyboardButton('Другое', callback_data='profilede_another')
        ],
        [
            InlineKeyboardButton('Готово', callback_data='profilede_success')
        ],
    ]
)

async def type_cl(data, reply_keyb):
    list_inlin = reply_keyb['inline_keyboard']
    for keyb in range(len(list_inlin)):
        if list_inlin[keyb][0]['callback_data'] == data:
            if list_inlin[keyb][0]['text'].startswith('✅'):
                remove_list = list_inlin[keyb][0]['text']
                list_inlin[keyb][0]['text'] = list_inlin[keyb][0]['text'][1:]
            else:
                remove_list = False
                list_inlin[keyb][0]['text'] = '✅'+list_inlin[keyb][0]['text']
    return [InlineKeyboardMarkup(inline_keyboard=list_inlin), remove_list]


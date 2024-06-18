from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from keyboards.inline.callback_date import course_callback, book_callback

ilove = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Present Simple ➰", callback_data="courses"),
        InlineKeyboardButton(text="Present Continuous ➰", callback_data="books"),
    ],
    [
        InlineKeyboardButton(text="Future Simple ➰", callback_data="o"),
        InlineKeyboardButton(text="Past Simple ➰", callback_data="d"),
    ],
    [
        InlineKeyboardButton(text="Modal verbs", callback_data="go"),
    ]
])

st = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇺🇿", callback_data="uzb"),
        InlineKeyboardButton(text="🇺🇸", callback_data="usa"),
        InlineKeyboardButton(text="🇷🇺", callback_data="rus"),
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga qaytish", callback_data="back"),
    ]
])

til = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bayonot", callback_data="bayon"),
        InlineKeyboardButton(text="Inkor qilish", callback_data="inkor"),
        InlineKeyboardButton(text="Savol", callback_data="savol"),
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga qaytish", callback_data="back"),
    ]
])

il = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Important", callback_data="import"),
        InlineKeyboardButton(text="Denial", callback_data="denial"),
        InlineKeyboardButton(text="Question", callback_data="ques"),
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga qaytish", callback_data="back"),
    ]
])

lil = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Утверждение", callback_data="utver"),
        InlineKeyboardButton(text="Отрицание", callback_data="otris"),
        InlineKeyboardButton(text="Вопрос", callback_data="vop"),
    ],
    [
        InlineKeyboardButton(text="🔙 Orqaga qaytish", callback_data="back"),
    ]
])

bac = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Orqaga qaytish", callback_data="back"),
    ]
])

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

op = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎲 Game Words"),
            KeyboardButton(text="📚 Times Grammar")
        ],
        [
            KeyboardButton(text="❔ Questions"),
            KeyboardButton(text="📖 Ielts Words")
        ],
    ],
    resize_keyboard=True
)
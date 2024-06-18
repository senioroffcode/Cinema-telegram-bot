from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main import op
from loader import dp

@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=op)

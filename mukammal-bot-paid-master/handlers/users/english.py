from aiogram import types
from keyboards.default.game import game, soz, green, rain, omlet, lef, ubor, dog, toy, st
from keyboards.default.main import op
from loader import dp
from aiogram import types, Bot


@dp.message_handler(text="🎲 Game Words")
async def words(message: types.Message):
    await message.answer("O`yinda nechta so`z bo`lsin? 🇺🇿 \nСколько слов должно быть в игре? 🇷🇺\nHow many words should be in the game? 🇺🇸", reply_markup=soz)

@dp.message_handler(text="10 words")
async def game_words(message: types.Message):
    photo = "https://avatars.mds.yandex.net/i?id=4330175904fc5d934e63115316c98f96e4a4fe24-10806524-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=game)

# first word

@dp.message_handler(text="A) Window")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=green)


@dp.message_handler(text="B) Windy")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=green)


@dp.message_handler(text="C) Woniday")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=green)

# second word

@dp.message_handler(text="C) GreenPeace")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/i?id=3d2511bbb34f524cf3f48311182462dcaff3f95e-8451085-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=rain)


@dp.message_handler(text="A) Green vegetable")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=rain)


@dp.message_handler(text="B) waterfall")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=rain)

#third words


@dp.message_handler(text="C) reindeer")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/3345576/qdpt61xcuGg4WaTLk5XOtg2422/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=omlet)


@dp.message_handler(text="A) to sow")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=omlet)


@dp.message_handler(text="B) power socket")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=152579b343c738cb6c4ee70697cad500d03f3bc8-10686310-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=omlet)


#four words

@dp.message_handler(text="B) scrambled eggs")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/i?id=f90ed2a0c3fdba528ed7068800b72fea2d2bb249-4502683-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=lef)


@dp.message_handler(text="A) bowler")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=f90ed2a0c3fdba528ed7068800b72fea2d2bb249-4502683-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=lef)


@dp.message_handler(text="C) sponge")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/i?id=f90ed2a0c3fdba528ed7068800b72fea2d2bb249-4502683-images-thumbs&n=13"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=lef)

# five words

@dp.message_handler(text="C) leaf")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/3126687/NpvbpgoPk7DDWG0gcrWOAQ3857/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)


@dp.message_handler(text="A) Italy")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/3126687/NpvbpgoPk7DDWG0gcrWOAQ3857/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)


@dp.message_handler(text="B) hair")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/3126687/NpvbpgoPk7DDWG0gcrWOAQ3857/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)

#six

@dp.message_handler(text="A) the mop")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/2400088/j08xLPqL12PCT_Ky6Pn8_w4025/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=dog)


@dp.message_handler(text="A) judge")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/2400088/j08xLPqL12PCT_Ky6Pn8_w4025/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=dog)


@dp.message_handler(text="B) sky")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/2400088/j08xLPqL12PCT_Ky6Pn8_w4025/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=dog)

#seven

@dp.message_handler(text="A) muzzle")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/7773669/F29KD6zVLhRrUE3zu3kX3A4396/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)


@dp.message_handler(text="A) belly")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/7773669/F29KD6zVLhRrUE3zu3kX3A4396/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)


@dp.message_handler(text="B) dog")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/7773669/F29KD6zVLhRrUE3zu3kX3A4396/ocr   "
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=ubor)

#eight

@dp.message_handler(text="C) muzzle")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/1804017/ECdZt-qbKXA0rJUvQKW-tQ7813/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=toy)


@dp.message_handler(text="A) belly")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/1804017/ECdZt-qbKXA0rJUvQKW-tQ7813/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=toy)


@dp.message_handler(text="B) dog")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/1804017/ECdZt-qbKXA0rJUvQKW-tQ7813/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=toy)

# nine

@dp.message_handler(text="A) toy")
async def wondow(message: types.Message):
    await message.answer("✅True")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/101700/XneBQL94bFynpypnzmOF1Q8236/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=st)


@dp.message_handler(text="B) soil")
async def windy(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/101700/XneBQL94bFynpypnzmOF1Q8236/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=st)


@dp.message_handler(text="C) beggar")
async def woniday(message: types.Message):
    await message.answer("❌❌❌")
    photo = "https://avatars.mds.yandex.net/get-images-cbir/101700/XneBQL94bFynpypnzmOF1Q8236/ocr"
    await message.answer_photo(photo=photo, caption="What is this?", reply_markup=st)

#ten
@dp.message_handler(text="B) street light")
async def wondow(message: types.Message):
    await message.answer("✅True\n\n Thank You for Complete the test", reply_markup=op)


@dp.message_handler(text="A) lace")
async def windy(message: types.Message):
    await message.answer("❌❌❌")


@dp.message_handler(text="B) club")
async def woniday(message: types.Message):
    await message.answer("❌❌")

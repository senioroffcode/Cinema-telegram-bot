from aiogram import types
from keyboards.inline.path import ilove,st, til, bac, il,lil
from loader import dp
from aiogram import types, Bot
from aiogram.types import Message, CallbackQuery


@dp.message_handler(text="📚 Times Grammar")
async def how(message: Message):
    await message.answer("Grammars", reply_markup=ilove)

@dp.callback_query_handler(text="courses")
async def how(call: CallbackQuery):
    await call.message.answer("<b>Present Simple ➰</b> \n\n🇺🇿 Qaysi tilda bolishligini tanlang? \n🇷🇺 Выберите, на каком языке?\n🇺🇸 Choose which language it is in?", reply_markup=st)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="uzb")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Present Simple ➰</b> \nQaysi formasini qoidadi chiqsin: ", reply_markup=til)
    await call.answer(cache_time=10)
    await call.message.delete()


@dp.callback_query_handler(text="bayon")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Bayonot</b>:\n\nI / We / You / They + V\nU / U / It + V + s (es)\n<i>I go to work every day</i> - Men har kuni ishga boraman\n\n<i>They usually play tennis every weekend</i> - Ular odatda har hafta oxiri tennis o'ynaydilar.\n\n<i>She brings me coffee every morning</i> - U menga har kuni ertalab kofe olib keladi.\n\n<i>It snows in winter</i>  - qishda qor yog'adi.\n\n<b>MUHIM</b>: Present Simple-da fe'lning shakli deyarli har doim asl shakliga to'g'ri keladi. Istisno uchinchi shaxs birlikdir <b>(he / she / it)</b> - unga -s oxiri qo'shiladi:\n\n<i>I ride</i> — She rides\n\n<i>I dream</i> — He dreams\n\nAgar fe'l <b>-s, -ss, -sh, -ch, -x, -o</b> bilan tugasa, unga -es oxiri qo'shiladi.\n\n<i>I wish</i> — She wishes\n\n<i>I teach</i> — She teaches\n\nAgar fe'l -y harfi bilan tugasa va undan oldin undosh qo'shilsa, unga -es oxiri qo'shiladi, lekin -y o'rniga -i qo'shiladi.\n\n<i>I try</i> — She tries\n\n<i>I fly</i> — He flies\n\nAgar fe'l -y harfi bilan tugasa va oldidan unli tovush qo'shilsa, unga -s oxiri ham qo'shiladi, lekin -y o'zgarmaydi.\n\n<i>I play</i> — She plays\n\n<i>I stay</i> — He stays", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="inkor")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Inkor qilish:</b>\n\nInkor gap tuzish uchun mavzu va fe’l orasiga yordamchi fe’l qo’yish kerak.\n\nI / We / You / They + don't (don't) + V \n\nShe / He / It + doesn't (doesn't) + V \n\n<i>I don't go to school every day</i> - Men har kuni maktabga bormayman\n\n<i>They don't drink beer</i> - ular pivo ichishmaydi\n\n<i>He doesn't like the weather in London</i> - U Londondagi ob-havoni yoqtirmaydi\n\n<i>He doesn't drive the car</i> - U mashinani haydamaydi\n\nInkorni inkor olmoshlari va ergash gaplar yordamida ham ifodalash mumkin.\n\n<i>No one speaks Arabic</i> - hech kim arabcha gapirmaydi\n\n<i>I don't do anything</i> - men hech narsa qilmayman", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="savol")
async def sa(call: CallbackQuery):
    await call.message.answer("<b>Savol:</b>\n\nSo‘roq gaplar tuzilayotganda ko‘makchi fe’l mavzudan va ergash gapdan oldin qo‘yiladi. Odatda gap boshida.\n\nDo + I / we / you / they + V?\n\nDoes + she / he / it + V ?\n\n<i>Do you like pizza?</i> - Sizga pizza yoqadimi?\n\n<i>Do they play football?</i> - Ular futbol o'ynashadimi?\n\n<i>Does he study Russian?</i> — U rus tilini o‘rganyaptimi?\n\n<i>Does he live in Spain?</i> - U Ispaniyada yashaydimi?\n\nBa'zan so'roq gapda so'roq so'zlari va iboralar qo'llaniladi, bu suhbatdoshga to'g'riroq va to'g'ri savol berishga yordam beradi. Bunday so'zlarga quyidagilar kiradi: qancha vaqt (qancha vaqt), nima uchun (nima uchun), qaerda (qaerda) va boshqalar. Boshqa zamonlarda bo'lgani kabi ular Present Simplening so'roq qurilishidan oldin gapning eng boshida qo'yiladi.\n\nQW + do (does) + I / We / You / They / She / He / It + V ? \n\n<i>Where does he live in Prague?</i> - U Pragada qayerda yashaydi?\n\n<i>Why do you drink green tea?</i> - Nega yashil choy ichasiz?\n\nPresent Simple bilan gapda yordamchi fe’l kelganda asosiy fe’ldan -s oxiri yo‘qoladi. O'ylab ko'ring, bu o'ziga xos magnit bu oxirni o'ziga tortadi. Bu Present Simple ning inkor va so'roq shakllariga taalluqlidir. MUHIM: ba'zan <b>do / does</b> yordamchi fe'li tasdiqlovchi jumlalarda ifoda va yorqinlikni qo'shish uchun topilishi mumkin.\n\n<i>I want to try it</i> - men buni sinab ko'rmoqchiman.\n\n<i>Mary knows how to cook</i> - Meri haqiqatan ham pishirishni biladi", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

#USA

@dp.callback_query_handler(text="usa")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Present Simple ➰</b> \nWhich form is the rule: ", reply_markup=il)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="import")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Statement</b>:\n\nI / We / You / They + V\nU / U / It + V + s (es)\n<i>I go to work every day</i> - I go to work every day\n\n<i>They usually play tennis every weekend</i> - They usually play tennis every weekend.\n\n<i>She brings me coffee every morning</i> - He brings me coffee every morning.\n\n<i>It snows in winter</i> - it snows in winter.\n\n<b>IMPORTANT</b>: fe in Present Simple The form of 'l almost always corresponds to the original form.", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="denial")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Negation:</b>\n\nTo make a negative sentence, you need to put an auxiliary verb between the subject and the verb.\n\nI / We / You / They + don't (don't ) + V \n\nShe / He / It + doesn't (doesn't) + V \n\n<i>I don't go to school every day</i> - I don't go to school every day\n \n<i>They don't drink beer</i> - they don't drink beer\n\n<i>He doesn't like the weather in London</i> - He doesn't like the weather in London\n\n <i>He doesn't drive the car</i> - He doesn't drive the car\n\nNegation can also be expressed using negative pronouns and adverbs.\n\n<i>No one speaks Arabic</i> - no one does not speak Arabic\n\n<i>I don't do anything</i> - I don't do anything", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="ques")
async def sa(call: CallbackQuery):
    await call.message.answer("<b>Question:</b>\n\nWhen making interrogative sentences, the auxiliary verb is placed before the subject and the subordinate clause. Usually at the beginning of the sentence.\n\nDo + I / we / you / they + V?\n\nDoes + she / he / it + V ?\n\n<i>Do you like pizza?</i> - To you do you like pizza?\n\n<i>Do they play football?</i> - Do they play football?\n\n<i>Does he study Russian? \n\nDoes he live in Spain?</i> It helps to ask the right questions. Such words include: how long (how long), why (why), where (where) and others. As in other tenses, they are placed at the beginning of the sentence before the interrogative construction of the Present Simple.\n\nQW + do (does) + I / We / You / They / She / He / It + V ? \n\n<i>Where does he live in Prague?</i> - Where does he live in Prague?\n\n<i>Why do you drink green tea?</i> - Why do you drink green tea?\n \nIn a sentence with Present Simple, the -s ending is lost from the main verb when the auxiliary verb appears. Think of it as a kind of magnet that attracts this end. This applies to the negative and interrogative forms of the Present Simple. IMPORTANT: sometimes the auxiliary verb <b>do / does</b> can be found in affirmative sentences to add expression and brightness.\n\n<i>I want to try it</i> - I want to try it I want to try.\n\n<i>Mary knows how to cook</i> - Mary really knows how to cook", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()



#RUS

@dp.callback_query_handler(text="rus")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Present Simple ➰</b> \nКакая форма правила: ", reply_markup=lil)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="utver")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Утверждение</b>:\n\nI / We / You / They + V\nU / U / It + V + s (es)\n<i>Я хожу на работу каждый день</i> - Я хожу на работу каждый день\n\n<i>Они обычно играют в теннис каждые выходные</i> - Они обычно играют в теннис каждые выходные.\n\n<i>Она приносит мне кофе каждое утро</i> - Он приносит мне кофе каждое утро.\n\n<i>Зимой идет снег</i> - зимой идет снег.\n\n<b>ВАЖНО</b>: fe в Present Simple Форма 'l почти всегда соответствует исходной форме.", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="otris")
async def wow(call: CallbackQuery):
    await call.message.answer("<b>Отрицание:</b>\n\nЧтобы составить отрицательное предложение, между подлежащим и глаголом нужно поставить вспомогательный глагол.\n\nЯ / Мы / Вы / Они + не (не ) + V \n\nОна/Он/Оно + не (не) + V \n\n<i>Я не хожу в школу каждый день</i> - Я не хожу в школу каждый день\n \n<i>Они не пьют пиво</i> - Они не пьют пиво\n\n<i>Ему не нравится погода в Лондоне</i> - Он не пьет Мне нравится погода в Лондоне\n\n <i>Он не водит машину</i> - Он не водит машину\n\nОтрицание также можно выразить с помощью отрицательных местоимений и наречий.\n\n <i>Никто не говорит по-арабски</i> – никто не говорит по-арабски\n\n<i>Я ничего не делаю</i> – Я ничего не делаю", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()

@dp.callback_query_handler(text="vop")
async def sa(call: CallbackQuery):
    # await call.message.answer("<b>Вопрос:</b>\n\nПри построении вопросительных предложений вспомогательный глагол ставится перед подлежащим и придаточным предложением. Обычно в начале предложения.\n\nDo + I/we/you/they + V?\n\nDoes + she/he/it + V ?\n\n<i>Ты любишь пиццу?</ i> - Тебе нравится пицца?\n\n<i>Они играют в футбол?</i> - Они играют в футбол?\n\n<i>Он изучает русский язык? \n\nОн живет в Испании?</i> ", reply_markup=bac)
    await call.answer(cache_time=10)
    await call.message.delete()
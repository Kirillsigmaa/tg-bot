from aiogram import Dispatcher, Bot,types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import API_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def set_commads(bot: Bot):
    commads = [
        types.BotCommand(command="/start",description="Начать работу Киномана"),
        types.BotCommand(command="/help", description="Начать работу Киномана"),
        types.BotCommand(command="/about", description="Начать работу Киномана"),
        types.BotCommand(command="/shytka", description="Начать работу Киномана")

    ]
    await bot.set_my_commands(commads)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply('Здравствуйте, Сэр! 🖐 \nЯ Киноман 🎬, приятно познакомиться, что вас интересует? \n✨ Новинки? \n🎨 Классика? \nИли вы хотите что бы я вам рекомендацию для просмотра? 🧐', reply_markup= keyboard_vopros)

@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.reply('Вам не помогут')

@dp.message_handler(commands="about")
async def about(message: types.Message):
    await message.reply('Писал код для бота Ренат 💻\nИграл в бравл старс Миша 🎮')

@dp.message_handler(commands="shytka")
async def shytka(message: types.Message):
    await message.reply('Не шутите (шутка)',reply_markup=keyboard_wiki)


async def on_startup(dispatcher):
    await set_commads(dispatcher.bot)

keyboard_vopros = InlineKeyboardMarkup(row_width= 1)
button = InlineKeyboardButton('Что посоветуете❓', callback_data= 'zh_p_?')
button1 = InlineKeyboardButton('Какие самые популярные фильмы? 🧨', callback_data='k_s_p_f_?')
button2 = InlineKeyboardButton('Выбрать жанр 📺', callback_data='v_zh_?')
keyboard_vopros.add(button,button1,button2)


keyboard_zhanor = InlineKeyboardMarkup(row_width= 1)
button3 = InlineKeyboardButton ('Комедия 🤣', callback_data='comic')
button4 = InlineKeyboardButton ('Фантастика 🤖', callback_data='fantast')
button5 = InlineKeyboardButton ('Ужасы 👻', callback_data='yzhas')
button6 = InlineKeyboardButton ('Вернуться к вопросам 🤨', callback_data='v_k_v')
keyboard_zhanor.add(button3,button4,button5,button6)

keyboard_wiki = InlineKeyboardMarkup(row_width= 1)
button7 = KeyboardButton('Привет!✋', url='https://kartinkof.club/uploads/posts/2022-06/1655786469_44-kartinkof-club-p-kartinki-s-nadpisyu-moi-tebe-privetik-49.jpg')
button8 = KeyboardButton('Как дела❓', url='https://avatars.mds.yandex.net/i?id=a3f1660491e3e8fda0475dd4146fddd41e78f600-5351873-images-thumbs&n=13')
keyboard_wiki.add(button7,button8)

keyboard_back = InlineKeyboardMarkup(row_width= 1)
button9 = KeyboardButton('Назад 🔙', callback_data='back')
keyboard_back.add(button9)

@dp.callback_query_handler(lambda c: c.data == 'v_zh_?')
async def click_button(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,'Выбирайте жанр 📺',reply_markup=keyboard_zhanor)



@dp.callback_query_handler(lambda c: c.data == 'v_k_v')
async def click_button2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Возращаю вас к вопросам 🤗', reply_markup= keyboard_vopros)


@dp.callback_query_handler(lambda c: c.data == 'zh_p_?')
async def click_button2(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, 'https://gl.weburg.net/00/movies/1/420/original/405138.jpg',caption= 'Посоветую вам "Побег из Шоушенка" \nЖанр драма\nРежиссёр Фрэнк Дарабонт\nПродюсер Ники Марвин\nВозрастное ограничение: 16+',reply_markup=keyboard_back)
    await bot.send_message(callback_query.from_user.id,'Фильм основан на повести Стивена Кинга «Рита Хейуорт и спасение из Шоушенка». Он рассказывает историю банкира Энди Дюфрейна (Тим Роббинс), который приговорён к пожизненному заключению в государственной тюрьме Шоушенка за убийство своей жены и её любовника, несмотря на его заявления о невиновности. В течение следующих двух десятилетий он дружит с другим заключённым, контрабандистом Эллисом «Редом» Реддингом (Морган Фриман), и играет важную роль в операции по отмыванию денег, возглавляемой тюремным надзирателем Сэмюэлем Нортоном')

@dp.callback_query_handler(lambda c: c.data == 'k_s_p_f_?')
async def click_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,'Фильмы, набравшие 🔟 баллов из 🔟\n1. Джанго освобожденный (2012)\n2. Начало (2010)\n3. Петлитель (2012)\n4. Бесславные ублюдки (2009)\n5. Криминальное чтиво (1994)\n6. Властелин колец: Братство Кольца (2001)\n7. Список Шиндлера (1993)\n8. Крестный отец (1972)\n9. Звездные войны: эпизод IV - Новая надежда (1977)\n10. Матрица (1999)',reply_markup=keyboard_back)

@dp.callback_query_handler(lambda c: c.data == 'comic')
async def click_button(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, 'https://1gai.ru/uploads/posts/2022-07/1658917054_38.jpg',caption='Посоветую вам "Очень страшное кино"\nЖанры: комедия, пародия, слэшер\nРежиссёр: Кинен Айвори Уэйанс\nПродюсеры: Эрик Голд, Ли Мэйес\nВозрастное ограничение: 18+',reply_markup=keyboard_back)

@dp.callback_query_handler(lambda c: c.data == 'fantast')
async def click_button(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id,'https://mir-s3-cdn-cf.behance.net/project_modules/max_3840/ef0bfe28203139.56371454283f9.jpg',caption='Посоветую вам "Терминатор"\nЖанры: научная фантастика, боевик, триллер, неонуар\nРежиссёр: Джеймс Кэмерон\nПродюсер: Гэйл Энн Хёрд\nВозрастное ограничение: 18+',reply_markup=keyboard_back)

@dp.callback_query_handler(lambda c: c.data == 'yzhas')
async def click_button(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id,'https://upload.wikimedia.org/wikipedia/ru/thumb/c/c3/Alien_movie_poster.jpg/232px-Alien_movie_poster.jpg',caption='Посоветую вам "Чужой"\nЖанр:	научно-фантастический, фильм ужасов\nРежиссёр: Ридли Скотт\nПродюсеры:	Гордон Кэрролл, Дэвид Гайлер, Уолтер Хилл\nВозрастное ограничение: 18+',reply_markup=keyboard_back)

@dp.callback_query_handler(lambda c: c.data == 'back')
async def click_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Здравствуйте, Сэр! 🖐 \nЯ Киноман 🎬, приятно познакомиться, что вас интересует? \n✨ Новинки? \n🎨 Классика? \nИли вы хотите что бы я вам рекомендацию для просмотра? 🧐', reply_markup= keyboard_vopros)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from config import TOKEN

import random
from gtts import gTTS
import os

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)    # await message.answer_video(video=video)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('Song.ogg')
    await message.answer_voice(voice)

@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('TG02.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('training'))  # формат записи  mp3
async def training(message: Message):
    training_list = [
        "Тренировка 1:\\n 1. Скручивания: 3 подхода по 15 повторений\\n 2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n 3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\\n 1. Подъемы ног: 3 подхода по 15 повторений\\n 2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n 3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\\n 1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n 2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n 3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.mp3')
    audio = FSInputFile('training.mp3')
    await bot.send_audio(message.chat.id, audio)
    os.remove('training.mp3')

@dp.message(Command('send_training'))  # формат записи  mp3
async def send_training(message: Message):
    training_list = [
        "Тренировка 1:\\n 1. Скручивания: 3 подхода по 15 повторений\\n 2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\\n 3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\\n 1. Подъемы ног: 3 подхода по 15 повторений\\n 2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\\n 3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\\n 1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\\n 2. Горизонтальные ножницы: 3 подхода по 20 повторений\\n 3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio = FSInputFile('training.ogg')
    await bot.send_audio(message.chat.id, audio)
    os.remove('training.ogg')

@dp.message(Command('photo', prefix='&'))
async def photo(message: Message):
    list = ['https://i.pinimg.com/736x/ed/b8/e1/edb8e13206ed9e5a633e16f2d27be783.jpg',
            'https://www.loveyourcat.com/wp-content/uploads/2023/01/Group-of-different-cat-breeds-sitting-together-on-a-white-background-900x500.jpg',
            'https://i.ytimg.com/vi/_zD_uPj5VhE/maxresdefault.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Спасибо за фото')
@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какое фото', 'Непонятно что это такое', 'Не отправляй мне это больше']
    rand_answer = random.choice(list)
    await message.answer(rand_answer)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_unique_id}.jpg')
@dp.message(F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Иску́сственный интелле́кт (ИИ; искин; англ. artificial intelligence, AI) '
                         '— свойство искусственных интеллектуальных систем выполнять творческие функции, '
                         'которые традиционно считаются прерогативой человека[1] (не следует путать с искусственным сознанием); '
                         'наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ.')

@dp.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n/start \n/help \n /minitraining')


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет! {message.from_user.full_name}')  #  вариант first_name

@dp.message()  # третий вариант ввода свободного текста
async def test(message: Message):
    if message.text == 'тест':
        await message.answer('Тест пройден')

@dp.message()  # второй вариант ввода свободного текста
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)  # вариант по-другому  (message.from_user.id)

@dp.message()  # первый вариант ввода свободного текста
async def hello(message: Message):
    await message.answer('Я тебе ответила!')

async def main(dp):
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main(dp))
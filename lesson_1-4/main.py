import random
from aiogram import Bot, Dispatcher, executor, types
from constants import *


count = 0

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])  # Урок 2
async def help_command(message: types.Message) -> None:
    """Обработка команды /help"""
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    """Обработка команды /start"""
    await message.answer(text="Добро пожаловать в мой телеграм бот!")
    await message.delete()


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message) -> None:
    """Обработка команды /desc"""
    await message.answer(text="Это учебный проэкт телеграм бот!")
    await message.delete()


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message) -> None:
    """Обработка команды /count"""
    global count
    await message.answer(text=count)
    count += 1


@dp.message_handler()
async def check_zero(message: types.Message) -> None:
    """Проверка: есть ли '0' в сообщении пользователя"""
    if "0" in message.text:
        await message.answer("YES")
    else:
        await message.answer('NO')


@dp.message_handler()  # Урок1
async def acho(message: types.Message) -> None:
    """Функция принимает сообщение от пользователя и если сообщение состоит
        больше чем из одного слова, отправляет его назат пользователю в верхнем регистре
        иначе отвечает случайным символом алфавита"""
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper())
    else:
        await message.reply(random.choice(LETTERS))


if __name__ == "__main__":
    executor.start_polling(dp)

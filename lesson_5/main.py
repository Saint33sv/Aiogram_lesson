from aiogram import Bot, Dispatcher, executor, types
from constants import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    await message.answer("<em><b>Вас приветствует учебный бот!</b></em>", parse_mode="HTML")


@dp.message_handler(commands=["give"])
async def give_command(message: types.Message) -> None:
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJzOVkvotiKbNkmjjObUQOJkzEKJOOwAACFQADwDZPE81WpjthnmTnLwQ")
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message) -> None:
    await message.reply(message.text + "👌")

if __name__ == "__main__":
    executor.start_polling(dp)

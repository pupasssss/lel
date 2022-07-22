import logging
from aiogram import Bot, Dispatcher, executor, types
import marcup as nav
import random


API_TOKEN = '5462694930:AAEwAbrMBthewarPXeKz3qvc-ZFS-nMPX94'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("приветствую путешественник", reply_markup =nav.marcup)


@dp.message_handler(commands=['help'])
async def send_message(message: types.Message):
    
    await message.reply("денег нет но вы дершитесь")

@dp.message_handler()
async def send_message(message: types.Message):
    if message.text == "как дела":
        await bot.send_message(message.from_user.id, "нормально сам как?")

    elif message.text == "может по пивку":
        await bot.send_message(message.from_user.id, "давай 🍻")

    elif message.text == "купи мне машину":
        await bot.send_message(message.from_user.id, "держи от души 🛻")



    elif message.text == "рандомное число":
        await bot.send_message(message.from_user.id, "ваше число: " + str(random.randint(1, 1000)))



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
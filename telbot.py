import time 
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = "6746795964:AAEkpt505eXJ3Es0oWOMPYTOyGzZ90IFdbc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Да')).add(KeyboardButton('Нет'))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.reply(f"Привет, {user_name}! Программировал ли ты сегодня?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text.lower() == 'да')
async def yes_handler(message: types.Message):
    await message.reply("Отлично! Приятно поговорить с программистом. 🤖")
    # Заканчиваем общение после ответа "Да"
    await message.reply("Спасибо! Если у тебя есть еще вопросы, пиши мне снова. 😉", reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
    executor.start_polling(dp)
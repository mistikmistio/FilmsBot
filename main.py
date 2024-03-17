# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio
import random


TOKEN = '7128372360:AAEljbs4VvfvOcYvI_P0cBYNEYDg6aLHtYs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id='5890667637', text=f'Новый пользователь {message.from_user.username}')
    markup = InlineKeyboardMarkup(row_width=1)
    btnOne = InlineKeyboardButton(text='Получить название фильма 🎥', callback_data='startBut')
    markup.add(btnOne)
    with open('1.png','rb') as photo:
      await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'Привет {message.from_user.first_name}👋\n\nЧтобы получить название фильма из видео, нажми на кнопку ниже👇', reply_markup=markup)
    
@dp.callback_query_handler(lambda call: True)
async def rech_callback(call: types.CallbackQuery):
  
    if call.data == "startBut":
          markup = InlineKeyboardMarkup(row_width=1)
          sp1 = InlineKeyboardButton(text='🌟 Канал #1', callback_data='sp1', url='https://t.me/+QFilY3TlhIVkOGI6')
          sp2 = InlineKeyboardButton(text='🌟 Канал #2', callback_data='sp2', url='https://t.me/+rbtEN-qdr-Q5MDUy')
          sp3 = InlineKeyboardButton(text='🌟 Канал #3', callback_data='sp3', url='https://t.me/+I9pwnFsq3ekyMzBi')
          cheak = InlineKeyboardButton(text='✅ Проверить', callback_data='cheak')
          markup.add(sp1, sp2, sp3, cheak)
          await bot.send_message(call.from_user.id, 'Чтобы получить название фильма, нужно подписаться на наших спонсоров❤️', reply_markup=markup)
    
    elif call.data == 'cheak':
          await bot.send_message(call.from_user.id, 'Не вижу подписку на все каналы 🤨')
    
    else:
          pass
    
async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#кнопки
btn1 = KeyboardButton('как дела')
btn2 = KeyboardButton('может по пивку')
btn3 = KeyboardButton('купи мне машину')
btn4 = KeyboardButton('рандомное число')

marcup = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2,  btn3, btn4)
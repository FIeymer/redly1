from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Button 1'),
            KeyboardButton(text='Button 2'),
        ],
        [
            KeyboardButton(text='Inline menu'),
        ]
    ],
    resize_keyboard=True
)
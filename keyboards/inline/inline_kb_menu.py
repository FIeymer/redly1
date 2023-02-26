from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Soobschenie', callback_data='Soobschenie'),
                                        InlineKeyboardButton(text='link', url='https://www.youtube.com')
                                    ],
                                    [
                                         InlineKeyboardButton(text='alert', callback_data='alert')
                                    ]
                                ])
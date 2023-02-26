from aiogram import types
from aiogram. types import CallbackQuery

from loader import dp
from keyboards.inline import ikb_menu
from keyboards.default import kb_test

@dp.message_handler(text='Inline menu')
async def show_inline_menu(message: types.Message):
    await  message.answer('inline button is there', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Soobschenie')
async def send_message(call: CallbackQuery):
    await call.message.answer('кнопки заменены', reply_markup=kb_test)
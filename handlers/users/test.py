from aiogram import types
from loader import dp
from keyboards.default import kb_test

@dp.message_handler(text='test')
async def command_start(message: types.Message):
    await message.answer(f'Privet {message.from_user.full_name}! \n'
                         f'Testovyi tekst', reply_markup=kb_test)
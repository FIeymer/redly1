from aiogram import types
from loader import dp

@dp.message_handler(text='Button 1')
async def command_start(message: types.Message):
    await message.answer(f'Privet {message.from_user.full_name}! \n'
                         f'Ty vybral {message.text}')

@dp.message_handler(text='test')
async def command_start(message: types.Message):
    await message.answer(f'Privet {message.from_user.full_name}! \n'
                         f'Ty vybral {message.text}')

@dp.message_handler(text='100')
async def command_start(message: types.Message):
    await message.answer(f'Privet {message.from_user.full_name}! \n'
                         f'Ty vybral {message.text}')

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default import kb_menu

from loader import dp

from states import register

@dp.message_handler(Command('register'))
async def register_(message: types.Message):

    name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'{message.from_user.first_name}')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Hi, you are starting registration,\nEnter your name', reply_markup=name)
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer(f'{answer}, how old are you?')
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    age = data.get('test2')
    await message.answer(f'Ristration complete\n'
                         f'Your name {name}\n'
                         f'You are {age} years old', reply_markup=kb_menu)
    
    await state.finish()

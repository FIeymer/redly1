from aiogram import types

async def  set_defoult_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start','Zapustit bota'),
        types.BotCommand('help', 'pomosh'),
        types.BotCommand('register', 'start registration')
    ])
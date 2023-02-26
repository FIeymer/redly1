from loader import dp
from aiogram.types import ContentType, Message

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)

@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id

    photo_file_id = 'AgACAgIAAxkBAAIBQGPzkIDohMgPPtgndfgR9P-6XGczAAJZyzEbhPahS8ToDvysFVaZAQADAgADeQADLgQ'
    photo_url = 'sdf'
    photo_bytes = InputFile(path_or_bytesio='media/photo.png')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id)
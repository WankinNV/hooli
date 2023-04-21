import os
import uuid

from aiogram import types, Dispatcher
from aiogram.bot.bot import Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InputFile

from src.main_tg_bot.configs.bot_configs import bot_config
from src.main_tg_bot.callbacks.like_callbacks import get_like_kb
from src.main_tg_bot.configs.bot_state import *
from src.main_tg_bot.menu_texts import *
from src.services.model_inference import ModelInference
from src.services.services_configs.model_inference_cfg import InferenceConfig

bot = Bot(token=bot_config.token)
generator = ModelInference(InferenceConfig)


# Надо определиться, что конкретно делает команда старт выдает список всех команд?
# Как вариант, выдавать рандомную картинку с приветствием
async def start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)

    await message.answer(text="now we send you some photos")
    # img = generator.generate_img()
    os.makedirs(tmp_dir, exist_ok=True)
    image_name = f"{message.from_user.last_name}_{message.from_user.first_name}_" \
                 f"{str(uuid.uuid4())}.jpg"
    # image_path = os.path.join(tmp_dir, image_name)
    # Просто отправляю конкретную фотку в тг
    image_path = r'D:\IVAN_DAYUSTAN\SomeCode\Hool_bot\bot_hooligan\src\main_tg_bot\tmp\Savelyev_Ivan_22738.jpg'
    # cv2.imwrite(image_path, img)
    media_group = types.MediaGroup()
    media_group.attach_photo(InputMediaPhoto(media=InputFile(image_path)))
    await message.answer_photo(photo=InputFile(image_path),
                               reply_markup=get_like_kb(1))
    # os.remove(image_path)


async def help(message: types.Message):
    await message.answer(text=help_text)


# переход в состояние ожидания фото по команде
async def photo_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(text=start_photo_text)
    await state.set_state(WaitPhoto.wait_photo.state)


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text=cancel_text)


# Функция обработки фото
async def processing_photo(message: types.Message, state: FSMContext):
    os.makedirs(tmp_dir, exist_ok=True)
    image_name = f"{message.from_user.last_name}_{message.from_user.first_name}_" \
                 f"{str(uuid.uuid4())[-5:]}.jpg"
    # делаем проверку документа на фото и сохраняем
    if message.photo:
        photo_id = str(message.photo[-1].file_id)
        photo_file = await bot.get_file(file_id=photo_id)
        await bot.download_file(file_path=photo_file.file_path, destination=f'./{tmp_dir}{image_name}')
        await message.answer(text=answer_for_photo_text1)
        await state.finish()


# Фуункция для обработки документов-фотографий и текста
async def processing_doc_type(message: types.Message, state: FSMContext):
    os.makedirs(tmp_dir, exist_ok=True)
    image_name = f"{message.from_user.last_name}_{message.from_user.first_name}_" \
                 f"{str(uuid.uuid4())[-5:]}.jpg"
    # делаем проверку документа на фото и сохраняем
    if message.content_type == 'document' and message.document['mime_type'] == 'image/jpeg':
        doc_id = str(message.document['file_id'])
        doc_file = await bot.get_file(file_id=doc_id)
        await bot.download_file(file_path=doc_file.file_path, destination=f'./{tmp_dir}{image_name}')
        await message.answer(text=answer_for_photo_text2)
        await state.finish()
    else:
        await message.answer(text=wrong_photo_text)


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(cancel, commands=['cancel'], state=WaitPhoto.wait_photo)
    dp.register_message_handler(help, commands=["help"])
    dp.register_message_handler(photo_start, commands=["send"], state='*')
    dp.register_message_handler(processing_doc_type, content_types=['document', 'text'], state=WaitPhoto.wait_photo)
    dp.register_message_handler(processing_photo, content_types=['photo'],
                                state=WaitPhoto.wait_photo)

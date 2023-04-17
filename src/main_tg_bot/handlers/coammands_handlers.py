import os
import uuid

import cv2
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto, InputFile
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import ContentTypeFilter

from src.main_tg_bot.callbacks.like_callbacks import get_like_kb
from src.main_tg_bot.menu_texts import help_text
from src.services.model_inference import ModelInference
from src.services.services_configs.model_inference_cfg import InferenceConfig

generator = ModelInference(InferenceConfig)


async def start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)

    await message.answer(
        text="now we send you some photos",
    )
    img = generator.generate_img()
    tmp_dir = 'tmp/'
    os.makedirs(tmp_dir, exist_ok=True)

    image_name = f"{message.from_user.last_name}_{message.from_user.first_name}_" \
                 f"{str(uuid.uuid4())}.jpg"  # TODO make img_hash
    image_path = os.path.join(tmp_dir, image_name)
    cv2.imwrite(image_path, img)
    media_group = types.MediaGroup()
    media_group.attach_photo(InputMediaPhoto(media=InputFile(image_path)))
    await message.answer_photo(photo=InputFile(image_path),
                               reply_markup=get_like_kb(1))

    os.remove(image_path)


async def help(message: types.Message):
    await message.answer(text=help_text)


# класс для обработки состояния ожидания

class WaitPhoto(StatesGroup):
    wait_photo = State()


async def photo_start(message: types.Message, state: FSMContext):
    # await state.reset_state(with_data=True)
    await message.answer(text='Send photo and wait for magic')
    await state.set_state(WaitPhoto.wait_photo.state)


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("ok, cancel ")


async def choose_photo(message: types.Message, state: FSMContext):
    await message.answer(text='krasivoe')
    # await state.update_data(upload_photo=message.photo)
    await message.answer(str(message.photo[0]['file_id']))
    #await get_file(message.photo[0]['file_id'])
    # TODO: попробовать написать сохранеие через апи : https://qna.habr.com/q/699778


def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_message_handler(cancel, commands=['cancel'], state="*")
    dp.register_message_handler(help, commands=["help"], state="*")
    dp.register_message_handler(photo_start, commands=["send"], state="*")
    dp.register_message_handler(choose_photo, content_types='photo', state=WaitPhoto.wait_photo)

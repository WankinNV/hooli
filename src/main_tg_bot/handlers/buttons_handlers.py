from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData("matches", "action", "img_id")


async def mark_image(call: types.CallbackQuery, callback_data: dict):
    # img_id = callback_data["img_id"]
    # chat_id = call.from_user.id
    if callback_data["action"] == "1":
        ans = "you like it1"
    elif callback_data["action"] == "2":
        ans = "you dont like it2"
    elif callback_data["action"] == "3":
        ans = "ny vot3"
    elif callback_data["action"] == "4":
        ans = "ny vot4"

    await call.answer(text=ans)
    await call.answer(text="We mark your answer!", show_alert=True)


async def test_buttons(img_id=1):
    buttons = [types.InlineKeyboardButton(text='start', callback_data=cb.new(action='1', img_id='img_id')),
               types.InlineKeyboardButton(text='create new model', callback_data=cb.new(action='2', img_id='img_id')),
               types.InlineKeyboardButton(text='random interpolation',
                                          callback_data=cb.new(action='3', img_id='img_id')),
               types.InlineKeyboardButton(text='random image', callback_data=cb.new(action='4', img_id='img_id'))]

    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard


async def test(message: types.Message):
    pass


def register_testbut_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(
        mark_image, cb.filter(action=["1", "2", '3', '4']), state="*")

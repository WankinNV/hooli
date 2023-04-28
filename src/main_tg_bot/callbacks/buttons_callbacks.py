"""
Тут часть кода ,которую я тестировал. Не очень удачно. Так и не разобрался
"""

from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData("matches", "action", "img_id")


async def main_menu(call: types.CallbackQuery, callback_data: dict):
    # img_id = callback_data["img_id"]
    # chat_id = call.from_user.id
    if callback_data["action"] == "1":
        await call.message.answer(text='next step')
    # elif callback_data["action"] == "2":
    # ans = "you dont like it2"
    # elif callback_data["action"] == "3":
    # ans = "ny vot3"
    # elif callback_data["action"] == "4":
    # ans = "ny vot4"


def test_buttons(img_id=1):
    buttons = [InlineKeyboardButton(text='start', callback_data=cb.new(action='1')),
               InlineKeyboardButton(text='create new model', callback_data=cb.new(action='2', img_id='img_id')),
               InlineKeyboardButton(text='random interpolation',
                                    callback_data=cb.new(action='3', img_id='img_id')),
               InlineKeyboardButton(text='random image', callback_data=cb.new(action='4', img_id='img_id'))]

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def test_buttons2():
    buttons = [types.InlineKeyboardButton(text='OPOPOP')]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def press_first_but(call: types.CallbackQuery):
    await call.message.answer(text='pressed1')


def register_testbut_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(main_menu, cb.filter(action=["1", "2", '3', '4']), state="*")

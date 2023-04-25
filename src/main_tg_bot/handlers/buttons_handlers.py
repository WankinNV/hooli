from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def test_buttons(message: types.Message):
    kb = [[types.KeyboardButton(text='start')],
          [types.KeyboardButton(text='create new model')],
          [types.KeyboardButton(text='random interpolation')],
          [types.KeyboardButton(text='random image')]
          ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Hello friend, what u choose?', reply_markup=keyboard)

async def test(message: types.Message):
    pass
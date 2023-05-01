from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def main_menu_buttons():
    buttons = [
        [KeyboardButton(text="Create new model")],
        [KeyboardButton(text="Random interpolation")],
        [KeyboardButton(text="Random image")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard


def upload_menu_buttons():
    buttons = [
        [KeyboardButton(text="Upload one image")],
        [KeyboardButton(text="Upload many images")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons)
    return keyboard

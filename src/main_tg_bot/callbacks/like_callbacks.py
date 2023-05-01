from aiogram import types, Dispatcher
from aiogram.utils.callback_data import CallbackData

LikeCb = CallbackData("matches", "action", "img_id")


async def mark_image(call: types.CallbackQuery, callback_data: dict):
    # img_id = callback_data["img_id"]
    # chat_id = call.from_user.id
    if callback_data["action"] == "yes":
        ans = "you like it"
    elif callback_data["action"] == "no":
        ans = "you dont like it"

    await call.answer(text=ans)
    await call.answer(text="We mark your answer!", show_alert=True)


def get_like_kb(img_id=1):
    buttons = [
        types.InlineKeyboardButton(
            text="\U0000274c",
            callback_data=LikeCb.new(action="no", img_id=img_id),
        ),
        types.InlineKeyboardButton(
            text="\U00002705",
            callback_data=LikeCb.new(action="yes", img_id=img_id),
        ),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def register_like_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(
        mark_image, LikeCb.filter(action=["yes", "no"]), state="*"
    )

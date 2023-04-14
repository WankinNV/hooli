import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from src.main_tg_bot.callbacks.like_callbacks import register_like_callbacks
from src.main_tg_bot.configs.bot_configs import bot_config
from src.main_tg_bot.handlers.coammands_handlers import register_commands_handlers

storage = MemoryStorage()
bot = Bot(token=bot_config.token)
dp = Dispatcher(bot, storage=storage)

register_commands_handlers(dp)
register_like_callbacks(dp)


#@dp.message_handler(content_types=["photo"])
#async def ph(msg: types.Message):
#    await msg.reply(text='Vot eto krasota')


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="go to main menu"),
        BotCommand(command="/help", description="show help"),
        BotCommand(command="/send", description="send photo to hooliGAN")
    ]
    await bot.set_my_commands(commands)


async def main():
    await set_commands(bot)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())

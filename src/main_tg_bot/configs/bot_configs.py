import os

from dotenv import load_dotenv

from src.main_tg_bot.configs.bot_base_configs import TgBotConfig

load_dotenv()

bot_config = TgBotConfig(
    token=os.environ.get("BOT_TOKEN"))
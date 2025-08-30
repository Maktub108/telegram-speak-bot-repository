import logging
import asyncio
from aiogram import Bot, Dispatcher, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from handlers.start import cmd_start, cmd_myid, cmd_help
from handlers.practice import register_practice_handlers
from handlers.common import register_common_handlers

from config import config

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties())
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    try:
        # Регистрация обработчиков команд
        dp.message.register(cmd_start, Command(commands=["start"]))
        dp.message.register(cmd_myid, Command(commands=["myid"]))
        dp.message.register(cmd_help, Command(commands=["help"]))

        # Регистрация обработчиков практики
        register_practice_handlers(dp)

        # Регистрация общих обработчиков
        register_common_handlers(dp)

        logger.info("Бот запущен")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import config
from services.database import db
from utils.logger import setup_logging


# Настройка логирования
setup_logging()
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Глобальные переменные для хранения состояний
user_sessions = {}  # Здесь будем хранить состояния пользователей


async def register_handlers():
    """Регистрация всех обработчиков."""
    try:
        # Импортируем и регистрируем обработчики
        from handlers.start import register_start_handlers
        from handlers.common import register_common_handlers
        from handlers.practice import register_practice_handlers
        from handlers.support import register_support_handlers


        register_start_handlers(dp)
        register_common_handlers(dp)
        register_practice_handlers(dp)
        register_support_handlers(dp)


        logger.info("Все обработчики успешно зарегистрированы")
    except Exception as e:
        logger.error(f"Ошибка регистрации обработчиков: {e}")
        raise


async def on_startup():
    """Действия при запуске бота."""
    logger.info("Бот запускается...")
    await register_handlers()
    logger.info("Бот успешно запущен и готов к работе!")


async def on_shutdown():
    """Действия при остановке бота."""
    logger.info("Бот останавливается...")


async def main():
    """Основная функция запуска бота."""
    try:
        # Подключаем обработчики startup/shutdown
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)

        logger.info("Запуск бота в режиме polling...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")










import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Загружаем переменные окружения из.env файла
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Получение токена из.env
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не найден в переменных окружения!")
    logger.error("💡 Создайте файл .env с содержимым: BOT_TOKEN=your_token_here")
    exit(1)

# Инициализация бота и диспетчера
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)
dp = Dispatcher()

# Глобальные переменные для хранения состояний
user_sessions = {}


async def register_handlers():
    """Регистрация всех обработчиков."""
    try:
        # Импортируем обработчики через роутеры
        from handlers.start import router as start_router
        from handlers.practice import router as practice_router

        dp.include_router(start_router)
        dp.include_router(practice_router)

        logger.info("Все обработчики успешно зарегистрированы")
    except Exception as e:
        logger.error(f"Ошибка регистрации обработчиков: {e}")
        raise


async def on_startup():
    """Действия при запуске бота."""
    logger.info("Бот запускается...")
    await register_handlers()
    logger.info("Бот успешно запущен и готов к работе!")


async def main():
    """Основная функция запуска бота."""
    dp.startup.register(on_startup)

    logger.info("Запуск бота в режиме polling...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {e}")
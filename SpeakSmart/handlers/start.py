import logging
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command

from services.database import db
from config import config

logger = logging.getLogger(__name__)


async def cmd_start(message: Message):
    """Обработчик команды /start."""
    try:
        user = message.from_user

        # Добавляем пользователя в базу
        db.add_user(user.id, user.username, user.first_name, user.last_name)

        welcome_text = (
            "👋 *Добро пожаловать в SpeakSmart!*\n\n"
            "Я помогу вам практиковать разговорную речь на иностранном языке "
            "и отвечу на ваши вопросы.\n\n"
            "📚 *Доступные команды:*\n"
            "/start - Начать работу с ботом\n"
            "/practice - Начать языковую практику\n"
            "/support - Получить поддержку\n"
            "/help - Справка по использованию бота\n"
            "/myid - Узнать свой ID\n\n"
            "Выберите действие из меню или введите команду!"
        )

        await message.answer(welcome_text)
        logger.info(f"Пользователь {user.id} запустил бота")

    except Exception as e:
        logger.error(f"Ошибка в cmd_start: {e}")
        await message.answer("❌ Произошла ошибка при запуске бота. Попробуйте еще раз.")


async def cmd_myid(message: Message):
    """Обработчик команды /myid."""
    try:
        user_id = message.from_user.id
        response = (
            f"🆔 *Ваш ID:* `{user_id}`\n"
            f"🛡️ *ADMIN_ID из config:* `{config.ADMIN_ID}`\n\n"
            "Этот ID может понадобиться для идентификации при обращении в поддержку."
        )
        await message.answer(response)
        logger.info(f"Пользователь {user_id} запросил свой ID")

    except Exception as e:
        logger.error(f"Ошибка в cmd_myid: {e}")
        await message.answer("❌ Не удалось получить ваш ID.")


async def cmd_help(message: Message):
    """Обработчик команды /help."""
    help_text = (
        "📖 *Справка по использованию бота:*\n\n"
        "🎯 *Языковая практика (/practice):*\n"
        "- Бот отправляет голосовую фразу\n"
        "- Вы отвечаете голосовым сообщением\n"
        "- Бот проверяет ваш ответ и дает обратную связь\n\n"
        "🆘 *Поддержка (/support):*\n"
        "- Задайте вопрос текстом\n"
        "- Бот найдет ответ в базе знаний\n"
        "- Если ответа нет - чат передается оператору\n\n"
        "🔧 *Технические команды:*\n"
        "/start - Перезапустить бота\n"
        "/myid - Узнать свой идентификатор\n\n"
        "Для начала просто введите /practice или /support!"
    )
    await message.answer(help_text)


def register_start_handlers(dp):
    """Регистрация обработчиков стартовых команд."""
    try:
        # Регистрируем команды
        dp.message.register(cmd_start, Command("start"))
        dp.message.register(cmd_myid, Command("myid"))
        dp.message.register(cmd_help, Command("help"))

        logger.info("Стартовые обработчики успешно зарегистрированы")

    except Exception as e:
        logger.error(f"Ошибка регистрации стартовых обработчиков: {e}")
        raise







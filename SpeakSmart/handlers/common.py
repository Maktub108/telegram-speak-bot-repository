
from aiogram import Router, types
from aiogram.filters import Command

from services.database import db

router = Router()


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help."""
    help_text = (
        "📖 *Справка по использованию SpeakSmart*\n\n"
        "🎯 *Языковая практика:*\n"
        "Используйте /practice для начала тренировки. "
        "Бот отправит голосовую фразу, а вы попробуйте повторить её.\n\n"
        "❓ *Поддержка:*\n"
        "Используйте /support для обращения в поддержку. "
        "Бот ответит на частые вопросы или свяжет с оператором.\n\n"
        "📞 *Связь с оператором:*\n"
        "Если бот не смог ответить на ваш вопрос, "
        "чат будет автоматически передан оператору.\n\n"
        "💡 *Советы:*\n"
        "• Говорите четко и разборчиво\n"
        "• Используйте команды из меню для удобства\n"
        "• Не стесняйтесь обращаться за помощью!"
    )
    await message.answer(help_text)


# @router.message(Command("practice"))
# async def cmd_practice(message: types.Message):
#     """Обработчик команды /practice (заглушка)."""
#     await message.answer(
#         "🎯 *Режим языковой практики*\n\n"
#         "Эта функция находится в разработке. "
#         "Скоро вы сможете практиковать речь с помощью голосовых сообщений!\n\n"
#         "А пока можете воспользоваться поддержкой /support"
#     )


# @router.message(Command("support"))
# async def cmd_support(message: types.Message):
#     """Обработчик команды /support (заглушка)."""
#     await message.answer(
#         "❓ *Режим поддержки*\n\n"
#         "Эта функция находится в разработке. "
#         "Скоро вы сможете получить ответы на частые вопросы "
#         "и связаться с оператором!\n\n"
#         "А пока можете написать ваш вопрос текстом, "
#         "и мы постараемся помочь."
#     )


def register_common_handlers(dp):
    """Регистрация общих обработчиков."""
    dp.include_router(router)


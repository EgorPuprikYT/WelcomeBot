import disnake

class Config:
    # Обязательные параметры
    TOKEN = "ВАШ_ТОКЕН"              # Токен бота из Discord Developer Portal
    WELCOME_CHANNEL_ID = 123456789   # ID канала для приветствий
    
    # Настройки сообщений
    EMBED_COLOR = disnake.Color.blue()
    WELCOME_IMAGE_URL = None         # URL фонового изображения (или None)
    FOOTER_TEXT = "Copyright © 2025 | NOVA SPACE"  # Текст в подвале
    FOOTER_ICON = None               # URL иконки в подвале (или None)
    
    # Автоматизация
    AUTO_ROLE_ID = None              # ID роли для автовыдачи
    ADMIN_CHANNEL_ID = None          # ID канала для ошибок
    LOG_FILE = "logs/bot.log"        # Путь к файлу логов
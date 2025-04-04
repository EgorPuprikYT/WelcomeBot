# 🤖 Боты для Telegram и Discord | Telegram & Discord Bots

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Aiogram](https://img.shields.io/badge/Aiogram-2.x-green.svg)](https://docs.aiogram.dev/)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.0-purple.svg)](https://discordpy.readthedocs.io/)

Этот репозиторий содержит коллекцию мощных ботов для Telegram и Discord с разным функционалом — от автоматической модерации до интеграции с внешними API.

This repository contains a collection of powerful Telegram and Discord bots with various functionalities — from auto-moderation to external API integrations.

---

## 📂 Содержание | Table of Contents
- [Проекты | Projects](#-проекты--projects)
- [Технологии | Technologies](#-технологии--technologies)
- [Установка | Installation](#-установка--installation)
- [Конфигурация | Configuration](#-конфигурация--configuration)
- [Скриншоты | Screenshots](#-скриншоты--screenshots)
- [Лицензия | License](#-лицензия--license)

---

## 🚀 Проекты | Projects

### 🤖 Telegram-боты
1. **Бот для заказов еды**  
   - Меню с категориями из БД  
   - Корзина и оплата через ЮKassa/Stripe  
   - Система подписок (премиум-доступ)  
   - Админ-панель  

2. **Бот-ассистент с AI**  
   - Ответы на вопросы через GPT-3.5  
   - Генерация изображений через Stable Diffusion  
   - Конвертер голоса в текст  

### 🎮 Discord-боты
1. **Модератор сервера**  
   - Автоматический бан за мат (нейросеть BERT)  
   - Логирование действий в канал  
   - Капча для новых участников  

2. **Музыкальный бот**  
   - Воспроизведение музыки из YouTube/Spotify  
   - Плейлисты и очередь треков  
   - Распознавание музыки через Shazam API  

---

## 🛠 Технологии | Technologies
- **Языки**: Python 3.9+  
- **Библиотеки**:  
  - Telegram: `aiogram`, `python-telegram-bot`  
  - Discord: `discord.py`, `nextcord`  
  - AI: `openai`, `transformers`, `diffusers`  
  - Базы данных: `PostgreSQL`, `Redis`  
  - Платежи: `yookassa`, `stripe`  

---

## ⚙️ Установка | Installation
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-ник/ваш-репозиторий.git
   cd ваш-репозиторий
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Настройте конфигурацию (см. [Конфигурация](#-конфигурация--configuration)).

---

## 🔧 Конфигурация | Configuration
Создайте файл `.env` в корне проекта:
```ini
# Telegram
TELEGRAM_TOKEN=ваш_токен
ADMIN_IDS=123456789,987654321

# Discord
DISCORD_TOKEN=ваш_токен
DISCORD_GUILD_ID=ваш_id_сервера

# База данных
DATABASE_URL=postgresql://user:password@localhost/dbname

# OpenAI
OPENAI_API_KEY=ваш_ключ
```

---

## 📸 Скриншоты | Screenshots
| Telegram Bot | Discord Bot |
|--------------|-------------|
| ![Telegram](https://via.placeholder.com/300) | ![Discord](https://via.placeholder.com/300) |

---

## 📜 Лицензия | License
Этот проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

---

## 📞 Контакты | Contacts
- Telegram: [@egor_puprik](https://t.me/ваш_ник)  
- Email: novaspace618@gmail.com  

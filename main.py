import disnake
from disnake.ext import commands
import random
import logging
import os
from config import Config

# Настройка логирования
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(Config.LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix=Config.PREFIX if hasattr(Config, "PREFIX") else "!",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    logging.info(f"Бот {bot.user} запущен!")
    logging.info(f"Подключен к серверам: {[g.name for g in bot.guilds]}")

@bot.event
async def on_member_join(member):
    try:
        # Выдача роли
        if Config.AUTO_ROLE_ID:
            role = member.guild.get_role(Config.AUTO_ROLE_ID)
            if role and member.guild.me.guild_permissions.manage_roles:
                await member.add_roles(role)
                logging.info(f"Выдана роль {role.name} пользователю {member}")

        # Приветственное сообщение
        with open("greetings.txt", "r", encoding="utf-8") as f:
            greetings = [line.strip() for line in f if line.strip()]
        
        greeting = random.choice(greetings).format(
            user=member.mention,
            guild=member.guild.name
        )
        
        channel = bot.get_channel(Config.WELCOME_CHANNEL_ID)
        if channel:
            embed = disnake.Embed(
                description=greeting,
                color=Config.EMBED_COLOR
            )
            
            if Config.WELCOME_IMAGE_URL:
                embed.set_image(url=Config.WELCOME_IMAGE_URL)
            
            embed.set_footer(
                text=Config.FOOTER_TEXT,
                icon_url=Config.FOOTER_ICON
            )
            
            await channel.send(embed=embed)
            logging.info(f"Отправлено приветствие для {member}")

    except Exception as e:
        logging.error(f"Ошибка: {str(e)}", exc_info=True)
        if Config.ADMIN_CHANNEL_ID:
            admin_channel = bot.get_channel(Config.ADMIN_CHANNEL_ID)
            if admin_channel:
                await admin_channel.send(f"⚠ Ошибка при приветствии {member.mention}")

if __name__ == "__main__":
    try:
        bot.run(Config.TOKEN)
    except Exception as e:
        logging.critical(f"Ошибка запуска: {str(e)}")
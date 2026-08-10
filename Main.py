# -*- coding: utf-8 -*-
import asyncio
import logging
import time

# Все зависимости
import telebot
import telethon
import requests
import socks
import cryptg
import aiohttp
import qrcode
from PIL import Image

logging.basicConfig(level=logging.INFO)

# Твой токен
TOKEN = '8440312533:AAGCujc57zRNTFRjIAAdm8FenbEe_yBR10Q'

# Создаем бота
bot = telebot.TeleBot(TOKEN)

# Простой обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "✅ Бот работает!\n\n"
        "📦 Все зависимости установлены:\n"
        f"• pyTelegramBotAPI: {telebot.__version__}\n"
        f"• telethon: {telethon.__version__}\n"
        f"• requests: {requests.__version__}\n"
        "• pysocks: установлен\n"
        "• cryptg: установлен\n"
        "• aiohttp: установлен\n"
        "• qrcode: установлен\n"
        "• Pillow: установлен"
    )

# Обработчик для проверки что бот жив
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id, "🏓 Pong!")

# Обработчик остальных сообщений
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        f"📩 Вы написали: {message.text}\n\n"
        f"🆔 Ваш ID: {message.from_user.id}"
    )

# Запуск бота
if __name__ == '__main__':
    print("🚀 Бот запускается...")
    print("✅ Все зависимости загружены")
    print("🤖 Бот готов к работе")
    
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        time.sleep(3)

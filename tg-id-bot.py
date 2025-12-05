import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def startKBoard(message):
    bot.send_message(
        message.chat.id,
        f'Ваш ID — <code>{message.from_user.id}</code>\nСообщите его администратору',
        parse_mode="HTML"
    )

if __name__ == "__main__":
    print("Бот запущен...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)

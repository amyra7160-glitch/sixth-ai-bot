import telebot
from openai import OpenAI
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
أنت مدرس خبير بالسادس الإعدادي العراقي.
اشرح بطريقة مبسطة.
ركز على الأسئلة الوزارية.
إذا السؤال خارج المنهج اعتذر بلطف.
"""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message.text}
        ]
    )

    bot.reply_to(message, response.choices[0].message.content)

bot.polling()

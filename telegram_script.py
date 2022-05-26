import telebot
from chatbot_horoscope import get_message_response
TOKEN = "5231433351:AAFTLNhTv17LSli8s_MS1kOqDwS75uKvopQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,get_message_response(message) )

bot.polling(none_stop=True, interval=0)
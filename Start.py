python
import telebot


bot = telebot.TeleBot('6130934441:AAEpr6KGlPcUSKZmERIWiy20jv97yEJT5bs')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "مرحبًا بك! أهلاً بك في البوت.")

# ابدأ البوت
bot.polling()
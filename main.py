import telebot;
bot = telebot.TeleBot('');

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напишите -Привет-")
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю, напишите -/help-")

bot.polling(none_stop=True, interval=0)
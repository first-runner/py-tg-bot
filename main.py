import telebot;
from telebot import types;
bot = telebot.TeleBot('')

#@bot.message_handler(content_types=['text', 'document', 'audio'])
#def get_text_message(message):
#    if message.text == "Привет":
#        bot.send_message(message.from_user.id, "Привет, чем я могу помочь?")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напишите -Привет-")
#    else:
#        bot.send_message(message.from_user.id, "Я вас не понимаю, напишите -/help-")

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text', 'document', 'audio'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.form_user.id, "Как тебя завут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Напишите -/reg-")
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет?")
    bot.register_next_step_handler(message, get_age)
def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста!")
    #bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя завут '+name+' '+surname+'?')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе '+str(age)+' лет, тебя завут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callbeck_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Запомню!")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Повторим")
        bot.register_next_step_handler(call, start)

bot.polling(none_stop=True, interval=1)
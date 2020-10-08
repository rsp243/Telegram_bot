import telebot
bot = telebot.TeleBot('926414545:AAH8KbWEVavTkXQAtHgyJk7U9zDSce0jiXk')
spis = ["Север", "Запад", "Юг", "Восток"]
n = 0
@bot.message_handler(commands=['start'])
def start_message(message):
    button1 = telebot.types.InlineKeyboardButton(text='Влево', callback_data='left')
    button2 = telebot.types.InlineKeyboardButton(text='Вправо', callback_data='right')
    klava = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1, button2)
    bot.send_message(message.chat.id, 'Здравствуйте, Вы смотрите на север, куда вы равзвернулись: влево или вправо?',
                     reply_markup=klava)
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global n
    if call.data == "left":
        n -= 1
    if call.data == "right":
        n += 1
    bot.send_message(call.message.chat.id, text=n)
bot.polling()
import telebot
bot = telebot.TeleBot('')
spis = ["Север", "Запад", "Юг", "Восток"]
n = 0
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Здравствуйте, Вы смотрите на север.')
    klava = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = telebot.types.InlineKeyboardButton(text='Влево')
    button2 = telebot.types.InlineKeyboardButton(text='Вправо')
    klava.add(button1)
    klava.add(button2)
    bot.send_message(message.from_user.id, 'Если Вы повернулись куда-то, нажмите соответствующую кнопку.',  reply_markup=klava)
@bot.message_handler(content_types=['text'])
def welcome(message):
    global n
    if message.text == 'Влево':
        n -= 1
    else:
        n += 1
    if n == -1:
        n = 3
    if n == 4:
        n = 0
    klava = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = telebot.types.InlineKeyboardButton(text='Влево')
    button2 = telebot.types.InlineKeyboardButton(text='Вправо')
    klava.add(button1)
    klava.add(button2)
    bot.send_message(message.from_user.id, text=f'Вы смотрите на {spis[n]}', reply_markup=klava)
bot.polling()

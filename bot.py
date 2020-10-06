import telebot
bot = telebot.TeleBot('926414545:AAH8KbWEVavTkXQAtHgyJk7U9zDSce0jiXk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, Вы смотрите на север, куда вы равзвернулись?'
                                      'Влево или вправо?')
x = 1
@bot.message_handler(content_types=['text'])
def send_text(message):
    global x
    if message.text.lower() == 'влево' and x == 1:
        x = 2
        bot.send_message(message.chat.id, 'Вы смотрите на запад')
    elif message.text.lower() == 'влево' and x == 2:
        x = 3
        bot.send_message(message.chat.id, 'Вы смотрите на юг')
    elif message.text.lower() == 'влево' and x == 3:
        x = 4
        bot.send_message(message.chat.id, 'Вы смотрите на восток')
    elif message.text.lower() == 'влево' and x == 4:
        x = 1
        bot.send_message(message.chat.id, 'Вы смотрите на север')
    elif message.text.lower() == 'вправо' and x == 1:
        x = 4
        bot.send_message(message.chat.id, 'Вы смотрите на восток')
    elif message.text.lower() == 'вправо' and x == 2:
        x = 1
        bot.send_message(message.chat.id, 'Вы смотрите на север')
    elif message.text.lower() == 'вправо' and x == 3:
        x = 2
        bot.send_message(message.chat.id, 'Вы смотрите на запад')
    elif message.text.lower() == 'вправо' and x == 4:
        x = 3
        bot.send_message(message.chat.id, 'Вы смотрите на юг')
bot.polling()
import telebot
from telebot import types
bot = telebot.TeleBot('926414545:AAH8KbWEVavTkXQAtHgyJk7U9zDSce0jiXk')
spis = ["Север", "Запад", "Юг", "Восток"]
n = 0
r = 0
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Здравствуйте, Вы смотрите на север')
    klava = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Влево', callback_data='left')
    button2 = types.InlineKeyboardButton(text='Вправо', callback_data='right')
    klava.add(button1)
    klava.add(button2)
    bot.send_message(message.from_user.id, text="Куда вы повернулись?", reply_markup=klava)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "left":
        n -= 1
    elif call.data == "right":
        n += 1
    bot.send_message(call.message.chat.id, n)
bot.polling()
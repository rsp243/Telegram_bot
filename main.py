import telebot, requests
from telebot import types
import os

quest = requests.get(os.environ['jsonToQuest']).json()
ans = requests.get(os.environ['jsonToAns']).json()

bot = telebot.TeleBot(os.environ['token'])


def formMarkup(id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in quest[id]['answers']:
        for j in range(len(ans)):
            if i == ans[j]['id']:
                item = types.KeyboardButton(ans[j]['text'])
        markup.add(item)
    return markup


keyboardStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardStart.add('В самое начало')


def sendMessage(id, message):
    k = 0
    for j in range(len(quest)):
        if quest[j]["id"] == id:
            k += 1
            keyboard = formMarkup(j)
            if quest[j]["message_before_question"] != '':
                bot.send_message(message.chat.id, f'{quest[j]["message_before_question"]}')
            bot.reply_to(message, f'{quest[j]["text"]}', reply_markup=keyboard)
    if k == 0:
        bot.send_message(message.chat.id, 'Диалог дальше ещё не сформирован,'
                                          ' администраторы уже работают над этим, обратитесь через почту'
                                          ' к создателю этого бота -> reshetov.semjon@gmail.com',
                         reply_markup=keyboardStart)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    sendMessage(1, message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.type == 'private':
        for i in range(len(ans)):
            if ans[i]['text'] == message.text:
                sendMessage(ans[i]['goto'], message)
        if message.text == 'В самое начало':
            sendMessage(1, message)
        if message.text == 'Давай':
            bot.send_message(message.chat.id, 'Внимательно просмотри карту, а лучше сохрани!')
            bot.send_photo(message.chat.id, 'https://disk.yandex.ru/client/recent?idApp=client&dialog=slider&idDialog=%2Fdisk%2F%D0%94%D0%BB%D1%8F%20%D1%88%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%8C%D1%82%D0%B5%D0%B2%D0%BE%20%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D0%BB.jpg')
            sendMessage(3, message)

bot.polling()
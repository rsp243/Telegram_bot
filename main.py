import telebot, requests
from telebot import types
import os

quest = requests.get(os.environ['jsonToQuest']).json()
ans = requests.get(os.environ['jsonToAns']).json()

bot = telebot.TeleBot(os.environ['token'])


def formMarkup(id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = list()
    for i in quest[id]['answers']:
        for j in range(len(ans)):
            if i == ans[j]['id']:
                item = types.KeyboardButton(ans[j]['text'])
        a.append(i)
        markup.add(item)
    return markup


def sendMessage(id, message):
    keyboard = formMarkup(id)
    if id == quest[i]['id']:
        if quest[i]["message_before_question"] != '':
            bot.send_message(message.chat.id, f'{quest[i]["message_before_question"]}')
        bot.reply_to(message, f'{quest[i]["text"]}', reply_markup=keyboard)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    id = 0
    sendMessage(id, message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        if message.chat.type == 'private':
            for i in range(len(ans)):
                if ans[i]['text'] == message.text:
                    sendMessage(ans[i]['goto'] - 1, message)
    except:
        bot.send_message(message.chat.id, 'Диалог дальше ещё не сформирован, администраторы уже работают над этим, обратитесь через почту к создателю этого бота -> reshetov.semjon@gmail.com')


bot.polling()

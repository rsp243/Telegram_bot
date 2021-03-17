import telebot, requests
from telebot import types
import os


quest = requests.get(os.environ['jsonToQuest']).json()
ans = requests.get(os.environ['jsonToAns']).json()

bot = telebot.TeleBot(os.environ['token'])

def uploadInfo():
    global quest
    global ans
    quest = requests.get(os.environ['jsonToQuest']).json()
    ans = requests.get(os.environ['jsonToAns']).json()


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
    uploadInfo()
    sendMessage(1, message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.type == 'private':
        for i in range(len(ans)):
            if ans[i]['text'] == message.text:
                sendMessage(ans[i]['goto'], message)
        if message.text == 'В самое начало':
            uploadInfo()
            sendMessage(1, message)



bot.polling()

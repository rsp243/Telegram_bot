import telebot, requests, json
bot = telebot.TeleBot('926414545:AAH8KbWEVavTkXQAtHgyJk7U9zDSce0jiXk')
vopros=sorted(requests.get('https://app-name112.herokuapp.com/api/v1/questions/').json(), key=lambda s: s['id'])
otvet=sorted(requests.get('https://app-name112.herokuapp.com/api/v1/answers/').json(), key=lambda s: s['id'])
def keyboardhz(spisok):
    keyboardh = telebot.types.ReplyKeyboardMarkup()
    col = ['positive', 'primary', 'secondary']
    for i in range(len(spisok)):
        keyboardh.row(spisok[i])
    return keyboardh
def lydexanswers(o):
    for i in otvet:
        if i['text'] == o:
            return i['goto']
    return False
def lq(ide):
    for i in vopros:
        if i['id'] == ide+1:
            return i
    return False
def lydexanswerin(ide):
    for i in otvet:
        if i['id'] == ide:
            return i
    return False
@bot.message_handler(commands=['start'])
def start_message(message):
    if vopros[0]['message_before_question']:
        bot.send_message(message.from_user.id, vopros[0]['message_before_question'])
    if vopros[0] and vopros[0]['answers']:
        print(0)
        bot.send_message(message.from_user.id, vopros[0]['text'], reply_markup=keyboardhz([lydexanswerin(v)['text'] for v in vopros[0]['answers']]))
    elif vopros[0]:
        bot.send_message(message.from_user.id, vopros[0]['text'])
@bot.message_handler(content_types=['text'])
def send_text(textmessage):
    if lydexanswers(textmessage.text):
        if textmessage.text == ':baseupdate:':
            vopros=sorted(requests.get('https://app-name112.herokuapp.com/api/v1/questions/').json(), key=lambda s: s['id'])
            otvet=sorted(requests.get('https://app-name112.herokuapp.com/api/v1/answers/').json(), key=lambda s: s['id'])
            bot.send_message(textmessage.from_user.id, 'Базы обновлены.')
        if lq(lydexanswers(textmessage.text) - 1) and lq(lydexanswers(textmessage.text) - 1)['message_before_question']:
            bot.send_message(textmessage.from_user.id, lq(lydexanswers(textmessage.text) - 1)['message_before_question'])
        if lq(lydexanswers(textmessage.text) - 1) and lq(lydexanswers(textmessage.text) - 1)['answers']:
            bot.send_message(textmessage.from_user.id, lq(lydexanswers(textmessage.text) - 1)['text'], reply_markup=keyboardhz([lydexanswerin(v)['text'] for v in lq(lydexanswers(textmessage.text)-1)['answers']]))
        elif lq(lydexanswers(textmessage.text) - 1):
            bot.send_message(textmessage.from_user.id, lq(lydexanswers(textmessage.text) - 1)['text'])
bot.polling(none_stop=True)
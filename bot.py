import telebot

bot = telebot.TeleBot('7286433121:AAHx6dO74hzXZv8-EXsDzdrMehHjWj3u358');
name = ''
surname = ''
age = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '+':
        bot.send_message(message.from_user.id, "Привет, я ring_oleg_bot. А как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши "+", чтобы начать беседу')


def get_name(message):
    global name
    name = message.text
    if name.count(" ") == 0:
        bot.send_message(message.from_user.id, f'Какая у тебя фамилия, {name}?')
        bot.register_next_step_handler(message, get_surname)
    else:
        bot.send_message(message.from_user.id, 'Одним словом, пожалуйста')
        bot.register_next_step_handler(message, get_name)


def get_surname(message):
    global surname
    surname = message.text
    if surname.count(" ") == 0:
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, 'Одним словом, пожалуйста')
        bot.register_next_step_handler(message, get_surname)


def get_age(message):
    global age
    age = message.text
    if age.isnumeric():
        bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут '+name+' '+surname+'.\nЭто всё, что я умею на данный момент:)')
    else:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_age)


bot.polling(none_stop=False, interval=0)

from telebot import types
import telebot
from gamelogic import logic as gmlck
from work_with_db import changes as db_chng
from work_with_db import creates as db_crt
from work_with_db import requests as db_req
from data import db_session

# в settings/token.txt храним токен в settings/admin.txt - id админа (админов)
token = open('settings/token.txt').readline().split()[0]
bot = telebot.TeleBot(token)  # инит
admins = open('settings/admin.txt').read().split() # админы
db_session.global_init('db/base.db')


@bot.message_handler(commands=['start', 'help'])  # старт
def send_welcome(message):
    usr_id = str(message.from_user.id)  # userid
    usr_name = str(message.from_user.first_name)  # имя юзера
    keyboard = types.ReplyKeyboardMarkup(True)  # генерируем клаву
    button_play = types.KeyboardButton(text='Поиграть')
    keyboard.add(button_play)
    bot.reply_to(message, "Привет, " + str(message.from_user.first_name) + '\n' + "Давай поиграем в Вордли? Я загадаю слово из пяти букв, а ты попробуешь отгадать", reply_markup=keyboard)  # здороваемся

@bot.message_handler(commands=['play'])
@bot.message_handler(regexp="Поиграть")
def find(message):
    usr_id = str(message.from_user.id)
    word = gmlck.getword()
    if (db_req.req_user(usr_id)):
        print('Уже есть')
    else:
        db_crt.create_user(usr_id)
        db_chng.change_status(usr_id, True)
        db_chng.change_attempts(usr_id, 0)
        db_chng.change_word(usr_id, word)
        print('Успех')

    bot.reply_to(message, 'Я загадал, угадывай')
    if usr_id in admins:
        bot.reply_to(message, str(word))
    # bot.register_next_step_handler(message, result_back)
    # 


# если сообщение не распознано
@bot.message_handler(func=lambda message: True)
def answer(message):
    usr_id = str(message.from_user.id)
    # проверка, есть ли юзер в базе
    


if __name__ == '__main__':
    bot.infinity_polling()

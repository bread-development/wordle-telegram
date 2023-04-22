from telebot import types
import telebot
from gamelogic import logic as gmlck

# в settings/token.txt храним токен и id админа через enter
token = open('settings/token.txt').readline().split()[0]
bot = telebot.TeleBot(token)  # инит
admins = open('settings/token.txt').read().split() # админ


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
    bot.reply_to(message, 'Я загадал, угадывай')
    usr_id = str(message.from_user.id)
    word = gmlck.getword()
    if usr_id in admins:
        bot.reply_to(message, str(word))
    print(usr_id, admins)
    # bot.register_next_step_handler(message, result_back)
    # 


# если сообщение не распознано
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я тебя не понял, попробуй что-нибудь другое")


if __name__ == '__main__':
    bot.infinity_polling()

from random import choice
import json

def getword():
    with open("dict/dict.json", "r") as read_file:
        game_dict = json.load(read_file)
    word = choice(game_dict)
    return word

def checkword(input_word, attempts, is_win, target):
    with open("dict/dict.json", "r") as read_file:
        words = json.load(read_file)
    if len(input_word) == 5 and input_word in words:
        location = []
        for i in range(len(input_word)):
            letter = input_word[i]
            if letter in target and target[i] == input_word[i]:
                location.append(2)
            elif letter in target:
                location.append(1)
            else:
                location.append(0)
        attempts += 1
        if sum(location) == 10:
            return 'Победа', attempts, True
        if attempts == 6:
            return 'Поражение', attempts, False
        tries_left = '\nПопыток осталось: ' + str(6 - attempts) + '\n '
        return str(location)+tries_left, attempts, is_win
    elif len(input_word) != 5:
        return 'Введите слово из пяти букв\n', attempts, is_win

    elif input_word not in words:
        return 'Такого слова не существует\n', attempts, is_win

    
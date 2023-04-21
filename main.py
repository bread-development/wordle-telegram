import json

from random import choice

with open("dict/dict.json", "r") as write_file:
    words = json.load(write_file)

word = choice(words)
print(word)

end = False
attempts = 0

while not end:
    input_word = input()
    if len(input_word) == 5 and input_word in words:

        location = []

        for i in range(len(input_word)):
            letter = input_word[i]

            if letter in word and word[i] == input_word[i]:
                location.append(2)

            elif letter in word:
                location.append(1)

            else:
                location.append(0)

        print(location)

        if sum(location) == 10:
            end = True

        attempts += 1

        if attempts == 6:
            break

    elif len(input_word) != 5:
        print('Введите слово из пяти букв')

    elif input_word not in words:
        print('Такого слова не существует')

    print('Попыток осталось:', 6 - attempts)

if end:
    print('Победа!')
else:
    print('Поражение')

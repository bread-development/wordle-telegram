import json

normal_words = []

words = open('russian.txt', encoding='UTF-8').read().split()
for i in words[12:]:
    if len(i) == 5:
        normal_words.append(str(i).lower())

with open("data_file.json", "w") as write_file:
    json.dump(normal_words, write_file, ensure_ascii=False)

with open("data_file.json", "r") as write_file:
    words = json.load(write_file)
    print(words)

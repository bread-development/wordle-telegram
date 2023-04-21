from gamelogic import logic as gmlgc

word = gmlgc.getword()
print(word, '\n')
is_win = False
attempts = 0

while not is_win or attempts < 6:
    input_word = input().lower()
    to_print, attempts, is_win = gmlgc.checkword(input_word, attempts, is_win, word)
    print(to_print)
    if attempts >= 6 or is_win:
        break

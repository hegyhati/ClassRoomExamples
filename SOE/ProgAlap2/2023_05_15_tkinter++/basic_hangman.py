def display_word():
    for symbol in hidden_word:
        if symbol.lower() in guessed_symbols:
            print(symbol, end='')
        elif symbol == ' ':
            print(symbol, end=' ')
        else:
            print("_", end='')
    print()

def did_we_win():
    for symbol in hidden_word:
        if symbol.lower() not in guessed_symbols:
            return False
    return True


life = 5
hidden_word = "Julius Caesar"
guessed_symbols = []

while not did_we_win() and life > 0:
    new_symbol = input("Add meg a kovetkezo betut: ")
    guessed_symbols.append(new_symbol.lower())
    if new_symbol.lower() in hidden_word.lower():
        print("Van benne!")
    else:
        print("Nem talalt, -1 elet.")
        life -= 1
    display_word()

if life==0:
    print("GAME OVER")
else:
    print("CONGRATS!")
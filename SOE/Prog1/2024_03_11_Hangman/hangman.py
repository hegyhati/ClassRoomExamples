secret = "Norciusz Maximusz"
life = 5
previous = set()

def win_check():
    for char in secret:
        if char.lower() not in previous and char != " ":
            return False
    return True

def game_over():
    return life == 0

def input_new_guess():
    guess = input("Kovetkezo betu:").lower()
    while guess in previous or len(guess) != 1 or guess == " ":
        guess = input("Votma' vagy nem karakter vagy szokoz, adj masikat! ").lower()
    previous.add(guess)
    return guess

def print_clue():
    for char in secret:
        if char in previous or char.lower() in previous:
            print(" " + char, end="")
        elif char == " ":
            print("  ", end="")
        else:
            print(" _", end = "")
    print()
    
while not win_check() and not game_over():
    print_clue()
    guess = input_new_guess()
    if guess in secret.lower():
        print("Ugyi")
    else:
        print("Nem ugyi")
        life -= 1
        
if game_over():
    print("Game over")

if win_check():
    print("Yeppeeee")
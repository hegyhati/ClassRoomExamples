class Hangman:
    def __init__(self, hidden_word):
        self.hidden_word = hidden_word
        self.life = 5
        self.guessed_symbols = set()
    
    def win(self):
        for symbol in self.hidden_word:
            if symbol != ' ' and symbol.lower() not in self.guessed_symbols:    
                return False
        return True

    def dead(self):
        return self.life == 0

    def gameover(self):
        return self.win() or self.dead()

    def encoded_word(self):
        encoded = ""
        for symbol in self.hidden_word:
            if symbol.lower() in self.guessed_symbols or symbol == ' ':
                encoded = encoded + symbol
            else:
                encoded = encoded + "_"
        return encoded


    def print_status(self):
        print("Feladvany: ", self.encoded_word())
        print("Eletek szama:", self.life)
        print("Eddigi tippek:", ", ".join(sorted(self.guessed_symbols)))

    def get_new_symbol(self):
        while True:
            symbol = input("Adj meg egy karaktert: ").lower()
            if len(symbol) != 1 :
                print("Nem karaktert adtal meg!")
            elif symbol in self.guessed_symbols:
                print("Ezt mar tippelted, masikat adj meg!")
            else:
                break
        return symbol

    def handle_symbol(self, symbol):
        self.guessed_symbols.add(symbol)
        if symbol not in self.hidden_word.lower():
            self.life -= 1
            return False
        return True

    
    def run(self):
        while not self.gameover():
            self.print_status()
            symbol = self.get_new_symbol()
            if not self.handle_symbol(symbol):
                print("Nincs benne ez a karakter!")
        if self.win():
            print("Gratulalok, nyertel!")
        else:
            print("Sajnalom, vesztettel.")
        self.print_status()


if __name__ == "__main__":
    game = Hangman("Julius Caesar")
    game.run()
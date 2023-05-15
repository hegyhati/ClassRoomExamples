import tkinter as tk
from better_hangman import Hangman

class Game_State (tk.Frame):
    def __init__(self, model):
        super().__init__(highlightthickness=2, highlightbackground="black")
        self.model = model
        self.encoded_label = tk.Label(self, text=self.model.encoded_word())
        self.encoded_label.pack()
        self.life_label = tk.Label(self, text = "Eletek szama: 5")
        self.life_label.pack()
        self.guess_label = tk.Label(self, text = "Eddig nem tippeltel.")
        self.guess_label.pack()
    
    def update(self):
        self.encoded_label.configure(text = self.model.encoded_word())
        self.life_label.configure(text = f"Eletek szama: {self.model.life}")
        self.guess_label.configure(text = f"Tippek: {', '.join(self.model.guessed_symbols)}")

class Game_Input (tk.Frame):
    def __init__(self, model):
        super().__init__(highlightthickness=2, highlightbackground="red")
        self.symbol_entry = tk.Entry(self)
        self.symbol_entry.pack()
        self.symbol_entry.focus()

    def get_symbol(self):
        symbol = self.symbol_entry.get().lower()
        self.symbol_entry.delete(0,tk.END)
        return symbol

    


class Hangman_GUI (tk.Tk):
    def __init__(self, hidden_word):
        super().__init__()
        self.model = Hangman(hidden_word)
        self.state_frame = Game_State(self.model)
        self.state_frame.pack()
        self.input_frame = Game_Input(self.model)
        self.input_frame.pack()
        self.title("Hangman v1.0")
        self.bind("<Return>", self.handle_new_guess)
        self.message_label = tk.Label(self, text="Kezdj tippelni!")
        self.message_label.pack()

    def update_message(self, new_message):
        self.message_label.configure(text = new_message)

    def handle_new_guess(self, *args):
        symbol = self.input_frame.get_symbol()
        if len(symbol) != 1:
            self.update_message("Nem karaktert adtal meg!")
        elif symbol in self.model.guessed_symbols:
            self.update_message("Ezt mar tippelted, masikat adj meg!")
        else:
            if self.model.handle_symbol(symbol):
                self.update_message("Jo tipp!")
            else:
                self.update_message("Nincs benne ez a karakter!")
        self.update()

    def new_game(self):
        pass


    def update(self):
        self.state_frame.update()
        if self.model.gameover():
            if self.model.dead():
                self.update_message("Sajnalom, vesztettel.")
            if self.model.win():
                self.update_message("Gratulalok, nyertel!")
            self.input_frame.destroy()
            self.new_game_button = tk.Button(self, text = "Start new game", command = self.new_game)
            self.new_game_button.pack()



hangman_game = Hangman_GUI("ab")
hangman_game.mainloop()
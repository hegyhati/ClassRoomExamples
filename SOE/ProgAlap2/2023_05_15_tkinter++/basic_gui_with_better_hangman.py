import tkinter as tk
from better_hangman import Hangman

model = Hangman("Alma")

def handle_button(*args):
    symbol = symbol_entry.get().lower()
    if len(symbol) != 1:
        message_label.configure(text = "Nem karaktert adtal meg!")
    elif symbol in model.guessed_symbols:
        message_label.configure(text = "Ezt mar tippelted, masikat adj meg!")
    else:
        if model.handle_symbol(symbol):
            message_label.configure(text = "Jo tipp!")
        else:
            message_label.configure(text = "Nincs benne ez a karakter!")
    encoded_label.configure(text = model.encoded_word())
    symbol_entry.delete(0,tk.END)
    if model.gameover():
        if model.dead():
            message_label.configure(text = "Sajnalom, vesztettel.")
        if model.win():
            message_label.configure(text = "Gratulalok, nyertel!")
        symbol_entry["state"] = "disabled"
        guess_button["state"] = "disabled"

window = tk.Tk()
window.title("Hangman v0.1")
encoded_label = tk.Label(window, text=model.encoded_word())
encoded_label.pack()
symbol_entry = tk.Entry(window)
symbol_entry.pack()
symbol_entry.focus()
window.bind("<Return>", handle_button)
guess_button = tk.Button(window, text="Tippelek", command=handle_button)
guess_button.pack()
message_label = tk.Label(window, text="Kezdj tippelni!")
message_label.pack()

window.mainloop()
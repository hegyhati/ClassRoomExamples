from tkinter import *
from logic import Deck
from view import DeckFrame, TestUIFrame



def push(value):
    try:
        deck.push(value)
        card_frame.push_card(value)
        ui_frame.update_message("OK")
    except ValueError:
        ui_frame.update_message("Not OK")

deck = Deck([1,2,3,4,3],3)

window = Tk()
card_frame = DeckFrame(window, deck)
card_frame.pack(side=LEFT)
ui_frame = TestUIFrame(window, push)
ui_frame.pack(side=LEFT)

window.mainloop()
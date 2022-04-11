from tkinter import Button, Entry, Frame, Label


class DeckFrame(Frame):
    def __init__(self, master, deck) -> None:
        super().__init__(master)
        self.model = deck
        self.__init_ui()

    def __init_ui(self):
        for idx,card in enumerate(self.model.cards):
            Button(self,text="" if idx < self.model.hidden else f"{card}").pack()

    def push_card(self, value):
        Button(self, text=f"{value}").pack()

from functools import partial
class TestUIFrame(Frame):
    def __init__(self, master, push_function) -> None:
        super().__init__(master)
        self.push_function = push_function
        self.__init_ui()
    
    def __init_ui(self):
        self.new_card = Entry(self)
        self.new_card.pack()
        Button(self,text='push', command=self.handle_button_push).pack()
        self.message = Label(self,text="")
        self.message.pack()
    
    def update_message(self, message):
        self.message.config(text=message)
    
    def handle_button_push(self):
        value=int(self.new_card.get())
        self.push_function(value)
from functools import partial
from tkinter import *
# import tkinter as tk



window = Tk()
window.title("My awesome GUI app")

number = Label(window,text="", bg="blue", font=("Arial",40))
number.pack()

numpad = Frame(window)
numpad.pack()

def button_click(digit):
    number.config(text=number['text']+str(digit))


for digit in range(1,10):
    Button(numpad,text=str(digit), command = partial(button_click,digit)).grid(column=(digit-1)%3, row=(digit-1)//3)
Button(numpad,text="0", command = lambda: button_click(0)).grid(column=1, row=3)

def set_by_entry_field():
    number.config(text = user_input.get())

user_input = Entry(window)
user_input.pack()
Button(window,text="SET",command=set_by_entry_field).pack()

window.mainloop()


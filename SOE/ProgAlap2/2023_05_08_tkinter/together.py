from tkinter import *

window = Tk()
window.title("sum of two numbers")

def calculate():
    result.config(text = int(num1.get())+int(num2.get()))

num1 = Entry(window, justify="right")
num1.grid(column=1, row=0)

num2 = Entry(window, justify="right")
num2.grid(column=1, row=1)

Label(window,text="+").grid(column=0, row=1)

result = Label(window, bg="yellow", anchor="e")
result.grid(column=1, row=3, sticky="we", padx=5, pady=5)

Button(window,text="=",command=calculate).grid(column=0, row=3)

Frame(window,bg="black", height=2).grid(columnspan=2, column=0, row=2, sticky="nesw")





window.mainloop()

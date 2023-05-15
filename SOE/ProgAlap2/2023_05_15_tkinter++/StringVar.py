import tkinter as tk

def click():    
    mybutton.configure(text = inputfield.get())
    mylabel.configure(text = inputfield.get())



window = tk.Tk()

myvar = tk.StringVar()
myvar.set(3)

inputfield = tk.Entry(window, textvariable = myvar)
inputfield.pack()
mybutton = tk.Button(window, textvariable=myvar, command=click)
mybutton.pack()
mylabel = tk.Label(window, text="Click me")
mylabel.pack()

window.mainloop()
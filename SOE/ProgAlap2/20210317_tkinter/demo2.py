from tkinter import *

window=Tk()

for r in range(1,8):
    for c in range(1,8):
        if r%c == 0:
            Label(window,text="({},{})".format(r,c),bg="gray").grid(row=r, column=c, padx=5, pady=5)

window.mainloop()

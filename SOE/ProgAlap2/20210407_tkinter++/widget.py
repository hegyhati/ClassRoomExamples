from tkinter import *
from tkinter.ttk import *
from functools import partial


window = Tk()

"""
def foo():
    print(f"foo {checkbuttonstate.get()}")

checkbuttonstate = StringVar()
checkbuttonstate.set("foo")

checkbutton = Checkbutton(window, text = "izebize", command=foo, variable=checkbuttonstate, onvalue="checked", offvalue="unchecked")

Button(window,textvariable=checkbuttonstate).pack()

checkbutton.pack()
"""

"""
Label(window,text="Valassz szint").pack()
rbvalue=StringVar()
rbvalue.set("piros")
Radiobutton(window,text="Piros", variable=rbvalue,value="piros").pack()
Radiobutton(window,text="Kek", variable=rbvalue,value="kek").pack()
Radiobutton(window,text="Zold", variable=rbvalue,value="zold").pack()
Label(window,text="Valassz meretet").pack()
rbvalue2=StringVar()
rbvalue2.set("M")
Radiobutton(window,text="Medium", variable=rbvalue2,value="M").pack()
Radiobutton(window,text="Large", variable=rbvalue2,value="L").pack()
Radiobutton(window,text="Extra large", variable=rbvalue2,value="XL").pack()
"""

"""
ize=StringVar()
cb=Combobox(window,textvariable=ize,values=["1","ketto","three"])
cb.state(["readonly"])
cb.pack()
"""

"""

def isnumber(text:str) -> bool:
    for c in text:
        if c not in "0123456789":
            return False
    return True
isnumber_wrapper = (window.register(isnumber), '%P') # TODO



ize=StringVar()
ize.set("123")
entry=Entry(window,textvariable=ize,validate='key',validatecommand=isnumber_wrapper)
entry.pack()
"""


names = ["Andi","Bela","Cili","Dani","Elek","Feri","Geza","Hedvig","Ili","Jani"]


def open_new_window(parent):
    global names
    name = names[0]
    names = names[1:]
    new_window = Toplevel(parent)
    new_window.title(f"{name} son of {parent.mytitle}")
    new_window.mytitle=f"{name} son of {parent.mytitle}"
    Button(new_window, text=f"En a {name} vagyok, es a {parent.mytitle} a szulom", command=partial(open_new_window,new_window)).pack()


window.title("Main window")
window.mytitle="Main window"


Button(window, text="show me a new window", command=partial(open_new_window,window)).pack()

window.mainloop()

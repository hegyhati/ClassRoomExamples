from functools import partial
from tkinter import *
from Bottles import BottleSystem


sizes = input("Bottles?")
sizes = [ int(size) for size in sizes.split(",") ]

model = BottleSystem(sizes)

style = {
    "font" : ("Arial", 34)
}

def update_levels():
    global level_labels
    global model
    for idx in range(model.size):
        level_labels[idx].config(text=str(model.get_level(idx)))

w = Tk()
level_labels = [Label(w,text="X", **style) for _ in range(model.size)]


for idx in range(model.size):
    level_labels[idx].grid(column=idx,row=0)
for idx,max in enumerate(model.get_max()):
    Label(w,text=f"{max}", **style).grid(column=idx, row=1)
update_levels()

def controller(func,**kwargs):
    global model
    func(**kwargs)
    update_levels()
    # vagy dekorator

def fill_controller(idx:int):
    global model
    model.fill(idx)
    update_levels()

def empty_controller(idx:int):
    global model
    model.empty(idx)
    update_levels()

def pour_controller(source:int, sink:int):
    global model
    model.pour(source, sink)
    update_levels()

for idx in range(model.size):
    Button(w,text="FILL",command=partial(fill_controller, idx)).grid(column=idx,row=2)
for idx in range(model.size):
    Button(w,text="EMPTY",command=partial(controller, model.empty, idx=idx)).grid(column=idx,row=3)



w.mainloop()
from functools import partial
from tkinter import Tk,Frame,font,Label,Button, Misc
from Bottles import BottleSystem





class Bottle_Frame(Frame):
    def __init__(self, model:BottleSystem, master: Misc | None = None) -> None:
        super().__init__(master)
        self.__model=model
        self.__setup_ui()
    
    def update(self):
        for idx in range(self.__model.size):
            self.__level_labels[idx].config(text=str(self.__model.get_level(idx)))
        super().update()

    def __setup_ui(self):
        self.__level_labels = [Label(self,text="X") for _ in range(self.__model.size)]
        for idx in range(self.__model.size):
            self.__level_labels[idx].grid(column=idx,row=0)
        for idx,max in enumerate(self.__model.get_max()):
            Label(self,text=f"{max}").grid(column=idx, row=1)        
        for idx in range(self.__model.size):
            Button(self,text="FILL",command=partial(self.controller, self.__model.fill, idx=idx)).grid(column=idx,row=2)
        for idx in range(model.size):
            Button(self,text="EMPTY",command=partial(self.controller, self.__model.empty, idx=idx)).grid(column=idx,row=3)
        self.update()   

    def controller(self, func,**kwargs): # kulon osztalyba illene
        func(**kwargs)
        self.update()



sizes = input("Bottle sizes? ")
sizes = [ int(size) for size in sizes.split(",") ]

model = BottleSystem(sizes)

w = Tk()
font.nametofont("TkDefaultFont").configure(size=32)
Bottle_Frame(model,w).pack()
w.mainloop()
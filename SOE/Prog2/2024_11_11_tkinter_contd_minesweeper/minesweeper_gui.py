from tkinter import Misc, Tk, Frame, Button, Label, FLAT, RAISED, DISABLED, NORMAL, BOTH, TOP, BOTTOM
from minesweeper_model import MineSweeper
from functools import partial




class Field(Button): 

    def __init__(self, master, model:MineSweeper, row:int, col:int, **kargs):
        super().__init__(master, width=2, height=2 , **kargs)
        self.__row:int = row
        self.__col:int = col
        self.__model:MineSweeper = model
        self.config(command=self.__click)
        self.grid(row=row, column=col)
    
    def __click(self) -> None:
        self.__model.uncover(self.__row, self.__col)
        self.master.update_view()  
    
    def update_view(self) -> None:
        uncovered = self.__model.is_uncovered(self.__row, self.__col)
        is_bomb = self.__model._is_bomb(self.__row, self.__col)
        bomb_count = self.__model.neighbor_bomb_count(self.__row, self.__col)

        if uncovered:
            self.config(relief=FLAT, state=DISABLED)
            if not is_bomb and bomb_count != 0 : self.config(text=bomb_count)

        if self.__model.is_game_over() or self.__model.is_won():
            self.config(state=DISABLED)
            if is_bomb:
                self.config(background="red" if self.__model.is_game_over() else "green" )



class MineFieldFrame(Frame):
    def __init__(self, master, model:MineSweeper, **kargs):
        super().__init__(master, **kargs)
        self.__model:MineSweeper = model


        self.__fields = [ 
            Field(self, model, r, c)
            for r in range(model.height())
            for c in range(model.width())
        ]
    
    def update_view(self):
        self.master.update_message()
        for field in self.__fields:
            field.update_view()      

class MineSweeperGUI(Tk):

    def __init__(self, width:int, height:int, bombcount:int):
        super().__init__()
        self.title("Tk Minesweeper")
        self.__width:int = width
        self.__height:int = height
        self.__bombcount:int = bombcount
        self.__status_message:Label = Label(self)
        self.__status_message.pack(side=TOP, fill=BOTH)
        self.__field_frame:MineFieldFrame|None = None
        Button(self,text="RESET",command=self.reset).pack(side=BOTTOM, fill=BOTH)
        self.reset()


    def reset(self) -> None:
        self.__status_message.config(text="Let the sweepin' begin!")
        self.__model = MineSweeper(self.__width, self.__height, self.__bombcount)
        if self.__field_frame is not None:
            self.__field_frame.destroy()
        self.__field_frame = MineFieldFrame(self,self.__model)
        self.__field_frame.pack()
        

    def update_message(self):
        if self.__model.is_won():
            self.__status_message.config(text="Congrats! You won!")
        elif self.__model.is_game_over():
            self.__status_message.config(text="Sotty, you have lost.")
        else:
            self.__status_message.config(text="Keep sweepin'")







gui = MineSweeperGUI(5,5,4)
gui.mainloop()


from functools import partial
from tkinter import Tk, Frame, Button, Entry, Label
from Cell import *

class GreetingFrame(Frame):

    def __init__(self, master, *args, **kargs):
        super().__init__(master, *args, **kargs)
        newButton = Button(self, text="New", command=self.new_spreadsheet)
        file = Entry(self)
        openButton = Button(self, text="Open", command=self.open_spreadsheet)
        newButton.pack()
        file.pack()
        openButton.pack()

    def new_spreadsheet(self):
        sheet = Sheet(5,5)
        self.master.show_spreadsheet(sheet)

    def open_spreadsheet(self):
        sheet = None # load sheet from file
        self.master.show_spreadsheet(sheet)

class FileSaveFrame(Frame):
    def __init__(self, master):
        super().__init__(master, border = 10, highlightcolor = "black", relief = "solid")
        self.filename = Entry(self)
        self.savebutton = Button(self, text="SAVE")
        self.filename.pack(side="left", fill="x")
        self.savebutton.pack(side="left")

class CellEditor(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.cellcontent = Entry(self)
        self.updatebutton = Button(self, text="OK")
        self.cellcontent.pack(side="left", fill="x")
        self.updatebutton.pack(side="left")

class SpreadSheetFrame(Frame):
    def __init__(self, master, sheet_data):
        super().__init__(master)
        self.__sheet = sheet_data
        self._row_count = sheet_data.row_count()
        self._column_count = sheet_data.column_count()
        colums = [chr(c) for c in range(ord("A"), ord("A")+self._column_count)]
        for cidx,col in enumerate(colums):
            Label(self,text=col).grid(row=0, column=cidx+1)
        for row in range(1,1+self._row_count):
            Label(self,text=str(row)).grid(column=0, row=row)
        self.__cells = [
            [ Entry(self) for c in range(self._column_count) ]
            for r in range(self._row_count)
        ]
        for r in range(self._row_count):
            for c in range(self._column_count):
                self.__cells[r][c].grid(row=r+1, column=c+1)
                self.__cells[r][c].bind("<Return>", partial(self.cell_edited, row=r, column=c))
                self.__cells[r][c].bind("<FocusOut>", partial(self.revert_cell, row=r, column=c))
                self.__cells[r][c].bind("<Button-1>", partial(self.master._update, row=r, column=c))
                self.__cells[r][c].bind("<FocusIn>", partial(self.master._update, row=r, column=c))
        self.__update()
    
    def __update(self):
        for r in range(self._row_count):
            for c in range(self._column_count):
                self.__cells[r][c].delete(0,"end")
                self.__cells[r][c].insert(0, str(self.__sheet.get_cell(r,c)))
    
    def revert_cell(self, event=None, row=0, column=0):
        self.__cells[row][column].delete(0,"end")        
        self.__cells[row][column].insert(0, str(self.__sheet.get_cell(row,column)))

    
    def cell_edited(self, event=None, row=0, column=0):
        new_text = self.__cells[row][column].get()
        print(f"Cell {row} {column} edited to {new_text}")
        self.__sheet.set_cell(row, column, self.__sheet.cell_factory(new_text))
        print(self.__sheet.get_cell(row,column).__class__)
        self.__update()




class SpreadSheetEditorFrame(Frame):
    def __init__(self, master, sheet_data):
        super().__init__(master)
        self.__sheet = sheet_data
        FileSaveFrame(self).pack(fill="x")
        self.cef = CellEditor(self)
        self.cef.pack(fill="x")
        SpreadSheetFrame(self, sheet_data).pack()
    
    def _update(self, event=None, row=0, column=0):
        self.cef.cellcontent.delete(0,"end")
        cell = self.__sheet.get_cell(row, column)
        if cell.is_formula():
            data = cell.get_formula()
        else:
            data = str(cell)
        self.cef.cellcontent.insert(0,data)



class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Awesome Excel alternative")
        self.minsize(width=500, height=500)
        self.greeting = GreetingFrame(self, border = 10, highlightcolor = "black", relief = "solid")
        self.greeting.pack()    
    
    def show_spreadsheet(self, sheet_data):
        self.greeting.destroy()
        SpreadSheetEditorFrame(self, sheet_data).pack()



MainWindow().mainloop()

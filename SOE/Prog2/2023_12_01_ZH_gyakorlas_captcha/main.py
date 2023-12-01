from io import BytesIO
from random import choice, randint, shuffle
from threading import Thread
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests


class MaciButton(tk.Button):
    api_url = "http://127.0.0.1:5000"
    def __init__(self, master, maci:bool):
        self.image = ImageTk.PhotoImage(Image.open("hourglass.png").resize((100, 100)))
        super().__init__(master,      
                image=self.image,
                height = 100, width = 100, bd=10,
                command=self.press,
                relief=tk.RIDGE
                )
        self.ready = False
        self.maci = maci
        if self.maci:
            self.animal = "bear"
        else:
            other_animals = requests.get(f"{self.api_url}/animals").json()
            other_animals.remove("bear")
            self.animal = choice(other_animals)

        Thread(target=self.download_image).start()

        
    def download_image(self):        
        self.image = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(f"{self.api_url}/random/{self.animal}").content)).resize((100, 100)))
        self.configure(image=self.image)
        self.configure(relief=tk.RAISED)
        self.ready = True
        
    def press(self):
        if self.cget("relief") == tk.RIDGE:
            return
        elif self.cget("relief") == tk.SUNKEN:
            self.configure(relief=tk.RAISED)
        else:
            self.configure(relief=tk.SUNKEN)
    
    def is_checked(self):
        return self.cget("relief") == tk.SUNKEN
    
    def is_maci(self):
        return self.maci
    
    def is_good(self):
        return self.is_checked() == self.is_maci() and self.ready



class MaciFrame(tk.Frame):
    SIZE = 5
    def __init__(self, master):
        super().__init__(master)
        macicount = randint(self.SIZE**2//4, self.SIZE**2//2)
        self.options = [MaciButton(self, True if i < macicount else False ) for i in range(self.SIZE**2)]
        shuffle(self.options)
        for idx,option in enumerate(self.options):
            option.grid(row=idx//self.SIZE, column=idx%self.SIZE,padx=10, pady=10)

    def get_state(self):
        return [option.is_checked() for option in self.options]
    
    def is_good(self):
        for option in self.options:
            if not option.is_good():
                return False
        return True # all

def check():
    if maciframe.is_good():
        window.destroy()
    else:
        print("Rossz válasz")

window = tk.Tk()
font.nametofont("TkDefaultFont").configure(size=32)
window.title("Macis captcha")
tk.Label(window, text="Kattints a macikra").pack()
maciframe = MaciFrame(window)
maciframe.pack()
tk.Button(window, text="OK", command=check).pack(fill=tk.X)
window.mainloop()

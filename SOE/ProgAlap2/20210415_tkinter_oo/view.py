import tkinter as tk
from model import Character, Map
from functools import partial

class MapFrame(tk.Frame):

  def __init__(self, master, map:Map, character:Character):
    super().__init__(master)
    self.images = {
      Map._wall : tk.PhotoImage(file="brick.gif"),
      Map._free : tk.PhotoImage(file="grass.gif"),
      Map._void : tk.PhotoImage(file="void.gif"),
      "alive" : tk.PhotoImage(file="warrior.gif")
    }
    self.map=map
    self.character=character
    self.initialize_map()
    self.update_map()

  def initialize_map(self):
    self.labels=[]
    for y in range(self.character.vision*2+1):
      self.labels.append([])
      for x in range(self.character.vision*2+1):
        label = tk.Label(self,image=self.images[Map._void], bd = 0)
        label.grid(row=y, column=x)
        self.labels[-1].append(label)


  def update_map(self):
    observable_map=self.map.observable_part(self.character)
    for y in range(self.character.vision*2+1):
      for x in range(self.character.vision*2+1):
        if x==self.character.vision and y == self.character.vision:
          self.labels[x][y].configure(image=self.images["alive"])
        else:  
          self.labels[x][y].configure(image=self.images[observable_map[x][y]])
  
  def _game_over(self):
    self.labels[self.character.vision][self.character.vision].configure(text="D",bg="red")


    


class GameView(tk.Tk):
  
  def __init__(self,map:Map,character:Character):
    super().__init__() 
    self.map=map
    self.character=character
    self.title("Super RPG Game")

    self.up_button = tk.Button(self, text="↑", command=partial(self.move,"up"))
    self.down_button = tk.Button(self, text="↓", command=partial(self.move,"down"))
    self.left_button = tk.Button(self, text="←", command=partial(self.move,"left"))
    self.right_button = tk.Button(self, text="→", command=partial(self.move,"right"))
    self.buttons=[self.up_button, self.down_button, self.left_button, self.right_button]
    for button in self.buttons:
      button.configure(state=tk.DISABLED, bg="blue", font=('Courier', 36))
    

    self.up_button.grid(row=0, column=1, sticky="we")
    self.down_button.grid(row=2, column=1, sticky="we")
    self.left_button.grid(row=1, column=0, sticky="ns")
    self.right_button.grid(row=1, column=2, sticky="ns")

    tk.Button(self,text="START",command=self.start_game).grid(row=1,column=1)
  
  def start_game(self):
    self.map_frame=MapFrame(self,self.map,self.character)
    self.map_frame.grid(row=1,column=1)
    for button in self.buttons:
      button.configure(state=tk.NORMAL)

  def __game_over(self):
    for button in self.buttons:
      button.configure(state=tk.DISABLED, bg="red")
    self.map_frame._game_over()
    
  def move(self,direction:str):
    if self.map.move(self.character,direction):
      self.map_frame.update_map()
      if self.map.stepped_on_mine(self.character):
        self.__game_over()

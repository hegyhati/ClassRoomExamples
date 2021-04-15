import json

class Character:

  def __init__(self, filename:str):
    with open(filename) as file:
      data=json.load(file)
      self.x=data["position"]["x"]
      self.y=data["position"]["y"]
      self.name=data["name"]
      self.vision=data["vision"]

class Map:
  _wall = "█"
  _free = "░"
  _void = " "


  def __init__(self,filename:str):
    self.mines=[]
    self.map=[]
    with open(filename) as file:
      data=json.load(file)
      self.map = data["map"]
      for mine in data["landmines"]:
        self.mines.append((mine["x"],mine["y"]))
  
  def stepped_on_mine(self, character:Character) -> bool:
    return (character.x,character.y) in self.mines

  def move(self,character:Character,direction:str) -> bool:
    x2=character.x
    y2=character.y
    if direction=="up":    y2-=1
    if direction=="down":  y2+=1
    if direction=="left":  x2-=1
    if direction=="right": x2+=1
    if self.map[y2][x2]==Map._free:
        character.x = x2
        character.y = y2
        return True
    else:
        return False

  def observable_part(self,character) -> list:
    height=len(self.map)
    width=len(self.map[0])
    observable_map=[]
    for y in range(character.y-character.vision,character.y+character.vision+1):
      observable_map.append([])
      if y < 0 or y >= height:
        for _ in range (2*character.vision+1):
          observable_map[-1].append(Map._void)
      else:
        for x in range(character.x-character.vision,character.x+character.vision+1):
          if x < 0 or x >= width:
            observable_map[-1].append(Map._void)
          else:
            observable_map[-1].append(self.map[y][x])
    return observable_map

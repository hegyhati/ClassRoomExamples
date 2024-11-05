from tetramino import Tetramino
from colors import colors
import json

class Board:

    def __init__(self, filename:str = "map.txt") -> None:
        self.__map = [ [0] * 7 for _ in range(7) ]
        with open(filename) as f:
            y = 7
            for line in f:
                y-=1
                for x,c in enumerate(line):
                    if c == "#":
                        self.__map[x][y] = -1
        input(self.__map)

        
        with open("tetraminos.json") as f:
            self.__in_hand = [
                Tetramino(tetramino, id+1)
                for id,tetramino in enumerate(json.load(f))
            ]
        for tetramino in self.__in_hand:
            tetramino.normalize()
        
        self.__in_hand = self.__in_hand[:8]
    
    def place_tetramino(self, tetramino:Tetramino) -> bool:
        for x,y in tetramino.get_positions():
            if self.__map[x][y] != 0:
                return False
            self.__map[x][y] = tetramino.get_id()
        return True
        

    def pop_tetramino(self):
        return self.__in_hand.pop(0)
    
    def finished(self) -> bool:
        return len(self.__in_hand) == 0
    
    def save_to_svg(self, filename:str) -> None:
        with open(filename, "w") as f:
            SIZE = 100
            f.write(f"<svg width=\"{SIZE * 7}\" height=\"{SIZE * 7}\">\n")
            #f.write(f"<group transform=\"translate(0,700) scale(1,-1)\">")
            for x in range(7):
                for y in range(7):
                    f.write(f'''<rect width="{SIZE}" height="{SIZE}" x="{SIZE*x}" y="{SIZE*y}" fill="{colors[self.__map[x][y]] if self.__map[x][y] >=0 else 'black'}" />''')
            #f.write(f"</group>")
            f.write(f"</svg>")

        
    



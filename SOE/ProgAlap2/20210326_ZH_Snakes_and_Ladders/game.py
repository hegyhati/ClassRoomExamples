from random import randint
import matplotlib.pyplot as plt

class Board:
    
    def __init__(self, size:int):
        self._jumps=[]
        self.size=size
        self.reset_statistics()

    def _valid_field(self,field:int) -> bool:
        return field <= self.size and field >=1
    
    def _free_field(self, field: int) -> bool:
        if not self._valid_field(field) or field==self.size: return False
        else:
            for jump in self._jumps:
                if jump[0]==field or jump[1] == field:
                    return False
            return True
    
    def add_jump(self, source:int, destination:int) -> bool:
        if not self._free_field(source) or not self._free_field(destination) or source==destination: return False
        else:
            self._jumps.append((source,destination))
            return True
    
    def reset_statistics(self):
        self._jump_count={}
        for jump in self._jumps:
            self._jump_count[jump]=0
    
    def move(self, position:int) -> int:
        position+=randint(1,6)     
        if position > self.size:
            position = self.size - (position - self.size)
        for jump in self._jumps:
            if jump[0]==position:
                position=jump[1]
                self._jump_count[jump] += 1
                break
        return position
    
    def draw_statistics(self, filename:str):
        fig,axes=plt.subplots()
        names=[]
        usages=[]
        for jump in self._jumps:
            names.append( "{} {}->{}".format("Snake" if jump[0] > jump[1] else "Ladder",jump[0],jump[1]))
            usages.append(self._jump_count[jump])
        axes.barh(names,usages)
        fig.savefig(filename,bbox_inches='tight')        


class Game:

    def __init__(self, board, max_rounds:int):
        self.max_rounds=max_rounds
        self.board = board
    
    def _initialize_positions(self, players:list) -> dict:
        positions={}
        for player in players:
            positions[player]=1
        return positions

    def simulate_game(self, players:list) -> str:
        positions = self._initialize_positions(players)
        for _ in range(self.max_rounds):
            for player in positions:
                positions[player]=self.board.move(positions[player])
                if positions[player] == self.board.size:
                    return player
        raise Exception("Maximal number of rounds reached")
    
from random import randrange, sample
from itertools import product

class MineSweeper:

    def __init__(self, width:int, height:int, bombcount:int) -> None:
        self.__uncovered = [ [False] * width  for _ in range(height) ]
        self.__bombs = set(sample(list(product(range(height),range(width))), k=bombcount))
        self.__game_over = False
    
    def is_uncovered(self, row:int, col:int) -> bool:
        return self.__uncovered[row][col]
    
    def _is_bomb(self, row:int, col:int) -> bool:
        return (row,col) in self.__bombs
    
    def uncover(self, row:int, col:int) -> None:
        if self.__game_over: return
        if self._is_bomb(row, col): 
            self.__game_over = True
        else: 
            self.__uncover_zero_region(row, col)

    def __neighbors(self, row:int, col:int) -> set[tuple[int,int]]:
        return {
            (r,c) 
            for r in (row-1,row,row+1) 
            for c in (col-1,col,col+1)
            if (r,c) != (row,col)
            if r >= 0 and r < self.height() and c >=0 and c < self.width()
        }
    
    def neighbor_bomb_count(self, row:int, col:int) -> int:
        return sum(1 for (r,c) in self.__neighbors(row,col) if self._is_bomb(r,c))
    
    def __uncover_zero_region(self, row:int, col:int) -> None:
        if self.__uncovered[row][col]: return
        self.__uncovered[row][col] = True
        if self.neighbor_bomb_count(row,col) == 0:
            for (r,c) in self.__neighbors(row, col):
                self.__uncover_zero_region(r,c)
    
    def is_won(self) -> bool:
        return not self.__game_over and sum(r.count(False) for r in self.__uncovered) == len(self.__bombs)
    
    def is_game_over(self) -> bool:
        return self.__game_over
    
    def height(self) -> int:
        return len(self.__uncovered)
    
    def width(self) -> int:
        return len(self.__uncovered[0])

    



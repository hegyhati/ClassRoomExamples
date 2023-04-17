import random
from typing import List

from matplotlib import pyplot as plt


class Board:

    def __init__(self, size) -> None:
        self._size = size
        self._jumps = []

    def _valid_field(self, field:int) -> bool:
        return field >= 1 and field <= self._size
    
    def _free_field(self, field:int) -> bool:
        if not self._valid_field(field): return False
        if field == self._size: return False
        for jump in self._jumps:
            if field in jump:
                return False
        return True

    def add_jump(self, from_field:int, to_field:int) -> bool:
        if not self._free_field(from_field) or not self._free_field(to_field): return False
        if from_field == to_field: return False 
        self._jumps.append( (from_field,to_field) )
        return True

    def __dice_roll_move(self, from_field:int) -> int:
        dice_roll = random.randint(1,6)
        destination = from_field + dice_roll
        if destination > self._size:
            dice_roll -= self._size - from_field
            destination = self._size - dice_roll
        return destination

    def _jump(self, field:int) -> int:
        for (jump_from, jump_to) in self._jumps:
            if field == jump_from:
                field = jump_to
                break
        return field


    def move(self, from_field:int) -> int:
        destination = self.__dice_roll_move(from_field)
        destination = self._jump(destination)
        return destination

class Board_with_Jump_statistics(Board):
    def __init__(self, size) -> None:
        super().__init__(size)
        self._statistics = {}
    
    def _jump(self, field:int) -> int:
        for jump in self._jumps:
            if field == jump[0]:
                field = jump[1]
                if jump in self._statistics:
                    self._statistics[jump] += 1
                else:
                    self._statistics[jump] = 1
                break
        return field

    def reset_statistics(self) -> None:
        self._statistics.clear()
    
    def draw_statistics(self, filename:str) -> None:
        print(self._statistics)
        fig, ax = plt.subplots()
        jumps = [f"Jump {jump}" for jump in self._statistics]
        counts = [self._statistics[jump] for jump in self._statistics]
        ax.barh(jumps, counts)
        fig.savefig(filename)


class Game:
    def __init__(self, board:Board, max_iteration:int) -> None:
        self._board = board
        self._max_iteration = max_iteration
        pass

    def simulate_game(self, players:List[str]) -> str:
        positions = {player: 1 for player in players}
        for _ in range(self._max_iteration):
            for player in players:
                positions[player] = self._board.move(positions[player])
                if positions[player] == self._board._size: return player
        raise Exception("Maximum iteration reached.")



board = Board_with_Jump_statistics(30)

print ("Valid jumps: "
    , board.add_jump(27,1)  # Green snek
    , board.add_jump(21,9)  # Blue snek
    , board.add_jump(19,7)  # Purple snek
    , board.add_jump(17,4)  # Green-orange snek
    , board.add_jump(3,22)  # One of the big ladders
    , board.add_jump(5,8)   # One of the small ladders
    , board.add_jump(11,26) # The other big ladder
    , board.add_jump(20,29) # The other small ladder
)

print ("Invlaid jumps: "
    , board.add_jump(27,1)  # Green snek again
    , board.add_jump(23,1)  # Tail overlaps with green snek
    , board.add_jump(6,30)  # Final field is not free
    , board.add_jump(0,10)  # Not a valid source field)
)

print( "Valid field:"
    , board._valid_field(1)  # True
    , board._valid_field(30) # True
    , board._valid_field(0)  # False
    , board._valid_field(42) # False
)

print( "Free field:"
    , board._free_field(0)    # False
    , board._free_field(2)    # True
    , board._free_field(30)   # False
    , board._free_field(42)   # False
)

players = ['Annie' , 'Betholdt', 'Reiner', 'Marcel']

impossible_game=Game(board,1)
print("Impossible game with 1 iteration: ", end='')
try:
    winner = impossible_game.simulate_game(players)
    print("The winner is",winner)
except Exception as e:
    print(e)

game=Game(board,40)
print("Normal game with 40 max iteration: ", end='')

try:
    winner = game.simulate_game(players)
    print("The winner is",winner)
except Exception as e:
    print(e)



board.reset_statistics()
for _ in range(9999):
    try:
        winner = game.simulate_game(players)
    except:
        pass
board.draw_statistics("9999_games.png")
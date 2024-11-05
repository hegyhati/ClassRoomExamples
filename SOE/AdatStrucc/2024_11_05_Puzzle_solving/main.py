from copy import deepcopy
from board import Board
from tetramino import Tetramino
from collections import deque

states_to_explore:deque[Board] = deque([Board()])

visited = 0
feasible = 0
tries = 0
solution = 0

while len(states_to_explore) != 0:
    visited += 1
    board = states_to_explore.pop()
    if board.finished():
        solution += 1
        print("Yeppeeee")
        board.save_to_svg(f"saves/{solution:09}.svg")
        continue
    tetramino = board.pop_tetramino()
    for m in [False,True]:
        for r in [0,1,2,3]:
            tetramino_copy = deepcopy(tetramino)
            if m: tetramino_copy.mirror()
            tetramino_copy.rotate(r)
            tetramino_copy.normalize()

            for dx in range(0,7-tetramino_copy.width()+1):
                for dy in range(0,7-tetramino_copy.height()+1):
                    tries += 1
                    board_copy = deepcopy(board)
                    tetramino_copy_copy = deepcopy(tetramino_copy)
                    tetramino_copy_copy.shift(dx,dy)
                    if board_copy.place_tetramino(tetramino_copy_copy):
                        feasible += 1
                        if feasible % 100 == 0:
                            print(f"tries: {tries:6} feasible:{feasible:6} explored:{visited:6} to explore: {len(states_to_explore):6}")
                        states_to_explore.append(board_copy)
            
        


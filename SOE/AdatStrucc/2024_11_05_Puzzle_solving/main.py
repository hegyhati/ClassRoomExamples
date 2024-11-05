from copy import deepcopy
from board import Board
from tetramino import Tetramino
from collections import deque
from sys import argv



# Load board and tetraminos
base_board:Board = Board("maps/nov5.txt")
tetraminos_to_place:list[Tetramino] = Tetramino.load_tetraminos_from_json("tetraminos/default.json")
tetramino_count = len(tetraminos_to_place)

# Precalculate all feasible placement of tetraminos and their variants considering FORBIDDEN squares
tetramino_placements = [
    [
        deepcopy(v).shift(dx,dy)
        for v in t.get_variants()
        for dx in range(base_board.width - v.width() + 1)
        for dy in range(base_board.height - v.height() + 1)
        if deepcopy(base_board).place_tetramino(deepcopy(v).shift(dx,dy))
    ]
    for t in tetraminos_to_place
]
for tidx,t in enumerate(tetraminos_to_place):
    print(f"{len(tetramino_placements[tidx])} feasible placement for {t} and its variants.")

# Sort tetraminos based on number of feasible variants to make top of the tree narrower:
tetramino_placements.sort(key = lambda x: len(x))



# Initialize search
tries = feasible = visited = solution = 0
states_to_explore:deque[Board] = deque([ (0,base_board) ])

report_interval = 10000 if len(argv) < 3 else int(argv[2])
if len(argv) < 2: exit("Provide BFS or DFS")
match argv[1]:
    case "BFS": 
        next_state = states_to_explore.popleft
        print_progress = False
        progress_text = ""
    case "DFS": 
        next_state = states_to_explore.pop
        progress_increase = 100 / len(tetramino_placements[0])
        progress = - progress_increase
        print_progress = True
    case _: exit("Provide BFS or DFS")



while len(states_to_explore) != 0:
    visited += 1
    next_tidx, board = next_state()


    #with open(f"tmp/{visited:09}.svg", "w") as f:
    #    f.write(board.to_svg())

    if next_tidx == 1 and print_progress:
        progress += progress_increase
        progress_text = f"{progress:5.2f} % "

    if next_tidx == tetramino_count:
        solution += 1
        with open(f"saves/nov5_default_{solution:09}.svg", "w") as f:
            f.write(board.to_svg())
        continue
    for tetramino in tetramino_placements[next_tidx]:        
        tries += 1
        if tries % report_interval == 0:
            print(f"{progress_text}Tries: {tries:9} feasible:{feasible:9} explored:{visited:9} solutions:{solution:2} to explore: {len(states_to_explore):9}")
        board_copy = deepcopy(board)
        if board_copy.place_tetramino(tetramino):
            feasible += 1
            states_to_explore.append( (next_tidx+1, board_copy) )
            
        


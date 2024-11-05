from copy import deepcopy
from board import Board
from tetramino import Tetramino
from collections import deque
from sys import argv
from time import time


EXPORT_SOLUTIONS = False
EXPORT_STEPS = False


# Load board and tetraminos
base_board:Board = Board("maps/nov5.txt")
tetraminos_to_place:list[Tetramino] = Tetramino.load_tetraminos_from_json("tetraminos/default.json")
tetramino_count = len(tetraminos_to_place)
min_tetramino_size = min( len(tetramino.get_positions()) for tetramino in tetraminos_to_place )

start_time = time()

# Precalculate all feasible placement of tetraminos and their variants considering FORBIDDEN squares
tetramino_placements = [
    [
        deepcopy(v).shift(dx,dy)
        for v in t.get_variants()
        for dx in range(base_board.width - v.width() + 1)
        for dy in range(base_board.height - v.height() + 1)
        if deepcopy(base_board).place_tetramino(deepcopy(v).shift(dx,dy), min_region_size=min_tetramino_size)
    ]
    for t in tetraminos_to_place
]
for tidx,t in enumerate(tetraminos_to_place):
    print(f"{len(tetramino_placements[tidx])} feasible placement for {t} and its variants.")

# Sort tetraminos based on number of feasible variants to make top of the tree narrower:
tetramino_placements.sort(key = lambda x: len(x))



# Initialize search
tries = feasible = hopeless = visited = solution = 0
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
        progress_text = "  0.00 % "
        print_progress = True
    case _: exit("Provide BFS or DFS")



while len(states_to_explore) != 0:
    visited += 1
    next_tidx, board = next_state()

    if EXPORT_STEPS:
        for count in range(30 if next_tidx == tetramino_count else 1):
            with open(f"tmp/{visited:09}_{count:02}.svg", "w") as f:
                f.write(board.to_svg(highlight=(count>0)))

    if next_tidx == 1 and print_progress:
        progress += progress_increase
        progress_text = f"{progress:5.2f} % "

    if next_tidx == tetramino_count:
        solution += 1
        if EXPORT_SOLUTIONS:
            with open(f"saves/nov5_default_{solution:09}.svg", "w") as f:
                f.write(board.to_svg())
        continue
    for tetramino in tetramino_placements[next_tidx]:        
        tries += 1
        if tries % report_interval == 0:
            print(f"{progress_text}Tries: {tries:9} feasible:{feasible:9} hopeless:{hopeless:9} explored:{visited:9} solutions:{solution:3} to explore: {len(states_to_explore):9}")
        board_copy = deepcopy(board)
        if board_copy.place_tetramino(tetramino, revert_on_failure=False):
            feasible += 1
            if board_copy.has_small_disjoint_region(min_tetramino_size): 
                hopeless += 1
                if next_tidx==0 and print_progress:
                    progress += progress_increase
                    progress_text = f"{progress:5.2f} % "
            else: states_to_explore.append( (next_tidx+1, board_copy) )

print(f""" 
      
Final report:
    Time elapsed: {time()-start_time} seconds

    {tries:9} tetramino placement tried
    {feasible:9} was feasible, from which 
    {hopeless:9} resulted in too small disjoint regions, the remaining 
    {visited:9} was explored, from which
    {solution:9}  was a good solution
""")
            
        


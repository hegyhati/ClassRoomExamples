gain2024_szomszedossagi_lista = [
    [1, 2, 5],
    [0, 2, 6],
    [0, 1, 7],
    [5, 4],
    [5, 3],
    [0, 3, 4],
    [1, 7],
    [2, 6]
]

gain2024_szomszedossagi_matrix = [
    [None, True, True, False, False, True, False, False],
    [True, None, True, False, False, False, True, False],
    [True, True, None, False, False, False, False, True],
    [False, False, False, None, True, True, False, False],
    [False, False, False, True, None, True, False, False],
    [True, False, False, True, True, None, False, False],
    [False, True, False, False, False, False, None, True],
    [False, False, True, False, False, False, True, None]
]

from parse import *
lista = parse_to_adjacency_list("gain2024.json")
matrix = parse_to_adjacency_matrix("gain2024.json")

i = 2
j = 4

# i es j indexu embere ismeri-e egymast?
if j in lista[i] : pass
if matrix[i][j] : pass

# i fokszama?
len(lista[i])

count = 0
for j in range(len(matrix)):
    if matrix[i][j]: 
        count += 1

sum(1 if matrix[i][j] else 0 for j in range(len(matrix)))
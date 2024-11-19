from sys import argv
from timeit import timeit
from graph import Graph
from graph_mate import *
from graph_others import *
classes = [
    AdjacencyMatrixGraph, 
    AdjacencyListGraph, 
    EdgeListGraph, 
    DzseniDaniGraph, 
    DzseniDaniModGraph, 
    DzseniDaniStupidModGraph,
    AkosAdrianAronGraph,
    AnnaLoriDaniGraph
]


def display_graph(g):
    print(g.vertex_count())
    for v in range(g.vertex_count()):
        print(v, ":", ", ".join([str(u) for u in g.neighbors_of(v)]))
    
if len(argv) == 3:
    N = int(argv[1])
    M = int(argv[2])

    file = f"n_{N}_m_{M}.dot"
    DzseniDaniGraph.random_graph(N,M).save_to_dot(file)
else:
    file = "n_10000_m_1000000.dot"

graphs:list[Graph] = [cls.load_from_dot(file) for cls in classes]

for g in graphs:
    print(timeit(lambda: g.shortest_path(0,5645), number=1), end="\t")
    print(str(g.__class__))



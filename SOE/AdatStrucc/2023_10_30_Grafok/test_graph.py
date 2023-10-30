from timeit import timeit
from graph import MatrixGraph, NumpyMatrixGraph, NeighborListGraph, NeighborSetGraph, EdgeListGraph, EdgeSetGraph, random_graph


n = int(input())
m = int(input())

cls_list = [MatrixGraph, NumpyMatrixGraph, NeighborListGraph, NeighborSetGraph, EdgeListGraph,EdgeSetGraph]
graphs = random_graph(cls_list, n, m)

print("Graphs ready")

for cls in cls_list:
    print(cls.__name__, timeit(lambda: graphs[cls.__name__].has_edge(0,1), number=10**3))
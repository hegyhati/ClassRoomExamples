from abc import ABC, abstractmethod
from random import randrange


class Graph(ABC):
    
    @abstractmethod
    def __init__(self, size:int) -> None:
        super().__init__()

    @abstractmethod
    def add_edge(self, x:int, y:int) -> None:
        pass    

    @abstractmethod
    def has_edge(self, x:int, y:int) -> bool:
        pass

class MatrixGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = [[False] * size for _ in range(size)]
    def add_edge(self, x: int, y: int) -> None:
        self._edges[x][y] = True
        self._edges[y][x] = True
    def has_edge(self, x: int, y: int) -> bool:
        return self._edges[x][y]

from numpy import array, zeros
class NumpyMatrixGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = zeros((size,size), dtype=bool)
    def add_edge(self, x: int, y: int) -> None:
        self._edges[x,y] = True
        self._edges[y,x] = True
    def has_edge(self, x: int, y: int) -> bool:
        return self._edges[x,y]


class NeighborListGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = [ [] for _ in range(size) ]
    def add_edge(self, x: int, y: int) -> None:
        self._edges[x].append(y)
        self._edges[y].append(x)
    def has_edge(self, x: int, y: int) -> bool:
        return y in self._edges[x]

class NeighborSetGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = [ set() for _ in range(size) ]
    def add_edge(self, x: int, y: int) -> None:
        self._edges[x].add(y)
        self._edges[y].add(x)
    def has_edge(self, x: int, y: int) -> bool:
        return y in self._edges[x]

class EdgeListGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = [ ]
    def add_edge(self, x: int, y: int) -> None:
        self._edges.append((x,y))
        self._edges.append((y,x))
    def has_edge(self, x: int, y: int) -> bool:
        return (x,y) in self._edges

class EdgeSetGraph(Graph):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._edges = set()
    def add_edge(self, x: int, y: int) -> None:
        self._edges.add((x,y))
        self._edges.add((y,x))  
    def has_edge(self, x: int, y: int) -> bool:
        return (x,y) in self._edges

def random_graph(cls_list, n: int, m:int) -> "Graph":
    graphs = {cls.__name__ : cls(n) for cls in cls_list}
    count = m * len(cls_list)
    while count > 0:
        x = randrange(n)
        y = randrange(n)
        for cls in cls_list:
            # if not graphs[cls.__name__].has_edge(x,y):
                graphs[cls.__name__].add_edge(x, y)
                count -= 1
    return graphs

if __name__ == "__main__":
    graphs = random_graph([MatrixGraph, NeighborListGraph], 10, 20)
    print(graphs)
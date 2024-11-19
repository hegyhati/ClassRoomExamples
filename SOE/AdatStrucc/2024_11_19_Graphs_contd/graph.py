from abc import ABC, abstractmethod
from random import randrange
from collections import deque
from timeit import timeit

class Graph(ABC):

    def __init__(self, vertex_count:int, edges:list[tuple[int,int]]) -> None:
        super().__init__()
        # print(vertex_count, edges)
        print(timeit(lambda: self._initialize(vertex_count, edges), number=1), self.__class__)
        
    
    @abstractmethod
    def _initialize(self, vertex_count:int, edges:list[tuple[int,int]]) -> None:
        pass

    @classmethod
    def test_house_graph(cls) -> "Graph":
        return cls(5,[(0,1),(0,2),(1,2),(1,3),(2,4),(3,4)])

    @classmethod
    def random_graph(cls, vertex_count:int, edge_count:int) -> "Graph":
        edges = set()
        while len(edges) != edge_count:
            v1 = randrange(vertex_count)
            v2 = randrange(vertex_count)
            if v1 != v2:
                edges.add((min(v1,v2),max(v1,v2)))
        return cls(vertex_count,list(edges))
    
    @classmethod
    def load_from_dot(cls, filename:str) -> "Graph":
        next_vertex = 0
        vertices = {}
        edges = []
        with open(filename) as f:
            for line in f:
                if line.strip() == "": continue
                if "graph" in line: continue
                if "{" in line: continue
                if "}" in line: continue
                if "--" in line:
                    ends = line.split("--")
                    edges.append((int(ends[0]), int(ends[1])))
                else:
                    vertex = int(line)
                    vertices[vertex] = next_vertex
                    next_vertex+=1
        return cls(next_vertex, [ (vertices[a],vertices[b]) for (a,b) in edges] )

    def save_to_dot(self, filename:str) -> None:
        with open(filename, "w") as f:
            f.write("graph {\n")
            for v in range(self.vertex_count()):
                f.write(f"  {v}\n")
            f.write("\n")
            for (v1,v2) in self.edges():
                f.write(f" {v1} -- {v2}\n")
            f.write("}\n\n")
    
    @abstractmethod
    def vertex_count(self) -> int:
        pass

    @abstractmethod
    def edge_count(self) -> int:
        pass

    def edges(self) -> list[tuple[int,int]]:
        return [
            (vertex, neighbor)    
            for vertex in range(self.vertex_count())
            for neighbor in self.neighbors_of(vertex) 
            if vertex < neighbor
        ]
        

    @abstractmethod
    def neighbor_count(self, v:int) -> int:
        pass

    @abstractmethod
    def neighbors_of(self,v:int) -> set[int]:
        pass

    def cluster(self,v:int) -> set[int]:
        v_cluster = set()
        to_explore = {v}
        while len(to_explore) != 0:
            u = to_explore.pop()
            v_cluster.add(u)
            to_explore.update(self.neighbors_of(u).difference(v_cluster))
        return v_cluster
    
    def shortest_path(self, source:int, destination:int) -> list[int]|None:
        if source == destination:
            return [source]
        
        visited = {source}
        queue = deque([(source, [source])])

        while queue:
            current, path = queue.popleft()
            for neighbor in self.neighbors_of(current):
                if neighbor == destination:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
        
        
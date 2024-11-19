from graph import Graph

class AdjacencyListGraph(Graph):

    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.__neighbors = [ [] for _ in range(vertex_count) ]
        for (v1,v2) in edges:
            self.__neighbors[v1].append(v2)
            self.__neighbors[v2].append(v1)
    
    def vertex_count(self) -> int:
        return len(self.__neighbors)

    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.__neighbors) // 2

    def neighbor_count(self, v:int) -> int:
        return len(self.__neighbors[v])

    def neighbors_of(self,v:int) -> set[int]:
        return set(self.__neighbors[v])


class AdjacencyMatrixGraph(Graph):
    def __init__(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        super().__init__(vertex_count, edges)

    def _initialize(self, vertex_count:int, edges:list[tuple[int,int]]) -> None:
        self.__matrix = [
            [False] * vertex_count
            for _ in range(vertex_count)
        ]
        for (v1,v2) in edges:
            self.__matrix[v1][v2] = self.__matrix[v2][v1] = True
    
    
    def vertex_count(self) -> int:
        return len(self.__matrix)

    
    def edge_count(self) -> int:
        return sum(l.count(True) for l in self.__matrix) // 2

    def neighbor_count(self, v:int) -> int:
        return self.__matrix.count(True)
    
    def neighbors_of_original(self, v: int) -> set[int]:
        return {u for u in range(self.vertex_count()) if self.__matrix[v][u]}
    
    def neighbors_of(self, v: int) -> set[int]:
        return {u for u,connected in enumerate(self.__matrix[v]) if connected}



class EdgeListGraph(Graph):

    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.__vertex_vount = vertex_count
        self.__edges = edges[:]
    
    def vertex_count(self) -> int:
        return self.__vertex_vount

    def edge_count(self) -> int:
        return len(self.__edges)

    def edges(self) -> list[tuple[int,int]]:
        return self.__edges[:]

    def neighbor_count(self, v:int) -> int:
        return len(self.neighbors_of(v))

    def neighbors_of(self,v:int) -> set[int]:
        return {
            sum(edge)-v
            for edge in self.__edges
            if v in edge 
        }
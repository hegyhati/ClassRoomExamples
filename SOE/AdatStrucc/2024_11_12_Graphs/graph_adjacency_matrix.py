from graph import Graph

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

    
    def edges(self) -> list[tuple[int,int]]:
        return [
            (v1,v2) 
            for v1 in range(self.vertex_count())
            for v2 in range(v1+1, self.vertex_count())
            if self.__matrix[v1][v2]
        ]
    
    def neighbor_count(self, v:int) -> int:
        return self.__matrix.count(True)
    
    def neighbors_of(self, v: int) -> set[int]:
        return {u for u in range(self.vertex_count()) if self.__matrix[v][u]}
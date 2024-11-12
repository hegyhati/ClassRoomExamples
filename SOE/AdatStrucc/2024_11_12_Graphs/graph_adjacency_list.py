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

    def edges(self) -> list[tuple[int,int]]:
        return [
            (v1,v2)
            for v1, neighbors in enumerate(self.__neighbors)
            for v2 in neighbors
            if v1 < v2
        ]

    def neighbor_count(self, v:int) -> int:
        return len(self.__neighbors[v])

    def neighbors_of(self,v:int) -> set[int]:
        return set(self.__neighbors(v))
from copy import deepcopy
from graph import Graph

class EdgeListGraph(Graph):

    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.__vertex_vount = vertex_count
        self.__edges = deepcopy(edges)
    
    def vertex_count(self) -> int:
        return self.__vertex_vount

    def edge_count(self) -> int:
        return len(self.__edges)

    def edges(self) -> list[tuple[int,int]]:
        return deepcopy(self.__edges)

    def neighbor_count(self, v:int) -> int:
        return len(self.neighbors_of(v))

    def neighbors_of(self,v:int) -> set[int]:
        return {
            sum(edge)-v
            for edge in self.__edges
            if v in edge 
        }
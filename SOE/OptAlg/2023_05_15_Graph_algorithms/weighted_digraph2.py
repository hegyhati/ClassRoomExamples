import sys
from typing import Set


class Digraph:
    def __init__(self) -> None:
        self.data = {}

    def add_vertex(self, vertex_name:str):
        self.data[vertex_name] = []
    
    def add_arc(self, from_vertex:str, to_vertex:str, weight: float = 1):
        if from_vertex in self.data.keys() and to_vertex in self.data.keys():
            self.data[from_vertex].append((to_vertex,weight))
    
    def has_arc(self, from_vertex:str, to_vertex:str) -> bool:
        if from_vertex in self.data:
            for (t,w) in self.data[from_vertex]:
                if t == to_vertex: return True
        return False
    
    def get_weight(self, from_vertex:str, to_vertex:str) -> float:
        if from_vertex in self.data:
            for (t,w) in self.data[from_vertex]:
                if t == to_vertex: return w
        return False

    def reachable_vertices(self, vertex: str) -> Set[str]:
        self.reached_vertices = set()
        self.explore(vertex)
        return self.reached_vertices

    def explore(self, vertex: str):
        self.reached_vertices.add(vertex)
        for (t,w) in self.data[vertex]:
            if t not in self.reached_vertices:
                self.explore(t)

    def shortest_path(self, vertex_from:str, vertex_to:str) -> float:
        fixed_vetices = set() # H 
        all_vertices = set(self.data.keys())
        distance = { vertex: sys.float_info.max for vertex in self.data}
        distance[vertex_from] = 0
        while len(all_vertices - fixed_vetices) != 0:
            min_vertex = list((all_vertices - fixed_vetices))[0]
            for vertex in all_vertices - fixed_vetices:
                if distance[vertex] < distance[min_vertex]:
                    min_vertex = vertex
            if min_vertex == vertex_to:
                return distance[min_vertex]
            fixed_vetices.add(min_vertex)
            for neighbor, weight in self.data[min_vertex]:
                if neighbor not in fixed_vetices:
                    if distance[neighbor] > distance[min_vertex] + weight:
                        distance[neighbor] = distance[min_vertex] + weight
        return None





        

def test_graph():
    d = Digraph()
    for vertex in "ABCD":
        d.add_vertex(vertex)
    d.add_arc("A", "C")
    d.add_arc("C", "B")
    d.add_arc("B", "A")
    d.add_arc("C", "D")
    print( "OK" if not d.has_arc("A","B") else "ERROR" )
    print( "OK" if     d.has_arc("A","C") else "ERROR" )
    print( "OK" if not d.has_arc("A","D") else "ERROR" )
    print( "OK" if     d.has_arc("B","A") else "ERROR" )
    print( "OK" if not d.has_arc("B","C") else "ERROR" )
    print( "OK" if not d.has_arc("B","D") else "ERROR" )

    print( "OK" if d.reachable_vertices("A") == {"A", "B", "C", "D"} else "ERROR" )
    print( "OK" if d.reachable_vertices("B") == {"A", "B", "C", "D"} else "ERROR" )
    print( "OK" if d.reachable_vertices("C") == {"A", "B", "C", "D"} else "ERROR" )
    print( "OK" if d.reachable_vertices("D") == {"D"} else "ERROR" )


def test_Dijkstra():
    d = Digraph()
    for v in "ABCDEF":
        d.add_vertex(v)
    for e in ["AB1", "BC2", "CD3", "DE1", "EF2", "BE8", "CA4"]:
        d.add_arc(e[0],e[1],float(e[2:]))
    for v in "ABCDEF":
        for v2 in "ABCDEF":
            print(f" {v} -> {v2} {d.shortest_path(v,v2)}")


if __name__ == "__main__":
    test_Dijkstra()

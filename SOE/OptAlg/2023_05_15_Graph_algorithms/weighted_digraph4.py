from typing import Set


class Digraph:
    def __init__(self) -> None:
        self.data = {}

    def add_vertex(self, vertex_name:str):
        for other_vertex in self.data:
            self.data[other_vertex][vertex_name] = None
        self.data[vertex_name] = { vertex : None for vertex in self.data}
        self.data[vertex_name][vertex_name] = None
    
    def add_arc(self, from_vertex:str, to_vertex:str, weight: float = 1):
        if from_vertex in self.data.keys() and to_vertex in self.data.keys():
            self.data[from_vertex][to_vertex] = weight
    
    def has_arc(self, from_vertex:str, to_vertex:str) -> bool:
        return self.data[from_vertex][to_vertex] != None

    def get_weight(self, from_vertex:str, to_vertex:str) -> float:
        return self.data[from_vertex][to_vertex]

    def reachable_vertices(self, vertex: str) -> Set[str]:
        self.unreached_vertices = set(self.data.keys())
        self.explore(vertex)
        return set(self.data.keys()) - self.unreached_vertices

    def explore(self, vertex: str):
        if vertex not in self.unreached_vertices: return 
        self.unreached_vertices.remove(vertex)
        for t in self.unreached_vertices.copy():
            if self.data[vertex][t] != None:
                self.explore(t)

    
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

if __name__ == "__main__":
    test_graph()

from typing import Set


class Digraph:
    def __init__(self) -> None:
        self.vertices = []
        self.arcs = []
    
    def add_vertex(self, vertex_name:str):
        self.vertices.append(vertex_name)
    
    def add_arc(self, from_vertex:str, to_vertex:str, weight: float = 1):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.arcs.append( (from_vertex, to_vertex, weight) )
    
    def has_arc(self, from_vertex:str, to_vertex:str) -> bool:
        for (f,t,w) in self.arcs:
            if f == from_vertex and t == to_vertex: return True
        return False

    def get_weight(self, from_vertex:str, to_vertex:str) -> float:
        for (f,t,w) in self.arcs:
            if f == from_vertex and t == to_vertex: return w
        return None
    
    def reachable_vertices(self, vertex: str) -> Set[str]:
        self.reached_vertices = []
        self.explore(vertex)
        return set(self.reached_vertices)

    def explore(self, vertex: str):
        self.reached_vertices.append(vertex)
        for (f,t,w) in self.arcs:
            if f == vertex and t not in self.reached_vertices:
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

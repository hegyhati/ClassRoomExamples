class Digraph:
    def __init__(self) -> None:
        self.data = {}

    def add_vertex(self, vertex_name:str):
        self.data[vertex_name] = set()
    
    def add_arc(self, from_vertex:str, to_vertex:str):
        if from_vertex in self.data.keys() and to_vertex in self.data.keys():
            self.data[from_vertex].add(to_vertex)
    
    def has_arc(self, from_vertex:str, to_vertex:str) -> bool:
        if from_vertex in self.data:
            return to_vertex in self.data[from_vertex]
        else: return False

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

if __name__ == "__main__":
    test_graph()

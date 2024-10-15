import random


class Graph:
    def __init__(self) -> None:
        self.vertices = {}
    
    def __str__(self) -> str:
        return "( {" + ", ".join(self.vertices.keys()) + "} , {" + ",".join([f"{v1}-{v2}" for v1 in self.vertices for v2 in self.vertices[v1]]) + "} )"
    
    
    def add_vertex(self, new_vertex:str) -> None:
        if new_vertex in self.vertices:
            raise ValueError("Vertex already exists.")
        self.vertices[new_vertex] = set()
    def add_edge(self, v1:str, v2:str) -> None:
        if v1 not in self.vertices:
            raise ValueError(f"No vertex: {v1}")
        if v2 not in self.vertices:
            raise ValueError(f"No vertex: {v2}")
        if v1 == v2:
            raise ValueError(f"No loops are allowed.")
        if v1 in self.vertices[v2]:
            raise ValueError(f"Edge {v1}-{v2} already exists")
        
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def vertex_count(self) -> int:
        return len(self.vertices)
    def edge_count(self) -> int:
        return sum(len(self.vertices[v]) for v in self.vertices) // 2
    def has_vertex(self, vertex:str) -> bool:
        return vertex in self.vertices
    def has_edge(self, v1:str, v2:str) -> bool:
        return self.has_vertex(v1) and self.has_vertex(v2) and v1 in self.vertices[v2]
    
    def neighbors(self, vertex:str) -> set[str]:
        if vertex not in self.vertices:
            raise ValueError(f"No vertex: {vertex}")
        return self.vertices[vertex].copy()

    @staticmethod
    def complete_graph(number_of_vertices:int) -> "Graph":
        g = Graph()
        for v in range(number_of_vertices):
            g.add_vertex(str(v))
        for v1 in range(number_of_vertices):
            for v2 in range(v1+1, number_of_vertices):
                g.add_edge(str(v1),str(v2))
        return g

    @staticmethod
    def random_graph(number_of_vertices: int, number_of_edges: int) -> "Graph":
        if number_of_edges > number_of_vertices * (number_of_vertices - 1) // 2:
            raise ValueError("Too many edges.")
        g = Graph()
        for v in range(number_of_vertices):
            g.add_vertex(str(v))
        while g.edge_count() < number_of_edges:
            v1 = random.randrange(number_of_vertices)
            v2 = random.randrange(number_of_vertices)
            try:
                g.add_edge(str(v1),str(v2))
            except ValueError:
                pass
        return g
    
    @staticmethod
    def load_from_file(filename:str) -> "Graph":
        g = Graph()
        with open(filename) as f:
            for line in f:
                v1,v2=[v.strip() for v in line.split(" ")]
                if not g.has_vertex(v1): g.add_vertex(v1)
                if not g.has_vertex(v2): g.add_vertex(v2)
                g.add_edge(v1,v2)
        return g
        
    
    
    def save_to_file(self, filename:str) -> None:
        with open(filename, "w") as f:
            for v1 in self.vertices:
                for v2 in self.vertices[v1]:
                    if v1<v2:
                        f.write(f"{v1} {v2}\n")


if __name__ == "__main__":
    g = Graph.random_graph(10,20)
    print(g)
    g.save_to_file("foobar.txt")
    g2 = Graph.load_from_file("foobar.txt")
    print(g2)
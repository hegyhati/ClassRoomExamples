import random

class Graph:
    def __init__(self, n):
        self.vertex = n
   
    @staticmethod
    def random_graph(n, m): # n = csúcs, m = él
        if m > n * (n - 1) // 2:
            raise ValueError("Too many edges.")
        
        g = Graph(n)
        
        table = [[None if row == col else 0 for row in range(n)] for col in range(n)]
        edges = 0
                        
        while edges < m:
            choices = range(n)
            random_col = random.choice(choices)
            random_row = random.choice(choices)
            if table[random_col][random_row] == 0:
                table[random_col][random_row] = 1
                table[random_row][random_col] = 1
                edges += 1

        print(edges)
        g.graph = table
        g.edges = edges
        return g
    
    def edge_count(self) -> int:
        return self.edges
    
    def vertex_count(self):
        return self.vertex
    
    def neighbors_of(self, v) -> set[int]:
        row = self.table[v]
        neighbors = set()
        for i, item in enumerate(row):
            if item == 1:
                neighbors.add(i)
                
        return neighbors
            
                     
g = Graph.random_graph(8,10)
g.edge_count()
g.vertex_count()
g.neighbors_of(0)





            
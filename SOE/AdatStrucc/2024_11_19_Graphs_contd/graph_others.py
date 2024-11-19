from graph import Graph

class AkosAdrianAronGraph(Graph):
   
    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.vertex = self.vertex_count
        self.table = [[None if row == col else 0 for row in range(vertex_count)] for col in range(vertex_count)]
        self.__edges = len(edges)
                        
        for (a,b) in edges:
            self.table[a][b] = 1
            self.table[b][a] = 1      
    
    def edge_count(self) -> int:
        return self.__edges
    
    def vertex_count(self):
        return self.vertex
    
    def neighbors_of(self, v) -> set[int]:
        return {
            i
            for i, item in enumerate(self.table[v])
            if item == 1
        }
    
    def neighbor_count(self, v: int) -> int:
        return self.table[v].count(1)

class DzseniDaniGraph(Graph):
    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.adj_list = {vertex : set() for vertex in range(vertex_count)}
        for (a,b) in edges:
            self.adj_list[a].add(b)
            self.adj_list[b].add(a)            

    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj_list.values()) // 2
    
    def vertex_count(self) -> int:
        return len(self.adj_list)
    
    def neighbors_of(self, v:int) -> set[int]:
        return self.adj_list[v]   
    
    def neighbor_count(self, v: int) -> int:
        return len(self.adj_list[v])

class DzseniDaniModGraph(Graph):
    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.adj_list = [ set() for vertex in range(vertex_count)]
        for (a,b) in edges:
            self.adj_list[a].add(b)
            self.adj_list[b].add(a)            

    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj_list) // 2
    
    def vertex_count(self) -> int:
        return len(self.adj_list)
    
    def neighbors_of(self, v:int) -> set[int]:
        return self.adj_list[v]   
    
    def neighbor_count(self, v: int) -> int:
        return len(self.adj_list[v])

class DzseniDaniStupidModGraph(Graph):
    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.adj_list = {vertex :  [] for vertex in range(vertex_count)}
        for (a,b) in edges:
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)            

    def edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj_list.values()) // 2
    
    def vertex_count(self) -> int:
        return len(self.adj_list)
    
    def neighbors_of(self, v:int) -> set[int]:
        return set(self.adj_list[v])
    
    def neighbor_count(self, v: int) -> int:
        return len(self.adj_list[v])

class AnnaLoriDaniGraph(Graph):
    def _initialize(self, vertex_count: int, edges: list[tuple[int, int]]) -> None:
        self.n = vertex_count
        self.__edges = set(edges)

    def edge_count(self) -> int:
        return len(self.__edges)

    def vertex_count(self) -> int:
        return len(self.n)

    def neighbor_count(self, v: int) -> int:
        count = 0
        for (a,b) in self.__edges:
            if a==v or b==v: 
                count += 1
        return count
    
    def neighbors_of(self, v: int) -> set[int]:
        neighbors = set()
        for (a,b) in self.__edges:
            if a==v:
                neighbors.add(b)
            elif b==v:
                neighbors.add(a)
        return neighbors
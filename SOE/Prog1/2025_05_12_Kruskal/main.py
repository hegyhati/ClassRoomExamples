import random
from sys import argv

class Graph:
    def __init__(self, n:int):
        self.__n = n
        self.__edges = set()

    def __check_vertex(self, v:int) -> None:
        if v < 1 or v > self.__n: raise ValueError(f"No such vertex: {v}")

    def edge_count(self) -> int:
        return len(self.__edges)
    
    def add_edge(self, v:int, u:int, w:int):
        self.__check_vertex(v)
        self.__check_vertex(u)
        if u == v : return
        if self.has_edge(u,v): return
        self.__edges.add((u,v,w))

    def has_edge(self, v:int, u:int) -> bool:
        self.__check_vertex(v)
        self.__check_vertex(u)
        if u == v : return False
        for (vv,uu,_) in self.__edges:
            if vv==v and uu==u or vv==u and uu==v : return True
        return False

    def __str__(self):
        return f"({set(range(1,self.__n+1))} { {f'{v} --{w}-- {u}'  for (u,v,w) in self.__edges} })"   

    def get_reachable_vertices(self, v:int) -> set[int]:
        self.__check_vertex(v)
        painted = {v}
        for _ in range(self.__n-1):
            for (vv,uu,w) in self.__edges:
                if vv in painted: painted.add(uu)
                if uu in painted: painted.add(vv)
        return painted

    def is_connected(self) -> bool:
        return len(self.get_reachable_vertices(1)) == self.__n
    
    def has_path_between(self, v:int, u:int) -> bool:
        return u in self.get_reachable_vertices(v)

    def Kruskal(self) -> "Graph":
        sorted_edges = list(self.__edges)
        sorted_edges.sort(key = lambda edge: edge[2])
        MST = Graph(self.__n)
        while len(sorted_edges) != 0:
            (v,u,w) = sorted_edges.pop(0)
            if not MST.has_path_between(v, u) : 
                MST.add_edge(v,u,w)
        return MST
    
    def get_weightless_edges(self):
        return { (min(u,v), max(u,v)) for (u,v,_) in self.__edges}
    
    def export_to_dot(self, filename:str, highlight_edges:None|set[tuple[int,int]] = None):
        with open(filename, "w") as f:
            f.write("graph{\n")
            for (u,v,w) in self.__edges:
                if highlight_edges is not None and ((u,v) in highlight_edges or (v,u) in highlight_edges):
                    color = "blue"
                else:
                    color = "black"
                f.write(f"\t{v} -- {u} [label=\"{w}\" color={color}]\n")
            f.write("}\n")

def generate_random_graph(n:int, m:int) -> Graph:
    if n < 1: raise ValueError("At least one vertex.")
    if m > n*(n-1)/2: raise ValueError("Too many edges.")
    G = Graph(n)    
    while G.edge_count() != m:
        G.add_edge(random.randint(1,n), random.randint(1,n), random.randint(1,100))
    return G

def complete_graph(n:int) -> Graph:
    if n < 1: raise ValueError("At least one vertex.")
    G = Graph(n)
    for u in range(1,n):
        for v in range(u+1,n+1):
            G.add_edge(u,v,1)
    return G


G = generate_random_graph(int(argv[1]),int(argv[2]))
print(G)
G.export_to_dot("G.dot")
if not G.is_connected():
    print("Not connected :-/")
else:
    print("Yay connected!!!")
    MST = G.Kruskal()
    G.export_to_dot("MST.dot", MST.get_weightless_edges())
    print(MST)

K5 = complete_graph(5)
K5.export_to_dot("K5.dot")
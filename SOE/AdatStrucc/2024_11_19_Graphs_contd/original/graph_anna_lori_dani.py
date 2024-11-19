import random
from collections import deque

class Graph:
    def __init__(self, n, m):
        self.n = n  
        self.m = m  
        self.neighbor_list = {}
        self.edges = self._generate_edges()
        self._build_graph()

    def _generate_edges(self):
        edges = set()
        while len(edges) < self.m:
            u = random.randint(0, self.n - 1)
            v = random.randint(0, self.n - 1)
            if u != v: 
                edges.add((u, v) if u < v else (v, u))
        return list(edges)

    def _build_graph(self):
        for u, v in self.edges:
            if u not in self.neighbor_list:
                self.neighbor_list[u] = []
            if v not in self.neighbor_list:
                self.neighbor_list[v] = []
            self.neighbor_list[u].append(v)
            self.neighbor_list[v].append(u) 

    def __str__(self):
        result = "Élek:\n" + "\n".join(f"{u} - {v}" for u, v in self.edges) + "\n"

        for node, neighbors in self.neighbor_list.items():
            result += f"{node}: {neighbors}\n"
        return result

    def edge_count(self) -> int:
        return len(self.edges)

    def vertex_count(self) -> int:
        return len(self.neighbor_list)

    def neighbors(self, node):
        return self.neighbor_list.get(node, [])
    
    def cluster(self, start):
        reachable = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in reachable:
                reachable.add(node)
                for neighbor in self.neighbor_list.get(node, []):
                    if neighbor not in reachable:
                        queue.append(neighbor)
        return reachable
    
    def shortest_path(self, start, goal):
        if start == goal:
            return [start]
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == goal:
                return path
            visited.add(current)
            for neighbor in self.neighbor_list.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None
    
    def load_from_dot(self, filename):
        self.edges = []
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if "--" in line:
                    
                    parts = line.split("--")
                    u = int(parts[0].strip())  
                    v = int(parts[1].strip().rstrip(";")) 
                    self.edges.append((u, v))

                self.neighbor_list.clear()
                self._build_graph()


if __name__=="__main__":
    random_graph = Graph(n = 4, m = 5)   
    random_graph.load_from_dot("graph.dot")
    print(random_graph)
    print(f"Élek száma: {random_graph.edge_count()}")
    print(f"Csúcsok száma: {random_graph.vertex_count()}")
    print(f"Szomszédok : {random_graph.neighbors(0)}")
    print(f"Elérhető csúcsok: {random_graph.cluster(0)}")
    print(f"Legrövidebb út: {random_graph.shortest_path(0, 4)}")
import random
import json
from collections import deque

class RandomGraph:
    def __init__(self, n, m):
        self.num_vertices = n
        self.num_edges = m
        self.edges = self.generate_random_edges()
        self.adjacency_list = self.create_adjacency_list()

    def generate_random_edges(self):
        edges = set()
        while len(edges) < self.num_edges:
            u = random.randint(0, self.num_vertices - 1)
            v = random.randint(0, self.num_vertices - 1)
            if u != v:
                edges.add((u, v))
        return edges
    
    def save_to_json(self):
        graph_data = {
            "num_vertices": self.num_vertices,
            "num_edges": self.num_edges,
            "edges": list(self.edges)
        }
        with open("MyLovelyGraph", 'w') as json_file:
            json.dump(graph_data, json_file, indent=4)        

    def create_adjacency_list(self):
        adjacency_list = {i: [] for i in range(self.num_vertices)}
        for u, v in self.edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        return adjacency_list

    def find_shortest_path(self, start, end):
        queue = deque([(start, [])])  
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            if current not in visited:
                visited.add(current)
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [(current, neighbor)]))
        return None

    def neighbors(self,v:int) -> set[int]:
        return set(self.adjacency_list[v])

    def display_edges(self):
        print("Generált élek:", self.edges)

num_vertices = 10
num_edges = 8
graph = RandomGraph(num_vertices, num_edges)
graph.save_to_json()
graph.display_edges()

start = 1
end = 6
shortest_path = graph.find_shortest_path(start, end)
if shortest_path != None:
    print(f"Legrövidebb út {start}-tól {end}-ig:", shortest_path)
else:
    print("nincs összekötve",start,"a(z)",end,"-vel")

vertex=2
print(f"A(z) {vertex} csúcs szomszédai:", graph.neighbors(vertex))
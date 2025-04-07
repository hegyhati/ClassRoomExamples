import json
import random
from sys import argv

def parse_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
    names = list(data.keys())
    return [
        [True if name2 in data[name] else False for name2 in names]
        for name in names
    ]

def generate_empty_graph(n):
    return [ [False] * n for _ in range(n) ]

# at most m edges
def generate_random_graph(n,max_m):
    G = generate_empty_graph(n)
    for _ in range(max_m):
        u = random.randrange(n)
        v = random.randrange(n)
        G[u][v] = G[v][u] = True
    return G

def vertices(G):
    return list(range(vertex_count(G)))


def export_to_dot(G, filename, colors = None):
    with open(filename, "w") as f:
        f.write("graph{\n")
        for v in vertices(G):
            f.write(f"{v}")
            if colors is not None:
                f.write(f'[ style = "filled" fillcolor = "{COLORS[colors[v]]}"]')
            f.write("\n")

        for v in vertices(G):
            for u in vertices(G):
                if G[v][u] and v < u:
                    f.write(f"  {u} -- {v}\n")
        f.write("}\n")


def vertex_count(G):
    return len(G)

def n(G):
    return vertex_count(G)

def edge_count(G:list[list[int]]) -> int:
    return sum( sum(neighbors) for neighbors in G )  // 2

m = edge_count

COLORS = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white",
    "gray", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "aqua", "silver",
    "gold", "beige", "coral", "crimson", "indigo", "ivory", "khaki", "lavender", "plum", "salmon"
]

def color_vertices(G:list[list[int]]) -> list[int]:
    colors = []
    for v in vertices(G):
        color = 0
        while True:
            has_neighbor_with_color = False
            for u in range(v):
                if G[v][u] and colors[u] == color:
                    has_neighbor_with_color = True
                    break
            if not has_neighbor_with_color:
                break
            else:
                color += 1
        colors.append(color)
    return colors


if __name__ == "__main__":
    nG = int(argv[1])
    max_mG = int(argv[2])
    G = generate_random_graph(nG,max_mG)
    export_to_dot(G, f"examples/random_n{nG}_m{m(G)}.dot", color_vertices(G))








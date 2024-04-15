sor = {
    "Akos" : ["Aron", "Adrian"],
    "Attila" : ["Aron", "Dzseni"],
    "Aron" : ["Attila", "Dzseni", "Akos"],
    "Adrian" : ["Akos"],
    "Dzseni" : ["Aron", "Attila"]
}

def empty_graph():
    return {}

def vertices(G):
    return G.keys()

def neighbours(G, node):
    if node not in G.keys(): raise ValueError("Node doesn't exist.")
    else: return G[node]

def edge_exist(G, node1, node2):
    if node1 not in G.keys() or node2 not in G.keys(): raise ValueError("Node doesn't exist")
    return node2 in G[node1]

def add_vertex(G, node):
    if node in G.keys(): raise ValueError("Node already exists")
    G[node] = []

def add_edge(G, node1, node2):
    if node1 not in G.keys() or node2 not in G.keys(): raise ValueError("Node doesn't exist")
    G[node1].append(node2)
    G[node2].append(node1)

def delete_vertex(G, node):
    if node not in G.keys(): raise ValueError("Node doesn't exist.")
    del G["node"]
    for vertex, neighbours in G.items():
        if node in neighbours:
            neighbours.remove(node)
    


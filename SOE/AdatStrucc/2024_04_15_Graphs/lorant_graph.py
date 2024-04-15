G = {
    "vertices" : ["Akos", "Adrian", "Attila", "Aron", "Dzseni"],
    "edges" : [
    #    Akos   Adrian Attila Aron   Dzseni
        [None,  True,  False, True,  False], # Akos
        [True,  None,  False, False, False], # Adrian
        [False, False, None,  True,  True ], # Attila
        [True,  False, True,  None,  True ], # Aron
        [False, False, True,  True,  None ]  # Dzseni
    ]
}

def empty_graph():
    return {
        "vertices" : [],
        "edges" : []
    }

def vertices(G):
    return G["vertices"]

def neighbours(G, node):
    if node not in G["vertices"]: raise ValueError("Node doesn't exist.")
    idx = G[vertices].index(node)
    neighbours = []
    for nidx in range(len(G["vertices"])):
        if nidx != idx:
            if G["edges"][idx][nidx]:
                neighbours.append(G["vertices"][nidx])
    return neighbours

def edge_exist(G, node1, node2):
    if node1 not in G["vertices"] or node2 not in G["vertices"]: raise ValueError("Node doesn't exist")
    return G["edges"][G[vertices].index(node1)][G[vertices].index(node2)]

def add_vertex(G, node):
    if node in G["vertices"]: raise ValueError("Node already exists")
    G["vertices"].append(node)
    for vertex in G["edges"]:
        vertex.append(False)
    G["edges"].append([False]*(len(G["vertices"])-1) + [None])

def add_edge(G, node1, node2):
    if node1 not in G["vertices"] or node2 not in G["vertices"]: raise ValueError("Node doesn't exist")
    G["edges"][node1][node2] = True
    G["edges"][node2][node1] = True

def delete_vertex(G, node):
    pass
    

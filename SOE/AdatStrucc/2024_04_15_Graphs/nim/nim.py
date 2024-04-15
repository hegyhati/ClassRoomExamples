# General digraph stuff

def empty_graph():
    return {}

def vertices(G):
    return G.keys()

def out_neighbours(G, node):
    if node not in G.keys(): raise ValueError("Node doesn't exist.")
    else: return G[node]

def edge_exist(G, node1, node2):
    if node1 not in G.keys() or node2 not in G.keys(): raise ValueError("Node doesn't exist")
    return node2 in G[node1]

def add_vertex(G, node):
    if node in G.keys(): raise ValueError("Node already exists")
    G[node] = []

def add_arc(G, node1, node2):
    if node1 not in G.keys() or node2 not in G.keys(): raise ValueError("Node doesn't exist")
    G[node1].append(node2)
    
    
# Nim state stuff

def next_states(current):
    state = current.split(",")
    player = int(state[0])
    kavics = int(state[1])
    next = []
    if kavics > 1: next.append(f"{3-player},{kavics-1}")
    if kavics > 2: next.append(f"{3-player},{kavics-2}")
    if kavics > 3: next.append(f"{3-player},{kavics-3}")
    return next

import sys
init_state = sys.argv[1]


# Build Nim state graph

state_graph = empty_graph()

add_vertex(state_graph, init_state)

def explore_vertex(state):
    new_states = next_states(state)
    for ns in new_states:
        try:
            add_vertex(state_graph, ns)
        except:
            pass
        try:
            add_arc(state_graph, state,ns)
            explore_vertex(ns)
        except:
            pass

explore_vertex(init_state)




# visualization

import pygraphviz as pgv

nim_counter = 0
def nim_step_by_step():
    global nim_counter
    G = pgv.AGraph(directed=True, fontsize="6", size="30,30")

    for node in vertices(state_graph):
        G.add_node(node, style="filled" if colors[node] else "bold", color=colors[node] if colors[node] else "black")

    for node1 in vertices(state_graph):
        for node2 in vertices(state_graph):
            if node1 != node2 and edge_exist(state_graph, node1,node2):
                G.add_edge(node1,node2)

    G.layout()
    G.draw(f"nim_{nim_counter:04}.png", args='-Gdpi=200', prog="dot")
    nim_counter += 1

# Nim winning stategy coloring

colors = { vertex : None for vertex in vertices(state_graph)}

nim_step_by_step()
colors["1,1"] = "red"
colors["2,1"] = "green"   

# Ha van olyan, ahol en jovok, es van el zoldre, akkor ez is zold

nim_step_by_step()
while None in colors.values():
    for state in vertices(state_graph):
        if colors[state] == None and state[0]=="1":
            for next in out_neighbours(state_graph, state):
                if colors[next] == "green":
                    colors[state] = "green"
                    nim_step_by_step()
                    break
    for state in vertices(state_graph):
        if colors[state] == None and state[0]=="2":
            for next in out_neighbours(state_graph, state):
                if colors[next] == "red":
                    colors[state] = "red"
                    nim_step_by_step()
                    break
    for state in vertices(state_graph):
        if colors[state] == None and state[0]=="1":
            allred = True
            for next in out_neighbours(state_graph, state):
                if colors[next] != "red":
                    allred = False
                    break
            if allred:
                colors[state] = "red"    
                nim_step_by_step()                
    for state in vertices(state_graph):
        if colors[state] == None and state[0]=="2":
            allgreen = True
            for next in out_neighbours(state_graph, state):
                if colors[next] != "green":
                    allgreen = False
                    break
            if allgreen:
                colors[state] = "green"
                nim_step_by_step()



    

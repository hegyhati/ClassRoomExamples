# graphviz
# pygraphviz
# pydot

import pygraphviz as pgv
import adrian_graph as ag

G = pgv.AGraph()

ag.add_vertex(ag.sor, "Mate")
ag.add_edge(ag.sor, "Dzseni", "Mate")
ag.add_edge(ag.sor, "Attila", "Mate")

for node in ag.vertices(ag.sor):
    G.add_node(node)

for node1 in ag.vertices(ag.sor):
    for node2 in ag.vertices(ag.sor):
        if node1 != node2 and ag.edge_exist(ag.sor, node1,node2):
            G.add_edge(node1,node2)

G.layout()
G.draw("sor.png")



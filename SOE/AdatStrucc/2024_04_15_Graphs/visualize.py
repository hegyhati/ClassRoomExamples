# graphviz
# pygraphviz
# pydot

import pygraphviz as pgv

G = pgv.AGraph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("A", "C")

G.layout()

G.draw("foo.png")

G.add_edge("B","C")

G.draw("foo2.png")

G.layout()

G.draw("foo3.png")
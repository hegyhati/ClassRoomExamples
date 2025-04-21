from copy import deepcopy
import os
from argparse import ArgumentParser
from typing import cast
import networkx as nx
from networkx.drawing.nx_pydot import read_dot, write_dot, to_pydot
import graphviz
from PIL import Image


FIXED = "black"
FIXED_FONT = "white"
TODO = "gray"
SELECTED = "darkslategray3"
UNDISCOVERED = "white"
HIGHLIGHT_PENWIDTH = 4


# Parse the CLI arguments, DOT file, etc.

parser = ArgumentParser(description="Generating a step-by-step execution of Dijkstra's algorithm.")
parser.add_argument("dot_file", type=str, help="Path to the DOT file.")
parser.add_argument("source_node", type=str, help="Name of the source vertex")
parser.add_argument("render_dir", type=str, help="Directory for rendered dot/png files.")
args = parser.parse_args()

if not os.path.exists(args.dot_file):
    raise FileNotFoundError(f"{args.dot_file} does not exist.")
elif not os.path.isfile(args.dot_file):
    raise FileNotFoundError(f"{args.dot_file} is not a file.")

G_multi = read_dot(args.dot_file)
G = nx.Graph()
G.add_nodes_from(G_multi.nodes(data=True))
G.add_edges_from(G_multi.edges(data=True))
if args.source_node not in G.nodes:
    raise ValueError("Source node not present.")
os.makedirs(args.render_dir, exist_ok=True)
G.remove_node("\\n")


# Utility to export

counter = 0
def export_G(highlight_vertex = None):
    global counter
    G_ = deepcopy(G)
    for node in G_.nodes():
        distance = G_.nodes[node]['distance']
        G_.nodes[node]["label"] = f"{node}\n{'∞' if distance is None else distance}"
    if highlight_vertex is not None and highlight_vertex in G.nodes:
        G_.nodes[highlight_vertex]["penwidth"] = HIGHLIGHT_PENWIDTH
        for _, _, data in G_.edges(highlight_vertex, data=True):
            data["penwidth"] = HIGHLIGHT_PENWIDTH
    write_dot(G_, args.render_dir + f"/{counter:04}.dot") 
    dot = to_pydot(G_)
    dot.set_graph_defaults(dpi="300")   
    dot.set_rankdir("LR")
    graphviz.Source(dot.to_string()).render(args.render_dir + f"/{counter:04}", format="png", cleanup=True)
    counter += 1


# Initialize style

for node in G.nodes:
    G.nodes[node]["style"] = "filled" 
    G.nodes[node]["width"] = 1.1
    G.nodes[node]["height"] = 1.1

#
#  DIJKSTRA
#

# Initialize nodes
for node in G.nodes():
    G.nodes[node]["fillcolor"] = UNDISCOVERED
    G.nodes[node]["distance"] = None
export_G()

# Initialize TODO list/set with the source node
todo_vertices = {args.source_node}
G.nodes[args.source_node]["fillcolor"] = TODO
G.nodes[args.source_node]["distance"] = "0.00"
export_G()

# While there is still a gray vertex, i.e., a reachable vertex whose distance is not yet final
while len(todo_vertices) != 0:
    # Select and remove the one with the smallest distance from the gray/reached but not fixed vertices
    current = min(todo_vertices, key = lambda node: float(G.nodes[node]["distance"])) # note: definitely not None for gray vertices
    todo_vertices.remove(current)
    G.nodes[current]["fillcolor"] = SELECTED
    export_G(current)

    # Iterate over edges on current vertex
    for _, neighbor, data in G.edges(current, data=True):
        # only gray and white, i.e., not fixed vertices are of interest
        if G.nodes[neighbor]["fillcolor"] != FIXED:
            # get the current distance
            current_distance = G.nodes[neighbor]["distance"]
            # get the possible distance via currentvertex, i.e., (fixed) distance to current + edge weight
            new_distance = float(G.nodes[current]["distance"]) + float(data["label"].strip('"'))
            # if the neighbor was white, i.e., unreached so far, and thus the distance None:
            if current_distance is None:
                # set the distance
                G.nodes[neighbor]["distance"] = f"{new_distance:.2f}"
                # mark neighbor as gray and add it to todo list
                G.nodes[neighbor]["fillcolor"] = TODO
                todo_vertices.add(neighbor)
            # otherwise (neighbor is already gray/reached) if the new distance is smaller
            elif new_distance < float(current_distance):
                # update the distance of neighbor
                G.nodes[neighbor]["distance"] = f"{new_distance:.2f}"
    export_G(current)

    # Set current as fixed and remove from todo list
    G.nodes[current]["fillcolor"] = FIXED
    G.nodes[current]["fontcolor"] = FIXED_FONT
    export_G()


# Make a GIF of the generated png files

png_files = sorted([f for f in os.listdir(args.render_dir) if f.endswith(".png")])
images = [Image.open(args.render_dir + "/" + f) for f in png_files]
images[0].save(args.render_dir + "/step_by_step.gif", save_all=True, append_images=images[1:], loop=0, duration=1000)

from graph_adjacency_matrix import AdjacencyMatrixGraph
from graph_adjacency_list import AdjacencyListGraph
from graph_edge_list import EdgeListGraph
from graph_dzseni_dani import DzseniDaniGraph

cls = DzseniDaniGraph

def display_graph(g):
    print(g.vertex_count())
    for v in range(g.vertex_count()):
        print(v, ":", ", ".join([str(u) for u in g.neighbors_of(v)]))
    
N = 10
M = 10

#test_house = cls.test_house_graph()
#display_graph(test_house)
test_random = cls.random_graph(N,M)
test_random.save_to_dot("random.dot")
display_graph(test_random)
# test_dot = cls.load_from_dot("test.dot")

print("\n\nClusters:\n\n")
for v in range(N):
    print(v, ":", ", ".join([str(u) for u in test_random.cluster(v)]))


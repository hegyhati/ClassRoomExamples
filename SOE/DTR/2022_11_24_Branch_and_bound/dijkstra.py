# Disjkstra algorithm to calculate shortest paths from a source

#           src: (dest, dist)
edges: dict[str, tuple[str, float]] = {}
# read graph edges from file
with open("graph.txt") as g:
    for line in g:
        start, finish, dist = line.split()
        dist = float(dist)
        if start not in edges:
            edges[start] = []
        edges[start].append((finish, dist))
        if finish not in edges:
            edges[finish] = []
        edges[finish].append((start, dist))

for e in edges:
    print(e, edges[e])

# distances of cities from the start
#            city: (distance, prev_city)
distances = {"Sopron": (0, "")}
start = "Sopron"
# list of (dist, city) pairs
open_nodes = [(0, "Sopron")]
# set of cities with known (proven) distances
completed = set()
while open_nodes:
    # sort by dist
    open_nodes.sort()
    # go to closest unvisited city
    prev_dist, city = open_nodes[0]
    open_nodes.pop(0)
    for e in edges[city]:
        newcity, dist = e
        newdist = prev_dist + dist
        if newcity not in distances or distances[newcity][0] > newdist:
            # found a new shortest path to newcity
            distances[newcity] = (newdist, city)
        if newcity not in completed:
            open_nodes.append((newdist, newcity))
    completed.add(city)

import pprint
pp = pprint.PrettyPrinter()
pp.pprint(distances)

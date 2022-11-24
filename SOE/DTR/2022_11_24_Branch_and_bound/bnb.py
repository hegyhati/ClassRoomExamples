# Shortest path search with branch-and-bound and Euclidean distances

import pprint
pp = pprint.PrettyPrinter()

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
pp.pprint(edges)

# Euclidean distances from target
#            city: Euclidean distance to Bp
BP_dist: dict[str, float] = {}
with open("BP_dist.txt") as f:
    for line in f:
        city, dist = line.split()
        dist = float(dist)
        BP_dist[city] = dist
pp.pprint(BP_dist)

def path_length(path: list[str]) -> float:
    path_dist = 0.0
    for i in range(1, len(path)):
        # path_dist += dist_mtx[path[i-1]][path[i]]
        for e in edges[path[i-1]]:
            if e[0] == path[i]:
                path_dist += e[1]
                break
    return path_dist

# list of (bound, path) pairs
# path is a list of cities, a partial solution
open_nodes = [(0+BP_dist["Sopron"], ["Sopron"])]
# objective value of best found solution
best = float("inf")
# path representation of best found solution
best_sol = None
while open_nodes:
    # sort by bound
    open_nodes.sort()
    # get partial solution with lowest bound
    bound, path = open_nodes[0]
    print("  ", bound, path)
    open_nodes.pop(0)
    if bound >= best:
        # partial solution is suboptimal
        print("  stop")
        continue
    path_dist = path_length(path)
    city = path[-1]  # last city on the path
    if city == "Budapest":
        # we found a complete solution
        if best_sol is None or path_dist < best:
            # better than the previous best solution
            best_sol = path
            best = path_dist
    else:
        # we haven't reached our destination
        for e in edges[city]:
            newcity, dist = e
            if newcity not in path:
                newbound = path_dist + dist + BP_dist[newcity]
                open_nodes.append((newbound, path+[newcity]))

if best_sol:
    print("Optimal solution:", best, best_sol)
else:
    print("Destination cannot be reached.")
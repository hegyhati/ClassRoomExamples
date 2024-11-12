map = """111111111111
100000000001
111111111111
111111100001
111111000001
111111111101
100001111111
111111111111"""

map = [
    [
        int(c) for c in line.strip()
    ]
    for line in map.split("\n")
]

zeros = {
    (r,c)
    for r in range(len(map))
    for c in range(len(map[0]))
    if map[r][c]==0
}

print(len(zeros), zeros)

while len(zeros) != 0:
    (r,c) = list(zeros)[0]

    to_explore = {(r,c)}
    cluster = set()
    while len(to_explore) != 0:
        (r,c) = to_explore.pop()
        cluster.add((r,c))
        to_explore.update({(r-1,c),(r+1,c),(r,c-1),(r,c+1)}.intersection(zeros).difference(cluster))

    print("Cluster", len(cluster), cluster)
    zeros.difference_update(cluster)



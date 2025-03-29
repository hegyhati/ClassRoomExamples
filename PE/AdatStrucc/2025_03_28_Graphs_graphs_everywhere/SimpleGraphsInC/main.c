#include "graph.h"
#include "stdio.h"
#include "time.h"

void testRandomGraph() {
    AdjacencyListGraph graph = randomGraph(10, 15);
    printGraph(graph);
    freeGraph(&graph);
}

void testDistance() {
    AdjacencyListGraph graph = circleGraph(10);
    unsigned v = rand() % 10;
    for (unsigned u = 0; u < 10; ++u)
        printf("Distance of %d from %d in C_10: %d.\n", u, v, distance(graph, u, v));
    freeGraph(&graph);
}

void testDFSTree() {
    AdjacencyListGraph graph = completeBipartiteGraph(5,2);
    unsigned v = rand() % 5;
    AdjacencyListGraph tree = dfsTree(graph,v);
    printGraph(graph);
    printf("DFS tree root: %d\n", v);
    printGraph(tree);
    freeGraph(&graph);
    freeGraph(&tree);
}

int main() {
    srand(time(NULL));

    testDFSTree();

    return 0;
}
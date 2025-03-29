#ifndef GRAPH_H
#define GRAPH_H

#include "stdlib.h"
#include "uint_list.h"

typedef struct AdjacencyListGraph {
    unsigned vertex_count;
    LLNode **neighbor_list;
} AdjacencyListGraph;



AdjacencyListGraph newGraph(unsigned size);
void freeGraph(AdjacencyListGraph *pgraph);
bool hasEdge(AdjacencyListGraph graph, unsigned v1, unsigned v2);
bool addEdge(AdjacencyListGraph graph, unsigned v1, unsigned v2);

void printGraph(AdjacencyListGraph graph);

AdjacencyListGraph emptyGraph(unsigned size);
AdjacencyListGraph lineGraph(unsigned size);
AdjacencyListGraph circleGraph(unsigned size);
AdjacencyListGraph completeGraph(unsigned size);
AdjacencyListGraph completeBipartiteGraph(unsigned size1, unsigned size2);
AdjacencyListGraph randomGraph(unsigned size, unsigned edgecount);

unsigned distance(AdjacencyListGraph graph, unsigned v1, unsigned v2);
AdjacencyListGraph dfsTree(AdjacencyListGraph graph, unsigned v);

#endif
#include "graph.h"
#include "stdio.h"

AdjacencyListGraph newGraph(unsigned size) {
    AdjacencyListGraph graph;
    graph.vertex_count = size;
    graph.neighbor_list = (LLNode **)malloc(size * sizeof(LLNode *));
    for (unsigned v = 0; v < graph.vertex_count; ++v)
        graph.neighbor_list[v] = NULL;
    return graph;
}

void freeGraph(AdjacencyListGraph *pgraph) {
    for (unsigned v = 0; v < pgraph->vertex_count; ++v)
        freeList(pgraph->neighbor_list + v);
    free(pgraph->neighbor_list);
    pgraph->vertex_count = 0;
}

bool hasEdge(AdjacencyListGraph graph, unsigned v1, unsigned v2) {
    if (v1 >= graph.vertex_count || v2 >= graph.vertex_count || v1 == v2) return false;
    return hasItem(graph.neighbor_list[v1], v2);
}

bool addEdge(AdjacencyListGraph graph, unsigned v1, unsigned v2) {
    if (v1 >= graph.vertex_count || v2 >= graph.vertex_count || v1 == v2) return false;
    if (!addItem(graph.neighbor_list + v1, v2, true)) return false;
    addItem(graph.neighbor_list + v2, v1, false);
    return true;
}

void printGraph(AdjacencyListGraph graph) {
    printf("( { 0..%d }, { ", graph.vertex_count);
    for (unsigned v = 0; v < graph.vertex_count; ++v)
        for (LLNode *u = graph.neighbor_list[v]; u != NULL; u = u->next)
            if (v < u->item) printf("%d-%d ", v, u->item);
    printf("} )\n");
}

AdjacencyListGraph emptyGraph(unsigned size) { return newGraph(size); }

AdjacencyListGraph lineGraph(unsigned size) {
    AdjacencyListGraph graph = emptyGraph(size);
    for (unsigned v = 1; v < size; ++v)
        addEdge(graph, v - 1, v);
    return graph;
}

AdjacencyListGraph circleGraph(unsigned size) {
    AdjacencyListGraph graph = lineGraph(size);
    addEdge(graph, 0, size - 1);
    return graph;
}

AdjacencyListGraph completeGraph(unsigned size) {
    AdjacencyListGraph graph = emptyGraph(size);
    for (unsigned v = 0; v < size; ++v)
        for (unsigned u = v + 1; u < size; ++u)
            addEdge(graph, u, v);
    return graph;
}

AdjacencyListGraph completeBipartiteGraph(unsigned size1, unsigned size2) {
    AdjacencyListGraph graph = emptyGraph(size1 + size2);
    for (unsigned v = 0; v < size1; ++v)
        for (unsigned u = size1; u < size1 + size2; ++u)
            addEdge(graph, v, u);
    return graph;
}

AdjacencyListGraph randomGraph(unsigned size, unsigned edgecount) {
    if (edgecount >= size * (size - 1) / 2) return completeGraph(size);
    AdjacencyListGraph graph = emptyGraph(size);
    unsigned v1, v2;
    while (edgecount > 0) {
      v1 = rand() % size, v2 = rand() % size;
      if (addEdge(graph, v1, v2)) --edgecount;
    }
    return graph;
}

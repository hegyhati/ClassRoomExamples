#include "graph.h"
#include "stdio.h"
#include "time.h"

int main() {
  srand(time(NULL));
  AdjacencyListGraph graph = randomGraph(10, 15);
  printGraph(graph);
  freeGraph(&graph);
  return 0;
}
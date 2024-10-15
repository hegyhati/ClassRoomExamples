import sys
from graph import Graph

def is_connected_dfs_recursive(g:Graph, v1:str, v2:str) -> bool:
    
    class FoundItException(Exception):
        pass
  
    visited = {}
    
    def find_vertex(source:str, target:str, depth=0) -> None:
        if source == target: raise FoundItException("Yeppee")
        for neighbor in g.neighbors(source):
            if neighbor not in visited:
                visited[neighbor] = source
                find_vertex(neighbor,target, depth+1)
            
    try:
        visited[v1] = None
        find_vertex(v1,v2)
    except FoundItException as e:
        current = v2
        while current != v1:
            print(current)
            current = visited[current]
        print(v1)
        return True
    return False


g = Graph.load_from_file(sys.argv[1])
print(is_connected_dfs_recursive(g,sys.argv[2],sys.argv[3]))
        
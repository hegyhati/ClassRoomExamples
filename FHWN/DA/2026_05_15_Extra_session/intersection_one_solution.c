#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char iname[16];

typedef struct {
    iname name;                              
    int car;                                    
    int bike;                                   
    int pedestrian;                             
} Intersection;

typedef struct {
    Intersection* intersections;                
    int intersection_count;                     
    float** connections;                        
} Map;

int get_idx(Map m, iname name) {
    for (int i=0; i<m.intersection_count; ++i)
        if (strcmp(m.intersections[i].name,name)==0)
            return i;
    return -1;
}

Map load_data_from_file(const char *filename) {
    Map m;
    FILE* f = fopen(filename, "r");
    fscanf(f, "%d", &m.intersection_count);
    m.intersections = malloc(m.intersection_count*sizeof(Intersection));
    m.connections = malloc(m.intersection_count * sizeof(float*));
    for (int i=0; i<m.intersection_count; ++i) {
        m.connections[i] = malloc(m.intersection_count * sizeof(float));
        for (int j = 0; j<m.intersection_count; ++j)
            m.connections[i][j] = -1.0;
    }
    for (int i=0; i<m.intersection_count; ++i)
        fscanf(f,
            "%s Cars: %d Bikes: %d Pedestrians: %d",
            m.intersections[i].name,
            &m.intersections[i].car,
            &m.intersections[i].bike,
            &m.intersections[i].pedestrian
        );
    iname name1, name2;
    float distance;
    while (fscanf(f,"%s - %s : %f km", name1, name2, &distance) == 3){
        int idx1 = get_idx(m,name1);
        int idx2 = get_idx(m,name2);
        m.connections[idx1][idx2] = distance;
        m.connections[idx2][idx1] = distance;
    }
    fclose(f);
    return m;
}

void free_map(Map* pm) {
    for (int i=0; i<pm->intersection_count; ++i)
        free(pm->connections[i]);
    free(pm->connections);
    free(pm->intersections);
    pm->intersection_count = 0;
    pm->connections = NULL;
    pm->intersections = NULL;
}

void debug_map(Map m) {
    printf("Intersections:\n");
    for (int i=0; i<m.intersection_count; ++i)
        printf(" - Daily traffic for %s: %d cars, %d bikes, %d pedestrians\n",
            m.intersections[i].name,
            m.intersections[i].car,
            m.intersections[i].bike,
            m.intersections[i].pedestrian
        );
    printf("Connections:\n");
    for (int i=0; i<m.intersection_count; ++i)
        for (int j=i+1; j<m.intersection_count; ++j)
            if (m.connections[i][j] > 0)
                printf(" - %g km between %s and %s\n",
                    m.connections[i][j],
                    m.intersections[i].name,
                    m.intersections[j].name
                );
}

int main(){
    Map map = load_data_from_file("intersection.txt");
    debug_map(map);
    free_map(&map);
}
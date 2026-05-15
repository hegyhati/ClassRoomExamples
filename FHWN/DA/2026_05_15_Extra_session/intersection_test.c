#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char iname[16];

typedef struct {
    /* TODO: store all data about an intersection */                          
} Intersection;

typedef struct {
    /* TODO: Store all intersection & connection data */                            
} Map;

Map load_data_from_file(const char *filename) {
    Map m;

    /* Puffer variables for reading */

    int i1,i2,i3,i4;
    iname s1,s2;
    float f1;

    /* Reading the data from the file */

    FILE* f = fopen(filename, "r");
    fscanf(f, "%d", &i1); // Reading the number of intersections
    /* TODO */
    for (int i=0; i<i1; ++i) {
        // Reading data for one intersection
        fscanf(f,"%s Cars: %d Bikes: %d Pedestrians: %d",s1,&i2,&i3,&i4);
        /* TODO */
    }
    // Reading connections data
    while (fscanf(f,"%s - %s : %f km", s1, s2, &f1) == 3){
        /* TODO */
    }
    fclose(f);
    return m;
}

void free_map(Map* pm) {
    /* TODO: free up memory allocated on the heap, set pointers to NULL */
}

void debug_map(Map m) {
    /* TODO: print out data for debugging */
}

int main(){
    Map map = load_data_from_file("intersection.txt");
    debug_map(map);
    free_map(&map);
}
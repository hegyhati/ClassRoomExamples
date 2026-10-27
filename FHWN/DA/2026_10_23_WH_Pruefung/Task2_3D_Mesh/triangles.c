#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    float x;
    float y;
    float z;
} Point;

typedef Point Triangle[3];

typedef struct {
    // TODO
} Mesh;

float distance_PP(const Point p1, const Point p2) {
    return sqrtf(
        (p1.x-p2.x) * (p1.x-p2.x) +
        (p1.y-p2.y) * (p1.y-p2.y) +
        (p1.z-p2.z) * (p1.z-p2.z)
    );
}

float distance_PT(const Point p, const Triangle t) {
    return fminf(fminf(distance_PP(p,t[0]), distance_PP(p,t[1])),distance_PP(p,t[2]));
}

Mesh load_mesh(const char* filename) {
    // TODO
    size_t c;
    float x,y,z;
    FILE* f = fopen(filename, "r");
    fscanf(f, "%lu", &c);
    for(size_t i=0; i<c; ++i)
        for(size_t p=0; p<3; ++p)
            fscanf(f, "%f %f %f", &x, &y, &z);
    fclose(f);
}

void free_mesh(Mesh* pmesh) {
    // TODO
}

void save_to_file(const Mesh mesh, const char* filename) {
    FILE* f = fopen(filename, "w");
    fprintf(f, "%lu\n", 0 /* number of triangles here*/);
    
    /* for all triangles */
    fprintf(f, "%.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f \n", 
        1,2,3,4,5,6,7,8,9 /* the actual coordinates of the triangle*/)
        
    fclose(f);
}

Mesh closest_triangles(const Mesh mesh, const Point p, const size_t count) {
   // TODO
}


int main() {
    Mesh mesh = load_mesh("bunny.txt");
    save_to_file(mesh, "test_bunny_copy.txt"); // should be identical to bunny.txt

    Point players[2] = {
        {1.0, 1.0, 1.0},
        {-1.0, -1.0, -1.0}
    };
    int count[7] = {1, 5, 10, 100, 1000, 10000, 100000};
    char filename[64];
    
    for (int p = 0; p < 2; ++p) { 
        for (int c = 0; c < 7; ++c) {
            printf("Player %d, Count %d\n", p+1, count[c]);
            Mesh closest = closest_triangles(mesh, players[p], count[c]);            
            snprintf(filename, sizeof(filename), "player_%d_count_%d.mesh", p + 1, count[c]);
            save_to_file(closest, filename);
            free_mesh(&closest);
        }
    }

    free_mesh(&mesh);
    return 0;
}

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
    size_t count;
    Triangle* triangles;
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
    Mesh m;
    FILE* f = fopen(filename, "r");
    fscanf(f, "%lu", &m.count);
    m.triangles = (Triangle*) malloc (m.count * sizeof(Triangle));
    for(size_t i=0; i<m.count; ++i)
        for(size_t p=0; p<3; ++p)
            fscanf(f, "%f %f %f", &m.triangles[i][p].x, &m.triangles[i][p].y, &m.triangles[i][p].z);
    fclose(f);
    return m;
}

void free_mesh(Mesh* pmesh) {
    pmesh->count = 0;
    free(pmesh->triangles);
    pmesh->triangles = NULL;
}

void swap(Mesh mesh, size_t idx1, size_t idx2) {
    Triangle tmp;
    memcpy(&tmp, mesh.triangles + idx1, sizeof(Triangle));
    memcpy(mesh.triangles + idx1, mesh.triangles + idx2, sizeof(Triangle));
    memcpy(mesh.triangles + idx2, &tmp, sizeof(Triangle));
}

size_t partition(const Point p, Mesh mesh, size_t from, size_t until) {
    swap(mesh, (from + until-1) / 2, until-1);
    const float pivot_distance = distance_PT(p,mesh.triangles[until-1]);
    size_t first_larger = from;
    for (size_t i = from; i<until-1; ++i) {
        if ( distance_PT(p,mesh.triangles[i]) < pivot_distance ) 
            swap(mesh,i,first_larger++);
    }
    swap(mesh, first_larger, until-1);
    return first_larger;
}

void quick_sort_left_k(const Point p, Mesh mesh, const size_t from, const size_t until, const size_t k) {
    if (until <= from ) return; 
    const size_t pivot = partition(p, mesh, from, until);
    if ( pivot < k - 1) quick_sort_left_k(p, mesh, pivot+1, until, k);
    else if (pivot > k) quick_sort_left_k(p, mesh, from, pivot, k);
}

Mesh closest_triangles(const Mesh mesh, const Point p, const size_t count) {
    if (count >= mesh.count) count = mesh.count;
    Mesh closest; 
    closest.count = count;
    closest.triangles = (Triangle*) malloc (closest.count * sizeof(Triangle));
    Mesh copy;
    copy.count = mesh.count;
    copy.triangles = (Triangle*) malloc (copy.count * sizeof(Triangle));
    memcpy(copy.triangles, mesh.triangles, copy.count*sizeof(Triangle));
    
    quick_sort_left_k(p, copy, 0, copy.count, count);

    memcpy(closest.triangles, copy.triangles, closest.count*sizeof(Triangle));
    free_mesh(&copy);
    return closest;
}

void save_to_file(const Mesh mesh, const char* filename) {
    FILE* f = fopen(filename, "w");
    fprintf(f, "%lu\n", mesh.count);
    for (size_t i=0; i<mesh.count; ++i) {
        for(size_t p=0; p<3; ++p)
            fprintf(f, "%.6f %.6f %.6f ", mesh.triangles[i][p].x, mesh.triangles[i][p].y, mesh.triangles[i][p].z);
        fprintf(f, "\n");
    }        
    fclose(f);
}


int main() {
    Mesh mesh = load_mesh("bunny.txt");
    save_to_file(mesh, "test_bunny_copy.txt");

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

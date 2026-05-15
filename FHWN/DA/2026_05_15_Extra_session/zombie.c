#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define M_PI 3.14159265358979323846

typedef struct {
    float x,y;
    float step_length;
    int hp;
} Zombie;

void print_zombie(Zombie z){
    printf("(%6.2f,%6.2f) %6s - [%3d]", z.x, z.y, z.hp>=1 ? "Alive" : "Dead",z.hp);
}

float rand_float(float max) {
    return 2 * max * ((float)rand()/RAND_MAX) - max;
}

Zombie random_zombie() {
    Zombie z;
    z.x = rand_float(50);
    z.y = rand_float(50);
    z.step_length = rand_float(10);
    z.hp = rand()%20+1;
    return z;
}

float distance(Zombie z) {
    return sqrtf(z.x*z.x + z.y*z.y);
}

void move(Zombie *pz) {
    float angle = rand_float(M_PI);
    float dx = pz->step_length * cosf(angle);
    float dy = pz->step_length * sinf(angle);
    float dist = distance(*pz);
    pz->x += dx;
    pz->y += dy;
    float new_dist = distance(*pz);
    if (new_dist > dist) {
        pz->x -= dx;
        pz->y -= dy;
    }
}


Zombie* spawn_zombies(int count){
    Zombie* zombies = malloc(count*sizeof(Zombie));
    for(int i=0;i<count;++i)
    zombies[i] = random_zombie();
    return zombies;
}

void print_zombies(Zombie* zombies, int size) {
    for(int i=0;i<size;++i) {
        print_zombie(zombies[i]);
        printf(" -- Distance: %7.2f\n", distance(zombies[i]));
    }
}

bool am_i_alive(Zombie* zombies, int count) {
    for(int i=0;i<count;++i) 
        if (distance(zombies[i]) <= 1.0)
            return false;
    return true;
}

bool is_one_zombie_alive(Zombie* zombies, int count) {
    for(int i=0;i<count;++i) 
        if (zombies[i].hp > 0)
            return true;
    return false;
}

void swap(Zombie* zombies, int idx1, int idx2) {
    Zombie tmp = zombies[idx1];
    zombies[idx1] = zombies[idx2];
    zombies[idx2] = tmp;
}

void heapify(int heapsize, Zombie* zombies, int parent) {
    while (1) {
        int closest_idx = parent;
        int left = 2 * parent + 1;
        int right = 2 * parent + 2;
        if (left < heapsize && distance(zombies[left]) < distance(zombies[closest_idx])) closest_idx = left;
        if (right < heapsize && distance(zombies[right]) < distance(zombies[closest_idx])) closest_idx = right;
        if (closest_idx != parent) {
            swap(zombies, parent, closest_idx);
            parent = closest_idx;
        } else break;
    }
}

void build_heap(int heapsize, Zombie* zombies) {
    for (int i=heapsize/2-1; i>=0; --i) 
        heapify(heapsize, zombies, i);
}

void promote(int heapsize, Zombie* zombies, int idx) {
    while (true) {
        if (idx == 0) break;
        int parent = (idx-1)/2;
        if (distance(zombies[idx]) >= distance(zombies[parent])) break;
        swap(zombies, parent, idx);
        idx = parent;
    }
}

int main(int argc, char** argv) {
    int count = atoi(argv[1]);
    int alive_count = count;
    Zombie* z = spawn_zombies(count);
    build_heap(alive_count, z);

    int round = 0;
    while (true) {
        printf("\n\n ==== ROUND %2d ==== \n\n", ++round);
        print_zombies(z,count);

        
        if (!am_i_alive(z,alive_count)) {
            printf("\n\n :-( \n\n");
            break;
        }

        z[0].hp -= rand() % 3;
        if (z[0].hp <= 0) {
            swap(z,0,alive_count-1);
            --alive_count;
            heapify(alive_count, z, 0);
        }

        if (alive_count == 0) {
            printf("\n\nYEPPEEEEEE\n\n");
            print_zombies(z,count);
            break;
        }

        int zidx = rand() % alive_count;
        move(z+zidx);
        promote(alive_count, z, zidx);
    }

    free(z);
    return 0;
}
/*

Imagine the following simulation:

We are at position 0.0,0.0 being swarmed by zombies from all direction. 
Zombies have a position, a step-length, and luckily they are not really clever creatures, but hungry. 
They way they move is that they pick a random direction, then check if they would get closer to us or not. If not, they stay where they are, if they do, they make the step.

Luckily, we have an automatic cannon that shoots at the closest target, and it is powerful enough to one-shot a zombie.

The whole simulation happens in a turn-by-turn based manner:

 1) the cannon shoots at the closest zombie and one shots it
 2) a random zombie moves closer
 3) repeat until a zombie gets too close (within 1 meter) or all the zombies are killed

Aiming with a cannon is a time consuming procedure, so we don't want to delay this by using an O(n) algorithm for selecting the target. 
Thus, we should maintain the zombies in a heap. 

*/

typedef struct {
    float x;
    float y;
    float step_length;
    bool alive;
} Zombie;

Zombie spawn() {
    // todo - spawn a zombie with random position, stepsize, and alive
}

void move(Zombie* const zombie) {
    // todo
}

float distance(Zombie zombie) {
    // todo
}

void print(Zombie zombie) {
    // todo
}

typedef struct {
    Zombie* zombies;
    int heapsize; // alive zombies
} Zombie_Heap;

Zombie_Heap spawn_all(int zombie_count) {
    // todo
}

Zombie closest(Zombie_Heap) {
    // todo
}

void kill_closest(Zombie_Heap* p_zombies) {
    // todo
}

void move_random_zombie(Zombie_Heap zombies) {
    // todo
}

bool all_killed(Zombie_Heap zombies) {
    // todo
}

bool closest_too_close(Zombie_Heap zombies) {
    // todo
}

void deallocate(Zombie_Heap* p_zombies) {
    // todo
}


int main() {
    Zombie_Heap zombies = spawn_all(1000);

    while(true) {
        if (closest_too_close(zombies)) {
            printf("You died.\n");
            break;
        }
        printf("The following zombie is about to be shot: ");
        print(closest(zombies));
        kill_closest(&zombies);
        if (all_killed(zombies)) {
            printf("Clear, all zombies unalived.\n");
            break;
        }
        move_random_zombie(zombies);
    }

    deallocate(&zombies);
}


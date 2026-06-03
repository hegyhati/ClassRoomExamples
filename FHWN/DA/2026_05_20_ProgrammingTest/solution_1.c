/*

Note: did it while planning what the test actually will be, so some solutions may seem awkward, as this was "refactored" couple of times. Also, not tested thoroughly.

*/


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef char string[32];

typedef struct {
    string name;
    int age;
    string breed;    
} Dog;

typedef struct {
    int count;
    Dog* dogs;
} DogList;

typedef struct {
    int size;
    bool* conflict;
} Conflicts;

int idx(DogList dl, string name) {
    for (int i=0; i<dl.count; ++i)
        if (strcmp(dl.dogs[i].name, name)==0)
            return i;
    return -1;
}

DogList load_dog_data(const char* dogfile) {
    DogList dl;
    FILE* f = fopen(dogfile, "r");
    fscanf(f," Number of dogs: %d ", &dl.count);
    dl.dogs = malloc(dl.count * sizeof(Dog));
    for (int i=0; i<dl.count; ++i)
        fscanf(f," Name: %s Age: %d Breed: %s ",
            dl.dogs[i].name,
            &dl.dogs[i].age,
            dl.dogs[i].breed
        );
    fclose(f);
    return dl;
}

void free_dog_data(DogList* pdl) {
    free(pdl->dogs);
    pdl->count = 0;
    pdl->dogs = NULL;
}

void debug_dog_list(DogList dl){
    for (int i=0; i<dl.count; ++i)
        printf("%20s - %d - %s\n", dl.dogs[i].name, dl.dogs[i].age, dl.dogs[i].breed);
}

void swap_dogs(DogList dl, int idx1, int idx2){
    Dog tmp = dl.dogs[idx1];
    dl.dogs[idx1] = dl.dogs[idx2];
    dl.dogs[idx2] = tmp;
}


void sort_by_name(DogList dl) {
    for(int i=1; i<dl.count; ++i)
        for(int j=i; j>0 && strcmp(dl.dogs[j].name,dl.dogs[j-1].name) < 0; --j)
            swap_dogs(dl,j,j-1);
}

void merge(Dog* start, int count1, int count2, Dog* puffer){
    int i1=0, i2=count1;
    for (int i=0; i<count1+count2; ++i) {
        if (i1==count1) puffer[i] = start[i2++];
        else if (i2==count1+count2) puffer[i] = start[i1++];
        else if (start[i1].age <= start[i2].age) puffer[i] = start[i1++];
        else puffer[i] = start[i2++];
    }
    for (int i=0; i<count1+count2; ++i)
        start[i] = puffer[i];
}

void sort_by_age(DogList dl) {
    Dog* puffer = malloc(dl.count * sizeof(Dog));
    for (int step=1; step < dl.count; step*=2) 
        for (int idx = 0; idx < dl.count-step; idx += 2*step)
            merge(dl.dogs+idx,step,idx+2*step<dl.count ? step : dl.count - idx - step, puffer);
    free(puffer);
}

void sort_by_age_then_by_name(DogList dl) {
    sort_by_name(dl);
    sort_by_age(dl);
}

Conflicts load_conflict_data(DogList dl, const char* logfile) {
    Conflicts c;
    c.size = dl.count;
    c.conflict = malloc(c.size * c.size * sizeof(bool));
    for (int i=0; i<c.size*c.size; ++i) c.conflict[i] = false;
    for (int d1=0; d1<dl.count; ++d1)
        for (int d2=d1+1; d2<dl.count; ++d2)
            if (strcmp(dl.dogs[d1].breed,dl.dogs[d2].breed)==0) 
                c.conflict[d1*c.size+d2] = c.conflict[d2*c.size+d1] = true;
    FILE* f = fopen(logfile, "r");
    string name1, name2;
    while(2==fscanf(f," %*s %s attacked %s ", name1, name2)) {
        int d1 = idx(dl,name1);
        int d2 = idx(dl,name2);
        c.conflict[d1*c.size+d2] = c.conflict[d2*c.size+d1] = true;
    }
    fclose(f);
    return c;
}

void free_conflicts_data(Conflicts* pc) {
    free(pc->conflict);
    pc->conflict = NULL;
    pc->size = 0;
}

bool is_conflict(Conflicts c, int idx1, int idx2){
    return c.conflict[idx1*c.size+idx2];
}

int* initialize_array(int size, int value) {
    int* array = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        array[i] = value;
    return array;
}


int* kennels_simple_opennew(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    int current_kennel = 0;
    for (int i=0; i<c.size; ++i) {
        for (int j=0; j<i; ++j)
            if (is_conflict(c,i,j) && kennels[j] == current_kennel) {
                ++current_kennel;
                break;
            }
        kennels[i] = current_kennel;
    }
    return kennels;
}

int* kennels_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    for (int i=0; i<c.size; ++i) {
        for (int k=0; k<c.size; ++k) {
            bool ok = true;
            for (int j=0; j<i; ++j)
                if (is_conflict(c,i,j) && kennels[j] == k) {
                    ok = false;
                    break;                
                }
            if (ok) {
                kennels[i] = k;
                break;
            } 
        }
    }
    return kennels;
}

int* kennels_clever_first_fit(Conflicts c) {
    int* bad_others = initialize_array(c.size, 0);
    for (int d1=0; d1<c.size; ++d1)
        for (int d2=0; d2<c.size; ++d2)
            if (is_conflict(c,d1,d2))
                ++bad_others[d1];
    int* sorted = initialize_array(c.size, -1);
    int next_idx = c.size-1;
    while (next_idx >= 0) {
        int friendliest_idx = -1;
        for (int i=0; i<c.size; ++i) {
            if (sorted[i] == -1 && (friendliest_idx==-1 || bad_others[i]<bad_others[friendliest_idx]) ) 
                friendliest_idx = i;
        }
        sorted[friendliest_idx] = next_idx--;
        bad_others[friendliest_idx] = 0;
        for (int d=0; d<c.size; ++d)
            if (is_conflict(c,friendliest_idx,d))
                --bad_others[d];
    }
    free(bad_others);
    int* kennels = initialize_array(c.size, -1);
    for (int i=0; i<c.size; ++i) {
        for (int k=0; k<c.size; ++k) {
            bool ok = true;
            for (int j=0; j<i; ++j)
                if (is_conflict(c,sorted[i],sorted[j]) && kennels[sorted[j]] == k) {
                    ok = false;
                    break;                }
            if (ok) {
                kennels[sorted[i]] = k;
                break;
            }
        }
    }
    free(sorted);
    return kennels;
}

int kennel_count(int* kennels, int size) {
    int max = kennels[0];
    for (int i=1; i<size; ++i)
        if (kennels[i] > max)
            max = kennels[i];
    return max+1;
}


int main() {
    DogList dl = load_dog_data("dog_data.txt");
    debug_dog_list(dl);

    printf("\nSorted by age then by name:\n");
    sort_by_age_then_by_name(dl);
    debug_dog_list(dl);

    Conflicts c = load_conflict_data(dl,"incident_data.txt");

    int* kennels1 = kennels_simple_opennew(c);
    int* kennels2 = kennels_first_fit(c);
    int* kennels3 = kennels_clever_first_fit(c);


    printf("Kennel counts : %d / %d / %d \n", 
        kennel_count(kennels1,c.size),
        kennel_count(kennels2,c.size),
        kennel_count(kennels3,c.size)
    );

    free(kennels1);
    free(kennels2); 
    free(kennels3);

    free_conflicts_data(&c);
    free_dog_data(&dl);
} 


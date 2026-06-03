/*

"Live coded" version for a video. Again, not well tested.

*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>


int* initialize_array(int size, int value) {
    int* array = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        array[i] = value;
    return array;
}

typedef char string[32];

typedef struct {
    string name;
    int age;
    string breed;    
} Dog;

typedef struct {
    int dogcount;
    Dog* dogs;
} DogList;

int get_dog_count(DogList dl) { 
    return dl.dogcount;
}

DogList load_dog_data(const char* dogfile) {
    /* Buffer variables for reading */
    int bint1, bint2;
    string bstring1, bstring2;
    
    DogList dl;
    FILE* f = fopen(dogfile, "r");
    fscanf(f," Number of dogs: %d ", &bint1);
    dl.dogcount = bint1;
    dl.dogs = (Dog*) malloc(dl.dogcount * sizeof(Dog));
    for (int i=0; i<bint1; ++i) {
        fscanf(f," Name: %s Age: %d Breed: %s ",
            bstring1,
            &bint2,
            bstring2
        );
        strcpy(dl.dogs[i].name, bstring1);
        dl.dogs[i].age = bint2;
        strcpy(dl.dogs[i].breed,bstring2);
    }
    fclose(f);
    return dl;
}

void free_dog_data(DogList* pdl) {
    free(pdl->dogs);
    pdl->dogs = NULL;
    pdl->dogcount = 0;
}

void debug_dog_list(DogList dl){
    printf("Dogs:\n");
    for(int i=0; i < dl.dogcount; ++i)
        printf(" %3d. Age: %2d Name: %-20s Breed: %s\n",
            i,
            dl.dogs[i].age,
            dl.dogs[i].name,
            dl.dogs[i].breed
        );
}

int max_age(DogList dl){
    int max_age = dl.dogs[0].age;
    for (int i=0; i < dl.dogcount; ++i)
        if (dl.dogs[i].age > max_age)
            max_age = dl.dogs[i].age;
    return max_age;
}

void stable_sort_by_age(DogList dl) {
    int mage = max_age(dl)+1;
    int* count_array = initialize_array(mage,0);
    for (int i = 0; i < dl.dogcount; ++i)
        ++count_array[dl.dogs[i].age];
    int* first_index = initialize_array(mage,0);
    first_index[0]=0;
    for (int k = 1; k < mage; ++k)
        first_index[k] = first_index[k-1] + count_array[k-1];
    Dog* sorted = (Dog*) malloc (dl.dogcount * sizeof(Dog));
    for (int i = 0; i < dl.dogcount; ++i)        
        sorted[first_index[dl.dogs[i].age]++] = dl.dogs[i];
    for (int i = 0; i < dl.dogcount; ++i)     
        dl.dogs[i] = sorted[i];   
    free(count_array);
    free(first_index);
    free(sorted);
}

void swap_dogs(Dog* dogs, int idx1, int idx2){
    Dog tmp = dogs[idx1];
    dogs[idx1] = dogs[idx2];
    dogs[idx2] = tmp;
}

int partition(Dog* dogs, int first, int last){
    int maybe_smaller_idx = 0;
    int maybe_larger_idx = last-1;
    while (maybe_smaller_idx < maybe_larger_idx) {
        while(strcmp(dogs[maybe_smaller_idx].name,dogs[last].name) < 0) ++maybe_smaller_idx;
        while(strcmp(dogs[maybe_larger_idx].name,dogs[last].name) >= 0) --maybe_larger_idx;
        if (maybe_smaller_idx < maybe_larger_idx) swap_dogs(dogs,maybe_smaller_idx,maybe_larger_idx);
    }
    swap_dogs(dogs,last,maybe_smaller_idx);
    return maybe_smaller_idx;
}

void quick(Dog* dogs, int first, int last){
    if (last <= first) return;
    int pivot_idx = partition(dogs, first, last);
    quick(dogs, first, pivot_idx-1);
    quick(dogs, pivot_idx+1, last);
}

void stable_sort_by_name(DogList dl) {
   quick(dl.dogs, 0, dl.dogcount-1);     
}

void sort_by_age_then_by_name(DogList dl) {
    stable_sort_by_name(dl);
    stable_sort_by_age(dl);
}


typedef struct {
    int size;
    bool** ok;
} Conflicts;

int get_dog_index(DogList dl, string name) {
    for (int i = 0; i < dl.dogcount; ++i)
        if (strcmp(dl.dogs[i].name,name) == 0)
            return i;
    return -1;
}

Conflicts load_conflict_data(DogList dl, const char* logfile) {
    /* Buffer variables for reading */
    string bstring1, bstring2;

    Conflicts c;
    c.size = dl.dogcount;
    c.ok = (bool**) malloc(c.size * sizeof(bool*));
    for (int i = 0; i < c.size; ++i) {
        c.ok[i] = (bool*) malloc(c.size * sizeof(bool));
        for (int j = 0; j < c.size; ++j) 
            c.ok[i][j] = strcmp(dl.dogs[i].breed,dl.dogs[j].breed) != 0;
    }
    
    FILE* f = fopen(logfile, "r");
    while(2==fscanf(f," %*s %s attacked %s ", bstring1, bstring2)) {
        int i = get_dog_index(dl,bstring1);
        int j = get_dog_index(dl,bstring2);
        c.ok[i][j] = false;
        c.ok[j][i] = false;
    }
    fclose(f);
    return c;
}

void free_conflicts_data(Conflicts* pc) {
    for (int i = 0; i < pc->size; ++i) free(pc->ok[i]);
    free(pc->ok);
    pc->ok = NULL;
    pc->size = 0;
}

int* kennels_simple_opennew(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    int current_room = 0;
    kennels[0] = 0;
    for (int i=1; i < c.size; ++i) {
        bool ok_in_current_room = true;
        for (int j=0; j < i; ++j)
            if (kennels[j] == current_room && !c.ok[i][j])
                ok_in_current_room = false;
        if (ok_in_current_room) {
            kennels[i] = current_room;
        } else {
            kennels[i] = ++current_room;
        }
    }
    return kennels;
}

int* kennels_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}

int* kennels_clever_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
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
        kennel_count(kennels1, get_dog_count(dl)),
        kennel_count(kennels2, get_dog_count(dl)),
        kennel_count(kennels3, get_dog_count(dl))
    );

    free(kennels1);
    free(kennels2); 
    free(kennels3);

    free_conflicts_data(&c);
    free_dog_data(&dl);
} 


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
    // TODO
} DogList;

int get_dog_count(DogList dl) { 
    /* TODO */
}

DogList load_dog_data(const char* dogfile) {
    /* Buffer variables for reading */
    int bint1, bint2;
    string bstring1, bstring2;
    
    DogList dl;
    FILE* f = fopen(dogfile, "r");
    fscanf(f," Number of dogs: %d ", &bint1);
    // TODO
    for (int i=0; i<bint1; ++i) {
        fscanf(f," Name: %s Age: %d Breed: %s ",
            bstring1,
            &bint2,
            bstring2
        );
        // TODO
    }
    fclose(f);
    return dl;
}

void free_dog_data(DogList* pdl) {
    // TODO
}



void debug_dog_list(DogList dl){
    // TODO
}

void sort_by_age_then_by_name(DogList dl) {
    // TODO
}


typedef struct {
    // TODO
} Conflicts;

Conflicts load_conflict_data(DogList dl, const char* logfile) {
    /* Buffer variables for reading */
    string bstring1, bstring2;

    Conflicts c;
    // TODO
    
    FILE* f = fopen(logfile, "r");
    while(2==fscanf(f," %*s %s attacked %s ", bstring1, bstring2)) {
        // TODO
    }
    fclose(f);
    return c;
}

void free_conflicts_data(Conflicts* pc) {
    // TODO
}


int* initialize_array(int size, int value) {
    int* array = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        array[i] = value;
    return array;
}


int* kennels_simple_opennew(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
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


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define uint unsigned int

void swap(uint *a, uint *b){
    uint tmp = *a;
    *a = *b;
    *b = tmp;
}

struct array{
    uint size;
    uint *values;
};

int load_array_from_file(const char *filename, struct array * const dest) {
    FILE* file = fopen(filename,"r");
    if (file==NULL) {
        printf("File %s does not exist.\n",filename);
        return 1;
    }
    fscanf(file,"%d",&(dest->size));
    dest->values = (uint*) malloc(dest->size * sizeof(uint));
    for(uint i=0 ; i < dest->size ; ++i) 
        fscanf(file,"%d",(dest->values)+i);
    fclose(file);
    return 0;
}

void delete_array(struct array* todelete) {
    if (todelete->size) {
        free(todelete->values);
        todelete->size = 0;
    }
}

void insertion_sort_inplace(struct array data) {
    for ( uint next=1 ; next < data.size ; ++next) 
        for ( uint find=next ; find > 0 && data.values[find-1]>data.values[find] ; --find )
            swap(data.values+find, data.values+find-1);
}

void debug_print(const struct array data){
    for (uint i = 0 ; i < data.size ; ++i) 
        printf(" %d", data.values[i]);
    printf("\n");
}

void print_time(const clock_t ticks){
    const long int seconds = ticks / CLOCKS_PER_SEC;
    printf("%ld h %ld min %ld s %ld ms \n", seconds%3600, (seconds/60)%60, seconds%60, 1000*ticks/CLOCKS_PER_SEC%1000);
}

void report_result(const char *testcase, const clock_t ticks) {
    FILE* results = fopen("results.csv","a");
    fprintf(results, "%s,%ld\n", testcase, ticks);
    fclose(results);
}

int main(const int argc, const char** argv) {
    uint debug = 0;
    if (argc < 2) {
        printf("Provide a file containing an array to sort\n");
        return 1;
    } else if (argc >= 3 && !strcmp(argv[2], "-v")) {
        debug = 1;
    }
    
    struct array data;
    if (load_array_from_file(argv[1], &data)) return 1;
    
    if (debug) debug_print(data);
    clock_t start = clock();
    insertion_sort_inplace(data);
    clock_t end = clock();
    if (debug) {
        printf("\n\nSorted:\n"); 
        debug_print(data);
        printf("\n");
        print_time(end-start);
        printf("\n");
    }
    delete_array(&data);

    report_result(argv[1],end-start);

    return 0;
}
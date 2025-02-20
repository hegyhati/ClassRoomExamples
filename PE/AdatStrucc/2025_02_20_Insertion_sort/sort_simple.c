#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void insertion_sort_inplace(int size, int *values) {
    for ( int next=1 ; next < size ; ++next) 
        for ( int find=next ; find > 0 && values[find-1]>values[find] ; --find )
            swap(values+find, values+find-1);
}

int main(int argc, char** argv) {
    FILE* file = fopen(argv[1],"r");    

    int size;
    fscanf(file,"%d",&size);
    int *data = (int*) malloc(size*sizeof(int));
    for(int i=0 ; i < size ; ++i) 
        fscanf(file,"%d",data+i);
    fclose(file);
    

    clock_t start, end;
    start = clock();
    insertion_sort_inplace(size,data);
    end = clock();
    free(data);

    printf("Ticks: %ld\n", end-start);

    return 0;
}
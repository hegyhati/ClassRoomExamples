# General rules

 - Time available: 8:30-10:30
 - Leaving the room = submission.
 - No external resources allowed.
 - Copying from others results in immediate 0 points.
 - Code doesn't compile: 0 points.
 - Code segfaults: 0 points.
 - Code leaks memory: points halved.
 - Not all tasks need to be solved, you can select the tasks on which you focus. See below.
 - Work in the `test.c` file only, and only submit that by the end to moodle.
 - `main` cannot be changed, you need to provide placeholders to satisfy the above criteria for functions that you don't implement correctly.
 - Read the descriptions carefully, it is better to ask questions and clarify if something is not fully understood.
 - If you see a typo/mistake, let us know immediately. If it is so, we will broadcast it to everyone.

# Dog shelter

We are the IT guys at a dog shelter, and have to carry out several tasks that has been asked from us.

## The "database"

We have two files that contain information about the dogs and previous incidents.

### `dog_data.txt`

The file follows this structure and contains the name, age, and breed for each dog in our shelter.

```
Number of dogs: 123
Name: Peppy_Sadie Age: 2 Breed: Australian_Cattle_Dog
Name: Jolly_Athena Age: 3 Breed: Boston_Terrier
Name: Noisy_Winston Age: 8 Breed: Brittany
Name: Grouchy_Archie Age: 3 Breed: Cocker_Spaniel
Name: Bouncy_Annie Age: 7 Breed: Rottweiler
...
```

### `incident_data.txt`

While dogs are the best, unfortunately they don't always like each other, and some disagreements may happen while volunteers take them for their daily walk. 
This file contains log of those events in this format:
```
2025-01-01: Mellow_Ellie attacked Tiny_Tank
2025-01-04: Rowdy_Chloe attacked Wacky_Callie
2025-01-07: Grumpy_Josie attacked Mighty_Lucky
2025-03-01: Snuggly_Lola attacked Curious_Otis
2025-04-05: Grumpy_Zeus attacked Tiny_Zeus
...
```

### Other inputs

Feel free to change the size / content of the input if it helps you debugging, and you can use `python3 generate.py` to generate new input files of arbitrary (up to 5000 dogs) size.

## Tasks

### Ordered list of dogs 

Most people prefer younger dogs when planning to adopt. 
So we were asked to provide the list of dogs sorted by age. 
There are plenty of dogs with the same age, so for usability reasons, the dogs should be ordered by name within the same age group.

### Larger kennels

Currently, each dog is accommodated in a very small individual kennel. 
It would be nicer to provide them more room to run around, but due to space limitations, that is only possible if we can put several dogs together in larger kennels. 

Naturally, we don't want any fights, and in order to maximize the area per kennel, we want to minimize the number of kennels.
Our job is to cleverly sort the dogs into kennels, in such a way, that 2 dogs cannot be in the same kennel, if one of them attacked the other at any time before. 
We also do not want to put two dogs of the same breed into one kennel. (So that if we say "The Labraor from kennel 3" we know exactly which dog we talk about.)


## The code, and points

### Skeleton, libraries, others

 - Use the provided [`test.c`](test.c) file as a skeleton.
 - The `main` function should not be modified **AT ALL**. 
 - If you don't solve part of the test, just make the function stubs behave so that the code compiles and doesn't leak memory.
 - Feel free to add any further functions, or use any function from the standard C library. 
 - Don't use any macros, and work in a single file. (And only upload that file to moodle by the end.)

These libraries will be needed: 

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

All strings (names of dogs) are less than 31 characters long, so feel free to use this type:

```c
typedef char string[32];
```

For comparing strings, the built in `strcmp` function can be used.  Manpage for it:

```
strcmp(3)                   Library Functions Manual                  strcmp(3)

NAME
       strcmp, strncmp - compare two strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       int strcmp(const char *s1, const char *s2);
       int strncmp(const char s1[.n], const char s2[.n], size_t n);

DESCRIPTION
       The strcmp() function compares the two strings s1 and s2.  The locale is
       not  taken into account (for a locale-aware comparison, see strcoll(3)).
       The comparison is done using unsigned characters.

       strcmp() returns an integer indicating the result of the comparison,  as
       follows:

       •  0, if the s1 and s2 are equal;

       •  a negative value if s1 is less than s2;

       •  a positive value if s1 is greater than s2.
```


### Dogs and DogList - basic structs

Use the following struct to store data about a dog:

```c
typedef struct {
    string name;
    int age;
    string breed;    
} Dog;
```

Design the `DogList` struct so that it entails all data from all of the dogs, and later functions (like sorting) will only receive such a struct as an argument.
Write a function that releases all heap-allocated memory for this, and a function that returns the number of dogs:

```c
typedef struct {
    // TODO
} DogList;

void free_dog_data(DogList* pdl) {
    // TODO
}

int get_dog_count(DogList dl) { 
    /* TODO */
}
```
You can use any datastructure you want, keep in mind that the number of dogs is **NOT** limited.

Extend the following function to load the data from [`dog_data.txt`](dog_data.txt).
All the data from the file is already read into the buffer variables, you just need to use them to fill a `DogList`.


```c
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
```

Make a simple printout of the list for easy debugging.

```c
void debug_dog_list(DogList dl){
    // TODO
}
```

Having all this done earns **3 points**.

### Sorting by age and then by name

Write the sorting described above (first by age (increasing) then by name (lexicographically increasing)).

```c
void sort_by_age_then_by_name(DogList dl) {
    // TODO
}
```


You **CANNOT** use bubble or shaker sort.

Depending on the implementation you provide, this can result in different points.

Baiscally:
 - `O(n^2)` sort: **5 points**
 - `O(nlogn)` sort: **9 points**
 - Counting sort: **11 points**
 - Radix: **+2 points**
  
Which allows plenty of combinations:
 - Sorting on both fields at once with:
   - an `O(n^2)` sorting algorithm: **5 points**
   - an `O(nlogn)` sorting algorithm: **9 points**
 - Using Radix sort on the two fields, with:
   - the same `O(n^2)` algorithm: **7 points**
   - the same `O(nlogn)` algorithm: **11 points**
   - Two different `O(n^2)` algorithms: **12 points**
   - An `O(n^2)` and an `O(nlogn)` algorithm: **16 points**
   - Two different `O(nlogn)` algorithms: **20 points**
   - Counting sort and an `O(n^2)` algorithm: **18 points**
   - Counting sort and an `O(nlogn)` algorithm: **22 points**

This also means, that you can get the maximal 23 points with tasks until now, or you can chose to go with a simpler solution here, and get additional points from the second part:


### Sorting dogs into kennels

Similar to `DogList`, design the `Conflicts` struct, extend the function that loads it from the file, and write another function that deallocates memory. 
This struct only need to store if two dogs can be put into the same kennel or not, further details about the reason are not necessary.

This is similarly worth **3 points**.

```c
typedef struct {
    // TODO
} Conflicts;

Conflicts load_conflict_data(DogList dl, const char* logfile) {
    /* Buffer variables for reading */
    string bstring1, bstring2;

    Conflicts c;
    // TODO
    
    FILE* f = fopen("dog_data.txt", "r");
    while(2==fscanf(f," %*s %s attacked %s ", bstring1, bstring2)) {
        // TODO
    }
    fclose(f);
    return c;
}

void free_conflicts_data(Conflicts* pc) {
    // TODO
}
```

> [!Important]
> You can assume, that the `DogList` provided for the loading function will not change later. 
> I.e., the indices of dogs will not change (all the sorting is done before that), you can build the graph based on indices.

Feel free to use this provided function if useful (just don't forget to deallocate memory):

```c
int* initialize_array(int size, int value) {
    int* array = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        array[i] = value;
    return array;
}
```

There are 3 different algorithms for sorting the dogs into kennels. 
You can decide which to implement if any. 
All of the functions should return a pointer to an `int` array, that contains at index `i` the number of the kennel where the the dog at index `i` should be put. 

Example:
 - If my Doglist is `[Athos, Porthos, Aramis, D'Artagnan]`
 - And one of the functions return `[0,1,1,0]`
 - It means, that Athos and D'Artagnan should be in Kennel 0, and Porthos and Aramis in Kennel 1.

#### Simple sorting - **8 points**

```c
int* kennels_simple_opennew(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```
Algorithm:
 - Put the first dog in kennel 0. 
 - For each subsequent dog, check if it can be put (no conflicts) into the same room.
   - if yes, put it there.
   - if no, consider the current kennel finished, open a new one, and put it there.


#### First fit with current ordering - **11 points**

```c
int* kennels_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```

Algorithm:
 - Put the first dog in kennel 0.
 - For each subsequent dog, put it into the kennel with the smallest index, where there is no conflict. (Put it into kennel 0 if ok. If not, try kennel 1, if not, kennel 2, etc.)

#### First fit with clever ordering - **18 points**

```c
int* kennels_clever_first_fit(Conflicts c) {
    int* kennels = initialize_array(c.size, -1);
    // TODO
    return kennels;
}
```

Algorithm:
 - First order the dogs by a "Selection sort variant":
   - move the dog with the least number of conflicts to the last position
   - Find the second dog with the least number of conflicts, and move it to the one bust last position. But(!) only consider conflicts between dogs that were not selected yet.
   - Do this for all of the dogs.
 - After sorting, use first-fit as described for the previous algorithm.


## Summary of possible points

The total number of achievable points is **66**, which is naturally not realistic in a 2 hour time frame, and the points are capped at 23.
You can select the tasks that are the safest/easiest for you.

Exam part | Sorting by age-name | Sorting into kennels |
--- | --- | ---| 
Basic structures, functions | 3 | 3 |
Main task | 5 to 22 | 9 + 11 + 18 |

Few example scenarios
 - Radix sort with quick sort for both fields + basic things for the second part, but no kenneling: 3+2+9+3 = 17 points.
 - Single merge sort for the first part, and the simple algorithm for the second: 3+9+3+8 = 23 points.
 - Radix sort with counting and quick sort, nothing from the second part: 3+2+11+9 = 25 -> 23 points.
 - Basic structure from the first part + simple first fit from the second: 3 + 3 + 11 = 17 points.
# Algorithm and Data structures Test 2 Example

## Theory 

### T1. Sorting theory - 2p

Name a sorting algorithm, that has a linear beast-case running time. Explain why in a few sentences.

### T2. Yes/No questions - 3p
Tell if the following statements are true or false, and provide a reason in a single sentence.

 -  Quick sort needs more memory (assymptotically) than heap sort.
 -  Insertion sort cannot be faster for any arrays than quicksort.
 -  In a max-heap, the left child should always be smaller than the right child.

## Practice

### P1. BST operations - 4p

Start with the following tree: `19-(6-(3-()-(5))-())-(34-()-(63))` 
(The notation reads: `Parent-(left child)-(right child)`)

Perform the following operations and draw the state of the tree after each:

 - `push(42)`
 - `push(7)`
 - `delete(6)`
 - `delete_max()`

For the final tree, provide:
 
 - pre-order traversal: 
 - in-order traversal: 
 - post-order traversal: 

### P2. Heap operations - 4p

Start with the following max-heap: `[55,21,34,13,2,5,8,1,3]`

Perform the following operations and draw the state of the heap after each:
 - `push(35)`
 - `push(21)`
 - `pop_max()`
 - `push(7)`
 - `pop_max()`
 - `pop_max()`

## Code analysis and correction - 4p

Which sorting algorithm is coded below:

```C
void magic_sort(int* array, int size) {
    int *p, *c, t;
    for(c=array; c<array+size; ++c) {
        for(p=array; p<array+size; ++p) {
            if (*p < *c) {
                t = *p;
                *p = *c;
                *c = t;
            }
        }
    }
}
```

Why is it wrong? Correct it. 

What is the running time best/average/worst case?



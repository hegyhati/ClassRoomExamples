# Data Structures & Algorithms - Test 1
2026.10.27.

## 1. Big-O notation
Match functions to the asymptotic sets that contain them.

| | <span style="visibility:hidden">________________________</span> | | 
| --- | ---  | --- |
| $n^2 + log(n)$ | | $O(n^2)$ | 
| $n^2 \cdot log(n)$ | | $\Theta(n^2)$ | 
| $n + log(n^2)$ | | $\Omega(\log(n))$ | 
| $n \cdot log(n^2)$ | | $\omega(n)$ | 


## 2. True/False
Which statements are true/false? In the latter case, reason about it.
 - Heap sort and Insertion sort are in-place.
 - In a balanced BST, finding the minimal value takes $O(1)$ time
 - In a max-heap, finding the minimal value takes $O(\log(n))$ time
 - Quick sort is always faster than bubble sort. 
 - Compared to dynamic arrays, linked lists have lower memory fragmentation, but they are worse for CPU caching.


## 3. Asymptotic running time of DS operations

 | |Dynamic Array|  (Singly) linked list with tail pointer | 
 | --- | --- | --- |
 `push_front(&mut self, mutvalue:i32)` | | 
 `push_back(&mut self, value:i32)` | | 
 `pop_front(&mut self) -> i32` | | 
 `pop_back(&mut self) -> i32` | | 
 `size(&self) -> i32` | | 
 `at(&self, idx:usize) -> i32` | | 
 `contains(&self, value:i32) -> bool` | | 

## 4. BST
 - In 1-2 sentences: what are the rules of a BST? (I.e., when is a tree considered a BST?)
 - Advantageous features of BST, and few examples where it can be useful. 
 - Sketch the basic `struct` and the `contains(&self, value:i32) -> bool` function.

## 5. Heap
Consider this initial array: `[1,7,3,9]`, draw the heap after each of the following steps:
 - build a max heap
 - `push(5)`
 - `push(55)`
 - `pop_max()` 
 - `push(8)`
 - `pop_max()`

Provide the pre- and postorder traversals in the last binary tree.

## 6. Sort
When learning about sorting algorithms, we always considered that the data is available in a dynamic array. Which algorithm would you use and why if the data is in a doubly linked list? Explain briefly the needed adjustments. 





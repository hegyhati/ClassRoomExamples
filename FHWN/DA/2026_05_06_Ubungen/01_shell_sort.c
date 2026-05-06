/*

Implement the Shell sorting algorithm in such a way, that the intervals are provided by an array as well.

Shell sort: https://en.wikipedia.org/wiki/Shellsort

Basic idea: if interval list is {4,2,1} then there are 3 "runs" of insertion sort.
In the first run 4 "subarrays" are sorted by insertion sort:
 1) 0,4,8,12,...
 2) 1,5,9,13,...
 3) 2,6,10,14,...
 4) 3,7,11,15,...

In the second run, 2 "subarrays" are sorted by insertin sort:
 1) 0,2,4,6,8,...
 2) 1,3,5,7,9,...

In the last run the whole array is sorted by insertion sort.

*/

void shell_sort(Array array, Array intervals) {
    // todo
}
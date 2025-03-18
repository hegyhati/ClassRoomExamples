# Fixes size array with known size at compilation

```cpp
#define SIZE roka

int my_array[SIZE];
```

de c++11 ota:

```cpp
#include <array>

std::array<int,10> myArray;
```


# Fixed sizes array with known size at runtime

```cpp
    int size;
    std::cin >> size;

    int *my_array = new int[size];
    ....
    delete [] my_array;
```
igazabol ilyet ne.

# Dynamic array

```cpp
#include <vector>

std::vector<int> myVector;
```


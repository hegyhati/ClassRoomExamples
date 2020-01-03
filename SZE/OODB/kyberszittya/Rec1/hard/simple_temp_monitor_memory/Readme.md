# Build with CMake
Create a folder:
```bash
mkdir build && cd build
cmake ..
make
```
Then run:
```bash
./SimpleTempMonitorMemory
```

# Debug
To debug with cmake, run the following:
```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug
make
```
Then, you can use a debugger (gdb):
```
gdb ./SimpleTempMonitorMemory
```

To check memory leaks with Valgrind, use the following:
```
valgrind --leak-check=yes ./SimpleTempMonitorMemory
```
#!/bin/bash

echo "---------------------------"
echo "Compiling optimized version"
echo "---------------------------"
echo

g++ -Wall -std=c++11 main.cpp -o optimized

echo "-------------------------------"
echo "Compiling non-optimized version"
echo "-------------------------------"
echo

g++ -Wall -std=c++11 -fno-elide-constructors main.cpp -o non-optimized

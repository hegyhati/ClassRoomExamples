#! /bin/bash

glpsol -m puska.m -o puska.txt
glpsol -m puska2.m -o puska2.txt
glpsol -m puska3.m -d puska3.d -y puska3.log -o puska3.txt

#!/bin/bash
docker build -t server .
docker run -p 5000:5000 -v "$(pwd)/$1:/app/map.txt" server 

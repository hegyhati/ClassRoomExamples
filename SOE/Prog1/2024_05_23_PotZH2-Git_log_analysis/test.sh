#!/bin/bash

printf "%-70s" "Cleaning up..."
rm examples/*.json
rm examples/*.png
echo "[Done]"

for i in `ls examples/*.log`
do
    printf "%-70s" "Converting log file $i to json..."
    ./log_parser.py "$i"
    echo "[Done]"
    
    printf "%-70s" "Generating statistics for ${i%.*}.json..."
    ./stats.py "${i%.*}.json"
    echo "[Done]"
done
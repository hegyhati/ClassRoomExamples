#!/bin/bash
cup json.cup &&
jflex json.jflex && 
javac -cp .:/usr/share/java/cup_runtime.jar *.java &&
java -cp .:/usr/share/java/cup_runtime.jar Main 

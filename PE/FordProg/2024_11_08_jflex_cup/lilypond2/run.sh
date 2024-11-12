#!/bin/bash 


jflex LilyPond.jflex && 
cup -parser LilyPond_Parser LilyPond.cup && 
javac -cp .:/usr/share/java/cup.jar *.java && 
java -cp .:/usr/share/java/cup.jar Main
set People;
set Tasks;
param previous{Tasks} symbolic in Tasks;
param lasttask symbolic in Tasks;

param nHours;
set Hours := 1..nHours;

param speed{People,Tasks} >= 0; # km/h
param efficiency <=1 >=0;

var do{Hours,People,Tasks} binary;
var progress{Hours union {0},Tasks} >= 0; # redundans / fixed, km

# A person can do only one task at a time
s.t. OneTaskPerPerson{e in People, o in Hours}:
    sum{f in Tasks} do[o,e,f] <= 1;

# Connect redundant variables
s.t. ProgressIsZeroAtStart{f in Tasks}:
    progress[0,f]=0;

s.t. Progress{o in Hours, f in Tasks}:
    progress[o,f]<=progress[o-1,f]+sum{e in People} do[o,e,f]*speed[e,f]*efficiency;

# Task progress can not overtake its prerequisite
s.t. TaskPrecedence{o in Hours, f in Tasks}:
    progress[o,f] <= progress[o,previous[f]];
    
maximize CompleteProgress: progress[nHours,lasttask];

solve;

for{ o in Hours} {
    printf "%d. ora:\n",o;
    for{f in Tasks}{
        printf "\t%14s (%.2f -> %.2f):",f,progress[o-1,f],progress[o,f];
        for{e in People : do[o,e,f]==1}
            printf " %s",e;
        printf "\n";
    }
    printf "\n";
}


data;

set People :=  Andi Bela Cili Dani Elek Feri Gabi Heni Ili;

set Tasks :=  hantas alapfestes jelzesfestes lakkozas;

param previous :=
    hantas       hantas # UGLY FIX LATER
    alapfestes   hantas
    jelzesfestes alapfestes
    lakkozas     jelzesfestes
;

param lasttask := lakkozas;

param nHours := 8;

param efficiency := 0.8;

param speed: 
	    hantas	alapfestes	jelzesfestes	lakkozas:=
Andi	5.49	8.14	    8.46    	    7.79
Bela	5.84	7.76	    5.82    	    8.93
Cili	5.74	7.68	    6.43    	    7.55
Dani	8.20	5.81	    8.09    	    8.76
Elek	7.39	6.62	    5.81    	    7.68
Feri	5.28	6.70	    5.10    	    5.90
Gabi	7.46	7.24	    5.82    	    7.12
Heni	7.35	7.29	    7.01    	    7.70
Ili	    7.22	6.05	    5.38    	    5.17
;

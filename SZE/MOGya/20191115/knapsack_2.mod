param objCount;
set Objects := 1..objCount;

# multiple knapsacks
param sacksCount;
set Sacks := 1..sacksCount;

param mass{Objects};

param value{Objects};

param capacity{Sacks};


var take{Objects,Sacks} binary;

maximize totalValue: sum{o in Objects, s in Sacks} take[o,s] * value[o];

s.t. massLimit{s in Sacks}:
    sum{o in Objects} take[o,s] * mass[o] <= capacity[s];

s.t. atMostOnce{o in Objects}:
    sum{s in Sacks} take[o,s] <= 1;

solve;

for{s in Sacks} {
    printf "Knapsack %d contents:", s;
    printf{o in Objects: take[o,s]}: " %d", o;
    printf "\n    Value: %g\n", sum{o in Objects} take[o,s] * value[o];
    printf "    Mass: %g\n", massLimit[s];
}
printf "Total value: %g\n", totalValue;
printf "Total mass: %g\n", sum{s in Sacks}massLimit[s];

data;

param objCount := 5;

param : mass  value :=
1       1     1
2       2.5   3
3       3.5   4
4       4     8
5       5     6
;

param sacksCount := 3;

param capacity :=
    1 4
    2 5
    3 6
;

end;

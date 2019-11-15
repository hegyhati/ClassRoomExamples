param objCount;
set Objects := 1..objCount;

param mass{Objects};

param value{Objects};

param capacity;


var take{Objects} binary;

maximize totalValue: sum{o in Objects} take[o] * value[o];

s.t. massLimit:
    sum{o in Objects} take[o] * mass[o] <= capacity;


solve;

printf "Knapsack contents:";
printf{o in Objects: take[o]}: " %d", o;
printf "\nTotal value: %g\n", totalValue;
printf "Total mass: %g\n", massLimit;

data;

param objCount := 5;

param : mass  value :=
1       1     1
2       2     3
3       3     4
4       9     8
5       5     6
;

param capacity := 13;

end;

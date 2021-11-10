param sellprice;
param maxcomponentprice;

set Components ;
param price{Components};


set Groups ;
param maxpay{Groups};
param population{Groups};

param needs{Groups,Components} binary;


var use{Components} binary;
var buy{Groups} binary;

s.t. Budget_constraint:
    sum{c in Components} price[c] * use[c] <= maxcomponentprice; 

s.t. Required_component{g in Groups, c in Components: needs[g,c]==1}:
    use[c] >= buy[g];

s.t. Max_budget_for_groups{g in Groups : maxpay[g] < sellprice}:
    buy[g] = 0;

maximize Income:
    sum{g in Groups} sellprice * population[g] * buy[g];


solve;

printf "\n\nUsed components:\n";
for {c in Components : use[c] == 1} {
    printf " - %s (%g)\n",c,price[c];
}

printf "\n\nBuying groups:\n";
for {g in Groups : buy[g] == 1} {
    printf " - %s (%g)\n",g,population[g];
}


printf "\n\nSum income: %g\n\n",Income;

end;
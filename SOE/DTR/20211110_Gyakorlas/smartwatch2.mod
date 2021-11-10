set Products;

param sellprice{Products};
param maxcomponentprice{Products};

set Components ;
param price{Components};


set Groups ;
param maxpay{Groups};
param population{Groups};

param needs{Groups,Components} binary;


var use{Products,Components} binary;
var buy{Groups,Products} binary;

s.t. Budget_constraint{p in Products}:
    sum{c in Components} price[c] * use[p,c] <= maxcomponentprice[p]; 

s.t. Required_component{g in Groups, c in Components, p in Products: needs[g,c]==1}:
    use[p,c] >= buy[g,p];

s.t. Max_budget_for_groups{g in Groups, p in Products: maxpay[g] < sellprice[p]}:
    buy[g,p] = 0;

s.t. At_most_one_watch_per_group{g in Groups}:
    sum{p in Products} buy[g,p] <= 1;

maximize Income:
    sum{g in Groups, p in Products} sellprice[p] * population[g] * buy[g,p];


solve;

for{p in Products} {

    printf "\n\n-- %s --\n\n",p;

    printf "Used components:\n";
    for {c in Components : use[p,c] == 1} {
        printf " - %s (%g)\n",c,price[c];
    }

    printf "Buying groups:\n";
    for {g in Groups : buy[g,p] == 1} {
        printf " - %s (%g)\n",g,population[g];
    }

}

printf "\n\nSum income: %d\n\n",Income;

end;
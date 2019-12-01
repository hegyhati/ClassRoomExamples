set Components;
param price{Components};

set Groups;
param needs{Groups,Components} binary;
param maxpay{Groups};
param population{Groups};

param sellprice;
param maxcomponentprice;

var use{Components} binary;
var buy{Groups} binary;

s.t. DontBuyIfNeededComponentIsMissing{g in Groups, c in Components : needs[g,c]=1}:
    buy[g] <= use[c];

s.t. DontBuyIfTooExpensive{g in Groups: sellprice > maxpay[g]}:
    buy[g]=0;

s.t. DontSpendTooMuchOnComponents:
    sum{c in Components} price[c] * use[c] <= maxcomponentprice;


maximize Income: 
    sum{g in Groups} buy[g]*sellprice*population[g];


solve;

printf "\nIncluded components: ";
for {c in Components: use[c]=1} printf " %s",c;
printf "\n";
printf "Targeted groups:\n";
for{g in Groups:buy[g]=1}
{
    printf "\tGroup %3s, population: %g\n",g,population[g];
}
printf "Sold to a total of %d people, making %d income\n", sum{g in Groups: buy[g]=1} population[g], sum{g in Groups: buy[g]=1} population[g]*sellprice;

set Components;
param price{Components};

set Groups;
param needs{Groups,Components} binary;
param maxpay{Groups};
param population{Groups};

set Watches;
param sellprice{Watches};
param maxcomponentprice{Watches};

var use{Watches,Components} binary;
var buy{Groups,Watches} binary;

s.t. DontBuyIfNeededComponentIsMissing{g in Groups, c in Components, w in Watches : needs[g,c]=1}:
    buy[g,w] <= use[w,c];

s.t. DontBuyIfTooExpensive{g in Groups, w in Watches: sellprice[w] > maxpay[g]}:
    buy[g,w]=0;

s.t. DontSpendTooMuchOnComponents {w in Watches}:
    sum{c in Components} price[c] * use[w,c] <= maxcomponentprice[w];

s.t. OnlyBuyAtMostOneWatch {g in Groups}:
    sum{w in Watches} buy[g,w] <= 1;

maximize Income: 
    sum{g in Groups, w in Watches} buy[g,w]*sellprice[w]*population[g];


solve;

for {w in Watches}
{
    printf "\n\nWatch: %s\n", w;
    printf "\tIncluded components: ";
    for {c in Components: use[w,c]=1} printf " %s",c;
    printf "\n";
    printf "\tTargeted groups:\n";
    for{g in Groups:buy[g,w]=1}
    {
        printf "\t\tGroup %3s, population: %g\n",g,population[g];
    }
    printf "\tSold to a total of %d people, making %d income\n", sum{g in Groups: buy[g,w]=1} population[g], sum{g in Groups: buy[g,w]=1} population[g]*sellprice[w];
}
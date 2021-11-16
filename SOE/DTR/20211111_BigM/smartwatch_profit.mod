
param maxcomponentprice;

set Components ;
param price{Components};


set Groups ;
param maxpay{Groups};
param population{Groups};

param needs{Groups,Components} binary;

param M  := max{g in Groups} (maxpay[g] + 1) * (population[g]+1);


var sellprice;  
var use{Components} binary;
var buy{Groups} binary;

s.t. Budget_constraint:
    sum{c in Components} price[c] * use[c] <= maxcomponentprice; 

s.t. Required_component{g in Groups, c in Components: needs[g,c]==1}:
    use[c] >= buy[g];

s.t. Max_budget_for_groups{g in Groups}:
    # Ha  maxpay[g] < sellprice akkor buy[g] = 0
    # Ha buy[g] == 1 akkor maxpay[g] >= sellprice
    # Ha      y == 1 akkor     LHS   >=  RHS
    # LHS >= RHS - M * (1 -y );
    maxpay[g] >= sellprice - M * (1 - buy[g]);

var income{Groups} >= 0;
# = sellprice * population[g] * buy[g]
#
# Ha buy[g] == 1 akkor income[g] = sellprice * population[g]
# Ha buy[g] == 0 akkor income[g] = 0
#
s.t. Bilinear_income_1{g in Groups}:
    income[g] <= sellprice * population[g] + M * (1-buy[g]);
s.t. Bilinear_income_2{g in Groups}:
    income[g] >= sellprice * population[g] - M * (1-buy[g]);
s.t. Bilinear_income_3{g in Groups}:
    income[g] <= 0 + M * buy[g];
# income[g] >= 0 - M * buy[g]

maximize Income:
    sum{g in Groups} income[g];


solve;

printf "\n\nUsed components:\n";
for {c in Components : use[c] == 1} {
    printf " - %s (%g)\n",c,price[c];
}

printf "\n\nBuying groups:\n";
for {g in Groups : buy[g] == 1} {
    printf " - %s (%g)\n",g,population[g];
}


printf "\n\nSellprice: %g\n",sellprice;
printf "Sum income: %g\n\n",Income;

end;

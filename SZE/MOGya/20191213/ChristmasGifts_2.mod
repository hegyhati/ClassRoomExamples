set Friends;
param budget{Friends};
set Items;
param price{Items};
param likes{Friends,Items} binary;

var buy{Friends,Items}, binary;
var give{Friends,Friends}, binary;

s.t. Dont_buy_for_yourself{f in Friends}:
  give[f,f]=0;
s.t. Dont_buy_not_liked_items{f in Friends, i in Items: likes[f,i]==0}:
  buy[f,i] = 0;
  
s.t. Dont_buy_unwanted_items{f1 in Friends, f2 in Friends, i in Items: likes[f2,i]==0}:
  buy[f1,i] <= 1 - give[f1,f2];
s.t. Dont_buy_things_you_cant_afford {f in Friends, i in Items: price[i]>budget[f]}:
  buy[f,i] = 0;

s.t. Everyone_buys_one_gift{f in Friends}:
  sum{i in Items} buy[f,i]=1;
s.t. Everyone_gives_one_gift{f in Friends}:
  sum{f2 in Friends} give[f,f2]=1;
s.t. Everyone_receives_one_gift{f in Friends}:
  sum{f2 in Friends} give[f2,f]=1;

minimize TotalCost : sum {f in Friends, i in Items} price[i]*buy[f,i];

solve;

printf "Total expenses: %g\n", TotalCost;
for {f1 in Friends, f2 in Friends, i in Items:buy[f1,i]==1 && give[f1,f2]==1}
{
  printf "%s (budget: %g) gifts %s (%g) to %s\n",f1,budget[f1],i,price[i],f2;
}

set Friends;
param budget{Friends};
set Items;
param price{Items};
param likes{Friends,Items} binary;


var buy{Friends,Friends,Items}, binary;

s.t. Dont_buy_for_yourself{f in Friends}:
  sum {i in Items} buy[f,f,i]=0;

s.t. Dont_buy_not_liked_items{f1 in Friends, f2 in Friends, i in Items: likes[f1,i]+likes[f2,i]<2}:
  buy[f1,f2,i] = 0;

s.t. Dont_buy_things_you_cant_afford {f in Friends, i in Items: price[i]>budget[f]}:
  sum{f2 in Friends} buy[f,f2,i] = 0;

s.t. Everyone_buys_one_gift{f in Friends}:
  sum{i in Items, f2 in Friends} buy[f,f2,i]=1;

s.t. Everyone_receives_one_gift{f in Friends}:
  sum{i in Items, f2 in Friends} buy[f2,f,i]=1;


minimize TotalCost : sum {f1 in Friends, f2 in Friends, i in Items} price[i]*buy[f1,f2,i];

solve;

printf "Total expenses: %g\n", TotalCost;
for {f1 in Friends, f2 in Friends, i in Items:buy[f1,f2,i]==1}
{
  printf "%s (budget: %g) gifts %s (%g) to %s\n",f1,budget[f1],i,price[i],f2;
}

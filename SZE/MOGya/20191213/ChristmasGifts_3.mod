set Friends;
param budget{Friends};
set Items;
param price{Items};
param likes{Friends,Items} binary;

set PossibleGiftGivings := 
  setof {
      giver in Friends, reciever in Friends, item in Items: 
      giver!=reciever and  likes[giver,item]==1 and likes[reciever,item]==1 and price[item]<budget[giver]
  } (giver,reciever, item);

set PossiblePairs := setof { (giver,reciever,item) in PossibleGiftGivings} (giver,reciever);
param minCost{(giver,reciever) in PossiblePairs} := min{(giver,reciever,item) in PossibleGiftGivings} price[item];


var gift{PossiblePairs}, binary;

s.t. Everyone_gives_one_gift{giver in Friends}:
  sum{(giver,reciever) in PossiblePairs} gift[giver,reciever]=1;

s.t. Everyone_receives_one_gift{reciever in Friends}:
  sum{(giver,reciever) in PossiblePairs} gift[giver,reciever]=1;

minimize TotalCost : sum {(giver,reciever) in PossiblePairs} minCost[giver,reciever]*gift[giver,reciever];

solve;

printf "Total expenses: %g\n", TotalCost;
for {(giver,reciever) in PossiblePairs : gift[giver,reciever]==1}
{
  printf "%s (budget: %g) gives gift to %s for %g,",giver,budget[giver],reciever,minCost[giver,reciever];
  printf "that can be one of the following: ";
  for{(giver,reciever,item) in PossibleGiftGivings:price[item]==minCost[giver,reciever]}
    printf "%s ",item;
  printf "\n";
}

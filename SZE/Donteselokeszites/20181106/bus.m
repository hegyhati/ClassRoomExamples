/*
We have several people who want to get to work using the same bus line,for which the travel times are given.
We know where these people work (at which station), and when they should start working there.
We have several busses that we can schedule to bring these people to work.
It can be assumed (for now) that the capacity of the busses is unlimited.
Everyone must to get to work on time, and we want to minimize the total wasted time before work, that happens when someone arrives early.
*/



set Stations;
set People;
param busCount;
set Busses := 1..busCount;

param traveltime{Stations};

param workstart{People};
param workplace{People}, symbolic;

param M := 300;

var start{Busses} >=0;
var board{People,Busses}, binary;
var arrive{People} >=0;

s.t. EveryboardsOneBusExactly {p in People}:
  sum{b in Busses} board[p,b] = 1;

s.t. EverybodyShouldGetToWorkOnTime{p in People}:
  arrive[p] <= workstart[p];

s.t. SetArrivalTime1{p in People, b in Busses}:
  arrive[p] >= start[b] + traveltime[workplace[p]] - M * (1-board[p,b]);
s.t. SetArrivalTime2{p in People, b in Busses}:
  arrive[p] <= start[b] + traveltime[workplace[p]] + M * (1-board[p,b]);

minimize TotalWastedTimeBeforeWork:
  sum {p in People} (workstart[p]-arrive[p]);

solve;

for{b in Busses}
{
  printf "Bus %d starts from A at: %g\n", b, start[b];
  printf "  ";
  for {s in Stations}
    printf "%s(%g) ",s,start[b]+traveltime[s];
  printf "\n\n";
  for {p in People : board[p,b]=1}
  {
    printf " %s travels to %s, arrives at %g, waits %g until %g\n",
      p, workplace[p], arrive[p], workstart[p]-arrive[p],workstart[p];
  }
  printf "\n\n";
}

printf "Total wasted time: %g\n", sum {p in People} (workstart[p]-arrive[p]);


data;


set Stations := A B C D;
set People := E1 E2 E3 E4 E5 E6 E7;
param busCount := 3;

param traveltime :=
  A 0
  B 10
  C 15
  D 22
  ;

param:
      workstart workplace :=
  E1  50        B
  E2  80        C
  E3  45        D
  E4  75        B
  E5  53        D
  E6  48        C
  E7  88        B
  ;

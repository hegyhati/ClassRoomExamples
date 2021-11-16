/*
We have several people who want to get to work using the same bus line,for which the travel times are given.
We know where these people work (at which station), and when they should start working there.
We have several busses that we can schedule to bring these people to work.
It can be assumed (for now) that the capacity of the busses is unlimited.
Everyone must to get to work on time, and we want to minimize the total wasted time before work, that happens when someone arrives early.
*/

set Stations;
param traveltime{Stations};

set People;
param workstart{People};
param workplace{People} symbolic within Stations;

param busCount;
set Busses := 1..busCount;

var take{People,Busses} binary;
var start{Busses}; # redundans = be kell kotni = ki kell fejezni take-ekbol
var wait{People}>=0; # szinten redundans 


s.t. Everyone_takes_one_bus{p in People}:
  sum{b in Busses} take[p,b] = 1;

# Erjen be idoben
# 
# Ha a p felszall a b buszra, akkor azzal idoben erjen be
# 
# Ha a p felszall a b buszra, akkor amikor beer <= amikor kezdodik a munkaja
# 
# Ha a p felszall a b buszra, akkor 
#   amikor indul b + amennyi ideig tart p munkahelyere eljutni 
#   <= 
#   amikor kezdodik a munkaja
# 
# Ha take[p,b] == 1, akkor 
#   start[b] + traveltime[workplace[p]]
#   <= 
#   workstart[p]
# 
# Ha take[p,b] == 1, akkor 
#   start[b] + traveltime[workplace[p]] <=  workstart[p]
# 
# s.t. Work_start_timing{p in People, b in Busses}:
#     start[b] + traveltime[workplace[p]] 
#     <= 
#     workstart[p] 
#     + M * (1 - take[p,b])
#     ;

param M := 1000;

s.t. Work_start_timing_1{p in People, b in Busses}:
    start[b] + traveltime[workplace[p]] + wait[p]
    >= 
    workstart[p] 
    - M * ( 1 - take[p,b] )
    ;

s.t. Work_start_timing_2{p in People, b in Busses}:
    start[b] + traveltime[workplace[p]] + wait[p]
    <= 
    workstart[p] 
    + M * ( 1 - take[p,b] )
    ;

minimize Total_Waiting_Time:
    sum{p in People} wait[p];


solve;

for {b in Busses}{
  printf "Bus %d: starts at %g\n",b,start[b];
  for {p in People: take[p,b] == 1}
    printf " - %s (%s,%g), waits %g until %g\n",
               p,   workplace[p], start[b] + traveltime[workplace[p]], wait[p], workstart[p];
}




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
/*

Egy bringás futárcégnek dolgozunk be szabadúszóként. 8 órát tervezünk tekerni, méghozzá olyan módon, hogy minden órában néhány jól bejáratott kör egyikére megyünk el, miközben az útvonalhoz közel eső helyekre kézbesítünk csomagokat. A futárcég egy csomaglistát bocsát rendelkezésünktre, amiből mi eldönthetjük, hogy melyikeket vállaljuk el, és melyikeket nem. Minden csomaghoz adott egy kézbesítési határidő, valamint a kiszállítás címe, ami alapján tudjuk, hogy melyik útvonalunkhoz esik közel, és melyikhez nem. Ismert továbbá a csomagok tömege. Célunk, hogy minel több csomagot kézbesítsünk. 

Hogy semmiképp ne csússzunk meg, sosem viszünk el egy körre 5-nél több csomagot, vagy tekerünk 10 kilónál több teherrel. Mindemellett, hogy tényleg biztosra menjünk, csak akkor viszünk el egy körre egy csomagot, ha annak a kézbesítési határideje később van, minthogy azt a kört befejeznénk. A késő kézbesítésekért ugyanis a futárcégnek díjat kell fizetnie, amit aztán rajtunk ver le kamatostul.

Bónusz kérdés: hány bringás ismerőst kellene elhívnom, hogy minden csomagot el tudjunk vállalni?

*/

# Input data
set Routes;
set Places;

param visit{Routes,Places};

param ordercount;
set Orders := 1..ordercount;

param weight{Orders}; # kg
param place{Orders} symbolic in Places;
param deadline{Orders}; # hour

param capacity; # kg
param slotcount; # pieces
param jobHours; # hours
set Hours:= 1..jobHours;

# Variables
var select{Hours,Routes} binary;
var deliver{Hours,Orders} binary;


# Constraints

# Exactly one route at a time

s.t. RouteSelection{h in Hours}:
  sum{r in Routes} select[h,r]=1;

# Only deliver orders at a selected route

s.t. OnlyDeliverOnRoute{o in Orders, h in Hours}:
  deliver[h,o]<= 1 - sum{r in Routes:visit[r,place[o]]==0} select[h,r];

# Deliver each order at most once

s.t. OrderDelivery{o in Orders}:
  sum{h in Hours} deliver[h,o] <= 1;
  

# Can not deliver after deadline

s.t. BeforeDeadline{o in Orders, h in Hours: h>=deadline[o]}:
  deliver[h,o]=0;

# Max 5 orders, and max 10kg at a single go

s.t. MaxCapacity {h in Hours}:
  sum{o in Orders} deliver[h,o] * weight[o] <= capacity;

s.t. MaxSlotCount {h in Hours}:
  sum{o in Orders} deliver[h,o] <= slotcount;




# Objective function

maximize deliveredOrders: sum{h in Hours, o in Orders} deliver[h,o];

# Display statement
solve;

for{h in Hours}
{
  for{r in Routes:select[h,r]==1}
  {
    printf "Hour %d: Route %s [",h,r;
    for{p in Places:visit[r,p]==1}
      printf " %s",p;
    printf "]\n";
    
    printf "\tOrders: Totalweight: %g\n",sum{o in Orders:deliver[h,o]==1} weight[o];
    for{o in Orders:deliver[h,o]==1}
      printf "\t\tOrder %d (%s)\n",o,place[o];
  }
}

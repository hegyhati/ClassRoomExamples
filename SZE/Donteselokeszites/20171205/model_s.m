/*
Egy bringás futárcégnek dolgozunk be szabadúszóként. 8 órát tervezünk tekerni, méghozzá olyan módon, hogy minden órában néhány jól bejáratott kör egyikére megyünk el, miközben az útvonalhoz közel eső helyekre kézbesítünk csomagokat. A futárcég egy csomaglistát bocsát rendelkezésünktre, amiből mi eldönthetjük, hogy melyikeket vállaljuk el, és melyikeket nem. Minden csomaghoz adott egy kézbesítési határidő, valamint a kiszállítás címe, ami vagy rajta van valamelyik útvonalunkon, vagy nincs. Ismert továbbá a csomagok tömege.

Hogy semmiképp ne csússzunk meg, sosem viszünk el egy körre 5-nél több csomagot, vagy tekerünk 10 kilónál több teherrel. Mindemellett, hogy tényleg biztosra menjünk, csak akkor viszünk el egy körre egy csomagot, ha annak a kézbesítési határideje később van, minthogy azt a kört befejeznénk. A késő kézbesítésekért ugyanis a futárcégnek díjat kell fizetnie, amit aztán rajtunk ver le kamatostul.

Célunk az, hogy ez alatt a 8 óra alatt maximalizáljuk  a kiszállított csomagok számát.

*/

set Routes;

param ordercount >=0, integer;
set Orders := 1..ordercount;
param deadline{Orders} >=0,integer; # round
param weight{Orders} >=0; # kg

param candeliver{o in Orders, r in Routes};

param capacity; # kg
param slotcount;

set Slots := 1 .. slotcount;

var chose{Slots,Routes}, binary;
var deliver{Slots,Orders}, binary;

s.t. ExactlyOneRouteAtEachSlot {s in Slots}:
    sum{r in Routes} chose[s,r] = 1;

s.t. DeliveredAtMostOnce{o in Orders}:
    sum{s in Slots} deliver[s,o]<=1;

s.t. DontDeliverAfterDeadline{o in Orders, s in Slots : s > deadline[o]}:
    deliver[s,o]=0;

s.t. DeliveredOnlyIfOnRoute{s in Slots, o in Orders}:
    deliver[s,o] <= sum{r in Routes} chose[s,r] * candeliver[o,r];

s.t. MeetCapacity{s in Slots}:
    sum{o in Orders} deliver[s,o]*weight[o]<=capacity;
    

maximize DeliveredOrders: sum{s in Slots, o in Orders} deliver[s,o];

solve;

printf "\n\n";
for{s in Slots}
{
    for{r in Routes:chose[s,r]==1}
    {
        printf "\nSlot %d: %s\n",s,r;
        for{o in Orders: deliver[s,o]==1}
        {
            printf "\t%d(%.2f kg|%d)",o,weight[o],deadline[o];
        }
        printf "\n";
    }   
}

end;

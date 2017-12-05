set Places;
set Routes;

param visit {Routes,Places}, binary;

param ordercount >=0, integer;
set Orders := 1..ordercount;
param deadline{Orders} >=0,integer; # round
param weight{Orders} >=0; # kg
param place{Orders}, symbolic, in Places;

param capacity; # kg
param slotcount;

set Slots := 1 .. slotcount;

set SlotOrder:=setof{s in Slots, o in Orders: s<=deadline[o]}(s,o);

var chose{Slots,Routes}, binary;
var deliver{SlotOrder}, binary;

s.t. ExactlyOneRouteAtEachSlot {s in Slots}:
    sum{r in Routes} chose[s,r] = 1;

s.t. DeliveredAtMostOnce{o in Orders}:
    sum{(s,o) in SlotOrder} deliver[s,o]<=1;

s.t. DeliveredOnlyIfOnRoute{(s,o) in SlotOrder}:
    deliver[s,o] <= sum{r in Routes: visit[r,place[o]]} chose[s,r];

s.t. MeetCapacity{s in Slots}:
    sum{(s,o) in SlotOrder} deliver[s,o]*weight[o]<=capacity;
    

maximize DeliveredOrders: sum{(s,o) in SlotOrder} deliver[s,o];

solve;

printf "\n\n";
for{s in Slots}
{
    for{r in Routes:chose[s,r]==1}
    {
        printf "\nSlot %d: %s\n",s,r;
        for{p in Places: visit[r,p]==1}
        {
            printf "\t%s:",p;
            for{(s,o) in SlotOrder: deliver[s,o]==1 && place[o]==p}
            {
                printf "\t%d(%.2f kg|%d)",o,weight[o],deadline[o];
            }
            printf "\n";
        }
    }   
}

end;

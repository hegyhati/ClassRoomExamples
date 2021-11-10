set Places;

set Routes;

param visit {Routes,Places} binary;

param ordercount;
set Orders := 1..ordercount;

param deadline{Orders};    
param weight{Orders};  
param place{Orders} symbolic in Places;
param profit{Orders};

param capacity;

param slotcount;
set Slots := 1..slotcount;

var select{Slots,Routes} binary;
var deliver{Slots,Orders} binary;

# Egy korben egy utvonalra megyunk
s.t. One_Route_at_a_time{s in Slots}:
    sum{r in Routes} select[s,r] = 1;


# Legfeljebb 5 rendelest teljesitek egy korben
s.t. Max_5_orders_at_a_time{s in Slots}:
    sum{o in Orders} deliver[s,o] <= 5;


# A kapacitasomat ne vallaljam tul, 10 kilonal tobbet egy korre ne vigyek el
s.t. Max_capacity{s in Slots}:
    sum{o in Orders} weight[o] * deliver[s,o] <= capacity;

# Nem szallithatunk olyat ki, ami nincs az utvonal mellett
s.t. Only_close_orders{s in Slots, o in Orders, r in Routes : visit[r,place[o]]==0 }:
    deliver[s,o] <= 1 - select[s,r];

# Egy rendelest legfeljebb egyszer vihetunk ki
s.t. Each_order_at_most_once{o in Orders}:
    sum{s in Slots} deliver[s,o] <= 1;


# Hatarido utan ne vigyunk ki dolgokat
s.t. No_delivery_after_deadline{o in Orders, s in Slots : s > deadline[o]}:
    deliver[s,o] = 0;

maximize Profit:
    sum{o in Orders, s in Slots} profit[o] * deliver[s,o]; 


solve;

for {s in Slots, r in Routes : select[s,r]==1} {
    printf "%d. kor: %s\n",s,r;
    for {o in Orders : deliver[s,o]==1}{
        printf " - %d. rendeles (%s, %g kg, %g Ft)\n", o, place[o], weight[o], profit[o];
    }

}


end;

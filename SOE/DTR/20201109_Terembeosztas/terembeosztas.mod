set Rooms;
param capacity{Rooms} integer, >=0;
param fee{Rooms}; # HUF/h

set Classes;
param hours{Classes} integer, >=0;
param students{Classes} integer, >=0;

param totalHours;

param M;


var assign{Classes,Rooms} binary;

s.t. EveryClassMustBeAssigned{c in Classes}:
  sum {r in Rooms} assign[c,r]=1;

s.t. ShouldNotExceedTimeLimit{r in Rooms}:
  sum{c in Classes} hours[c]*assign[c,r] <= totalHours;

s.t. CapacityMustBeLargerThanStudentCount{r in Rooms, c in Classes: capacity[r]<students[c]}:
  assign[c,r]=0;

s.t. CapacityMustBeLargerThanStudentCount2{r in Rooms, c in Classes}:
  capacity[r]>=students[c] - M*(1-assign[c,r]);


minimize TotalCost: sum{c in Classes, r in Rooms} assign[c,r]*hours[c]*fee[r];

solve;

printf "\n\n";

printf "Total cost: %d\n\n",TotalCost;

for{r in Rooms : sum{c in Classes}assign[c,r] > 0} {
  printf "Room %s (Capacity: %d):\n",r,capacity[r];
  for{c in Classes:assign[c,r]==1}
    printf " - %s (%dh, %d students)\n",c,hours[c],students[c];
  printf "\n";
}

data;

param M:=100;

param totalHours := 8;

set Rooms:= T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T19;

param:
      capacity  fee :=
  T1	33	      3600
  T2	57	      5000
  T3	26	      3500
  T4	15	      7500
  T5	17	      5900
  T6	40	      4600
  T7	26	      6200
  T8	70	      4000
  T9	99	      4100
  T10	57	      7900
  T11	19	      5400
  T12	24	      9900
  T13	87	      9700
  T14	59	      3700
  T15	15	      3300
  T16	50	      8400
  T17	78	      9500
  T18	59	      9200
  T19	77	      9900
;

set Classes:= Kurzus1 Kurzus2 Kurzus3 Kurzus4 Kurzus5 Kurzus6 Kurzus7 Kurzus8 Kurzus9 Kurzus10 Kurzus11 Kurzus12 Kurzus13 Kurzus14 Kurzus15 Kurzus16 Kurzus17 Kurzus18 Kurzus19 Kurzus20 Kurzus21 Kurzus22 Kurzus23;

param:
              hours   students :=
  Kurzus1	    2	      55
  Kurzus2	    4	      18
  Kurzus3	    2	      60
  Kurzus4	    6	      14
  Kurzus5	    6	      24
  Kurzus6	    3	      28
  Kurzus7	    3	      13
  Kurzus8	    3	      54
  Kurzus9	    6	      40
  Kurzus10  	4 	    54
  Kurzus11  	2 	    46
  Kurzus12  	4 	    35
  Kurzus13  	4 	    70
  Kurzus14  	5 	    13
  Kurzus15  	2 	    27
  Kurzus16  	6 	    47
  Kurzus17  	3 	    19
  Kurzus18  	4 	    43
  Kurzus19  	2 	    55
  Kurzus20  	3 	    40
  Kurzus21  	3 	    12
  Kurzus22  	3 	    43
  Kurzus23  	6 	    41
;

set Rooms;
param capacity{Rooms} integer, >=0;
param fee{Rooms}; # HUF/h
set ComputerRooms in Rooms;

set Classes;
param hours{Classes} integer, >=0;
param students{Classes} integer, >=0;
param needComputers{Classes} binary, default 0;

set ClassPairs:=setof{c1 in Classes, c2 in Classes: c1!=c2}(c1,c2);

set Lecturers;
param lecturer{Classes} symbolic in Lecturers;

param nDays;
set Days := 1..nDays;

param openHoursStart;
param openHoursEnd;

param M;

var assign{Classes,Rooms,Days} binary;
var start{Classes}>=openHoursStart;
var before{ClassPairs} binary;

s.t. EveryClassMustBeAssigned{c in Classes}:
  sum {r in Rooms, d in Days} assign[c,r,d]=1;

s.t. CapacityMustBeLargerThanStudentCount{r in Rooms, c in Classes, d in Days: capacity[r]<students[c]}:
  assign[c,r,d]=0;

s.t. IfNeedsComputerMustBeAssignedToComputerRoom {c in Classes, r in Rooms diff ComputerRooms, d in Days : needComputers[c]==1}:
  assign[c,r,d]=0;

s.t. FinishBeforeBuildingCloses{c in Classes}:
  start[c]+hours[c] <= openHoursEnd;

s.t. TeacherCanNotClone{l in Lecturers, (c1,c2) in ClassPairs, d in Days : lecturer[c1]=l && lecturer[c2]=l}:
  start[c2]  >= start[c1] + hours[c1] - M * (3-before[c1,c2]-sum{r in Rooms}assign[c1,r,d] - sum{r in Rooms}assign[c2,r,d]);

s.t. PrecedenceBetweenClassesForTheSameTeacher{l in Lecturers, (c1,c2) in ClassPairs, d in Days : lecturer[c1]=l && lecturer[c2]=l && c1<c2}:
  before[c1,c2] + before[c2,c1] >= -1 + sum{r in Rooms}assign[c1,r,d] + sum{r in Rooms}assign[c2,r,d];

s.t. OneClassAtATimeInARoom{r in Rooms, (c1,c2) in ClassPairs, d in Days}:
  start[c2]  >= start[c1] + hours[c1] - M * (3-before[c1,c2]-assign[c1,r,d]-assign[c2,r,d]);

s.t. PrecedenceBetweenClassesInTheSameRoom{r in Rooms, (c1,c2) in ClassPairs, d in Days: c1<c2}:
  before[c1,c2] + before[c2,c1] >= -1 + assign[c1,r,d] + assign[c2,r,d];

minimize TotalCost: sum{c in Classes, r in Rooms, d in Days} assign[c,r,d]*hours[c]*fee[r];

solve;

printf "\n\n";

printf "Total cost: %d\n\n",TotalCost;

param position{c in Classes, r in Rooms, d in Days: assign[c,r,d]==1}:= 
  sum{c2 in Classes: c2 != c && assign[c2,r,d]==1 && before[c2,c]==1} 1; 

for {d in Days} {
  printf "#####################\n";
  printf "### Day %d       #####\n",d;
  printf "#####################\n";

  for{r in Rooms : sum{c in Classes}assign[c,r,d] > 0} {
    for{{0}:r in ComputerRooms} printf "Computer ";
    printf "Room %s (Capacity: %d):\n",r,capacity[r];
    for{pos in 0..card(Classes)} {
      for{c in Classes:assign[c,r,d]==1 && position[c,r,d]==pos} {
        printf " %2d-%2d: %s (%dh, %d students)",start[c],start[c]+hours[c],c,hours[c],students[c];
        for{{0}:needComputers[c]} printf " - needs computers";
        printf "\n";
      }
    }
    printf "\n";
  }
}

param lposition{c in Classes, d in Days} := 
  sum{c2 in Classes: c2!=c && lecturer[c]==lecturer[c2] && before[c2,c] && sum{r in Rooms}assign[c,r,d]==1} 1;

for{l in Lecturers} {
  printf "Lecturer %s :\n",l;
  for {d in Days : sum{c in Classes, r in Rooms : lecturer[c]==l} assign[c,r,d] >= 1} {
    printf " Day %d: ",d;
    for{pos in 0..card(Classes)} {
      for{c in Classes, r in Rooms:lecturer[c]==l && lposition[c,d]==pos && assign[c,r,d]==1} {
        printf "%2d-%2d: %s (%s)  ",start[c],start[c]+hours[c],c,r;
      }
    }
    printf "\n";
  }
  printf "\n";
}

data;

param nDays := 5;

param openHoursStart := 8;
param openHoursEnd   := 18;

param M := 24;

set Rooms:= T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T19;
set ComputerRooms :=  T8 T9 T10 T11 T12 T13 T14 ;

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
set Lecturers:= Q W E R T Y;

param:
              hours   students  needComputers lecturer:=
  Kurzus1	    2	      55        .             Q
  Kurzus2	    4	      18        .             T
  Kurzus3	    2	      60        .             Q
  Kurzus4	    6	      14        .             Q
  Kurzus5	    6	      24        .             W
  Kurzus6	    3	      28        1             T
  Kurzus7	    3	      13        .             W
  Kurzus8	    3	      54        .             W
  Kurzus9	    6	      40        1             E
  Kurzus10  	4 	    54        .             Y
  Kurzus11  	2 	    46        .             E
  Kurzus12  	4 	    35        1             Y
  Kurzus13  	4 	    70        .             E
  Kurzus14  	5 	    13        .             R
  Kurzus15  	2 	    27        .             Q
  Kurzus16  	6 	    47        1             T
  Kurzus17  	3 	    19        .             R
  Kurzus18  	4 	    43        .             R
  Kurzus19  	2 	    55        .             R
  Kurzus20  	3 	    40        1             Q
  Kurzus21  	3 	    12        .             T
  Kurzus22  	3 	    43        .             Y
  Kurzus23  	6 	    41        1             Y
;       
        
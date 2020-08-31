set Offices;
param capacity{Offices} >=0, integer;

set Employees;

param nDays;
set Days:=1..nDays;

param present{Days,Employees} binary, default 0;

var assign{Employees,Offices} binary;

set Connections := setof {e1 in Employees, e2 in Employees: e1 < e2 } (e1,e2);
var meets{Connections} binary;


s.t. AbideOfficeCapacity{o in Offices}:
    sum{e in Employees} assign[e,o] <= capacity[o];

s.t. EveryoneNeedsAnOffice{e in Employees}:
    sum{o in Offices} assign[e,o] = 1;

s.t. PeopleMeetIfSameOfficeOnSameDay{(e1,e2) in Connections, o in Offices, d in Days: present[d,e1]==1 and present[d,e2]==1}:
    meets[e1,e2] >= assign[e1,o] + assign[e2,o] - 1; 

minimize TotalMeetings:
    sum{(e1,e2) in Connections} meets[e1,e2];

solve;

printf "\n\nTotal meetings: %d\n",TotalMeetings;
for{(e1,e2) in Connections : meets[e1,e2]}
{
    printf " %4s --- %-4s in office ",e1,e2;
    for {o in Offices: assign[e1,o]==1} printf "%s, on days: ", o;
    for {d in Days: present[d,e1]==1 and present[d,e2]==1} printf " %d",d;
    printf "\n";
}

printf "\n\nOffice assignments:\n";
for {o in Offices}
{
    printf " Office %s:",o;
    for {e in Employees: assign[e,o]==1}
        printf " %s",e;
    printf "\n";
}

data;

set Offices:= A604 A605 A606;

param capacity :=
    A604 2
    A605 2
    A606 3
;

set Employees := HFM BP CSA EF HM OO TSZB;

param nDays := 5;

param present: 
        HFM BP  CSA EF   HM   OO   TSZB:=
    1   1   .   1   .    .    1    1
    2   1   .   .   1    1    1    .
    3   1   .   1   .    1    1    .
    4   1   .   .   1    1    .    1
    5   1   .   1   .    .    1    1
    ;



/*
Advanced:

Azt minimalizaljuk, hogy egy ember atlagosan hany masikat fertoz meg.
Reggelente takaritanak. A hozzarendelt iroda lehet minden nap mas, de maximum 2 fele.
Vannak oktatok, akik idosek, ok nem talalkozhatnak senkivel.

*/

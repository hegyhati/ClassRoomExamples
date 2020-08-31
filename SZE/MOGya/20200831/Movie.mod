/*

Feladatunk koltseghatekonyan leforgatni egy film osszes jelenetet.

A filmben szerepel nehany szinesz, valamint adott a jelenetek listaja.

Minden jelenethez adott, hogy mennyi ideig tart leforgatni, illetve melyik szineszek erintettek benne.

Az egesz filmet adott, hogy hany nap alatt kell leforgatnunk, illetve tudjuk, hogy minden nap legfeljebb 8 orat tudunk dolgozni.

A szineszek fizetese napidij alapu, mely minden szines eseteben kulonbozo. A napidij alapu fizetes azt jelenti, hogyha csak egyetlen egy jelenet miatt is behivunk aznapra egy szineszt, akkor ugyanugy ki kell fizetni a napidijat, mintha mind a 8 orat vegigdolgozta volna.

Keszitsunk olyan MILP modellt, mely a fenti parameterek ismereteben mehatarozza, hogy melyik jelenetet melyik nap forgassuk, illetve melyik nap kiknek kell napidijat fizetni ugy, hogy a teljes koltsegunk minimalis legyen. 

*/

set Scenes;
set Actors;

param duration{Scenes};
param plays{Scenes,Actors} binary;

param nDays;
set Days:=1..nDays;

param dailyTime;
param dailyFee{Actors};

var schedule{Days,Scenes} binary;
var present{Days,Actors} binary;

s.t. EverySceneMustBeScheduled{s in Scenes}:
    sum {d in Days} schedule[d,s] = 1;

s.t. NoActorNoScene{s in Scenes, a in Actors, d in Days: plays[s,a]==1}:
    schedule[d,s] <= present[d,a];

s.t. DailyLimit{d in Days}:
    sum {s in Scenes} duration[s]*schedule[d,s] <= dailyTime;

minimize TotalCost: 
    sum{a in Actors, d in Days} dailyFee[a]*present[d,a];

solve;

for{d in Days} 
{
    printf "Day %d:\n",d;
    printf "  Total Fee: %d\n", sum{a in Actors:present[d,a]==1} dailyFee[a];
    printf "  Actors (Fees):";
    for{a in Actors:present[d,a]==1}
        printf " %s (%d)",a,dailyFee[a];
    printf "\n";
    printf "  Scenes:\n";
    for{s in Scenes:schedule[d,s]==1}
    {
        printf "    Scene %s (",s;
        for{a in Actors:plays[s,a]==1}
            printf " %s",a;
        printf " )\n";
    }
}

data;

set Scenes := 1 2 3 4 5 6 7 8 9 10;

param nDays := 7;

param duration :=
    1	3.06
    2	1.58
    3	1.46
    4	3.23
    5	0.89
    6	2.64
    7	3.95
    8	0.24
    9	4.85
    10	1.39
    ;

set Actors := 
    S_Astin 
    S_Bean 
    O_Bloom 
    B_Boyd 
    C_Blanchett 
    M_Csokas 
    I_Holm 
    C_Lee 
    A_Serkis 
    I_McKellen 
    D_Monoghan 
    V_Mortensen 
    J_RhysDavies 
    L_Tyler 
    H_Weaving 
    E_Wood
    ;


param plays (tr):
	                1	2	3	4	5	6	7	8	9	10:=
    S_Astin 	    0	0	0	0	0	1	1	1	0	1
    S_Bean 	        0	0	1	0	1	0	1	1	1	0
    O_Bloom 	    0	0	1	1	0	0	1	1	0	1
    B_Boyd 	        1	0	0	1	0	0	1	1	1	1
    C_Blanchett 	1	1	1	1	1	0	1	1	0	0
    M_Csokas 	    1	0	0	1	1	0	0	1	1	1
    I_Holm 	        0	0	1	0	1	1	1	1	1	1
    C_Lee 	        0	0	1	0	1	0	0	0	1	0
    A_Serkis 	    0	1	0	1	0	0	0	0	1	0
    I_McKellen 	    0	1	0	1	1	1	1	0	1	0
    D_Monoghan 	    1	1	1	1	1	0	0	0	0	0
    V_Mortensen 	0	0	0	0	1	0	0	0	1	1
    J_RhysDavies 	1	0	1	1	1	1	0	1	0	1
    L_Tyler 	    1	1	1	0	1	1	0	0	0	0
    H_Weaving 	    1	1	1	0	1	0	0	0	0	0
    E_Wood	        0	1	0	0	1	0	1	0	1	1
    ;

param dailyFee :=
    S_Astin 	    1300
    S_Bean 	        4700
    O_Bloom 	    2100
    B_Boyd 	        1700
    C_Blanchett     3400
    M_Csokas 	    2100
    I_Holm 	        4800
    C_Lee 	        1800
    A_Serkis 	    2900
    I_McKellen 	    5400
    D_Monoghan 	    2600
    V_Mortensen     3900
    J_RhysDavies    4100
    L_Tyler 	    1700
    H_Weaving 	    5600
    E_Wood	        5300
    ;

param dailyTime := 8;

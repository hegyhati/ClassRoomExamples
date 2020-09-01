set Tasks;
param duration{Tasks};

param _not_given := -1;
param given_start{Tasks}, default _not_given;

param M:= 1000;

set TaskPairs := setof {t1 in Tasks, t2 in Tasks: t1!=t2} (t1,t2);

var start{Tasks} >=0;
var before{TaskPairs} binary;
var finish;

s.t. FixStartIfGiven{t in Tasks: given_start[t]!=_not_given}:
    start[t]=given_start[t];

s.t. SequenceTasks{(t1,t2) in TaskPairs}:   
    start[t2] >= start[t1] + duration[t1] - M * (1-before[t1,t2]);

s.t. OneWayOrAnother{(t1,t2) in TaskPairs}:
    before[t1,t2]+before[t2,t1]=1;

s.t. Finish{t in Tasks}: 
    finish >= start[t]+duration[t];

minimize Makespan: finish;

solve;

for{position in 1..card(Tasks)}
{
    for{t in Tasks : sum{(t,t2) in TaskPairs} before[t,t2] ==card(Tasks)-position}
    {
        printf "%10s: %4g - %4g\n",t,start[t],start[t]+duration[t];
    }
}



data;

set Tasks:= MOGYA MOSZE A B C D;

param:      given_start duration :=
    MOGYA   3           3
    MOSZE   9           1.5
    A       .           2
    B       .           3.5
    C       .           0.4
    D       .           2.2
    ;

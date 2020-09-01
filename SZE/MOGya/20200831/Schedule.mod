set MovableTasks;
param duration{MovableTasks};

set FixedTasks;
param fixduration{FixedTasks};
param fixstart{FixedTasks};

param M := 1000;

var start{MovableTasks} >=0;
var M_before_F{MovableTasks,FixedTasks} binary;
var M_before_M{MovableTasks,MovableTasks} binary;
var F_before_M{FixedTasks,MovableTasks} binary;
var finish>=0;

s.t. MovableBeforeFix{m in MovableTasks, f in FixedTasks}:
    fixstart[f] >= start[m] + duration[m] - M * (1-M_before_F[m,f]);
s.t. MovableBeforeMovable{m1 in MovableTasks, m2 in MovableTasks: m1 != m2}:
    start[m1] >= start[m2] + duration[m2] - M * (1-M_before_M[m1,m2]);
s.t. FixBeforeMovable{m in MovableTasks, f in FixedTasks}:
    start[m] >= fixstart[f] + fixduration[f] - M * (1-F_before_M[f,m]);

s.t. OneWayOrTheOtherMF{m in MovableTasks, f in FixedTasks}:
    M_before_F[m,f]+F_before_M[f,m] = 1;
s.t. OneWayOrTheOtherMM{m1 in MovableTasks, m2 in MovableTasks:m1!=m2}:
    M_before_M[m1,m2]+M_before_M[m2,m1] = 1;


s.t. FinishAfterLastMovable{m in MovableTasks}:
    finish >= start[m]+duration[m];
s.t. FinishAfterLastFixed{f in FixedTasks}:
    finish >= fixstart[f]+fixduration[f];

minimize Makespan: finish;

solve;

for {f in FixedTasks}
    printf "%s %g-%g\n",f,fixstart[f],fixstart[f]+fixduration[f];
for {m in MovableTasks}
    printf "%s %g-%g\n",m,start[m],start[m]+duration[m];

data;

set MovableTasks := A B C D;

param duration := 
    A   2
    B   3.5
    C   0.4
    D   2.2
    ;

set FixedTasks := MOGYA MOSZE;

param:      fixduration fixstart :=
    MOGYA   3           3
    MOSZE   1.5         9
    ;



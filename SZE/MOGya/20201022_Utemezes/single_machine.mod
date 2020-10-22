set Tasks;
param arrival_time{Tasks} >=0;
param processing_time{Tasks} >=0;

param M := sum{t in Tasks} (arrival_time[t]+processing_time[t]);

var starting_time{Tasks} >=0;

set TaskPairs := setof{t1 in Tasks,t2 in Tasks: t1<t2} (t1,t2);
var preceeds{TaskPairs} binary;
var makespan>=0;

s.t. CanNotStartTooEarly{t in Tasks}:
    starting_time[t] >= arrival_time[t];

s.t. SetMakespan{t in Tasks}:
    makespan >= starting_time[t] + processing_time[t];

s.t. BigMFirst{(t1,t2) in TaskPairs}:
    starting_time[t2]>=starting_time[t1]+processing_time[t1]
        -M*(1-preceeds[t1,t2]);

s.t. BigMSecond{(t1,t2) in TaskPairs}:
    starting_time[t1]>=starting_time[t2]+processing_time[t2]
        -M*preceeds[t1,t2];

minimize Makespan : makespan;

solve;

for{t in Tasks}
    printf "Task %3s : %2d -- %-2d\n",t, starting_time[t],starting_time[t]+processing_time[t];

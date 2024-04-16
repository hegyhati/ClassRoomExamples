set People;
set Tasks;
param time{People,Tasks};

var do{People,Tasks} binary;
var MS >= 0;

s.t. Must_do_task_by_exactly_one_person{t in Tasks}:
    sum{p in People} do[p,t] = 1;

s.t. Makespan_must_be_more_than_individual_load{p in People}:
    sum{t in Tasks} time[p,t] * do[p,t] <= MS;

minimize Makespan: MS;
    


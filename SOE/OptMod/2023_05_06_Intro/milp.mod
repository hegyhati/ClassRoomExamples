set People;
set Jobs;
param hours{Jobs,People} >= 0;

var do{Jobs,People} binary;
var work_hours{People} >= 0;
var finish_time >= 0;

s.t. Every_job_must_be_done_by_one_person {j in Jobs}:
    sum{p in People} do[j,p] = 1;

s.t. Calculate_work_hours{p in People}:
    work_hours[p] = sum{j in Jobs} hours[j,p] * do[j,p];

s.t. Set_finish_time {p in People}:
    finish_time >= work_hours[p];

minimize Finish_Time:
    finish_time
;


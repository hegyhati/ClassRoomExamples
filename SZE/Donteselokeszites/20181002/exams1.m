set Courses;
param nDays;
set Days:=1..nDays;

param required_time{Courses};
param free_time{Days};
param exam_day{Courses};


var study{Days,Courses} >= 0;

s.t. FreeTimeConstraint{d in Days}:
  sum {c in Courses} study[d,c] <= free_time[d];


s.t. RequiredTimeConstraint{c in Courses}:
  sum{d in Days:d < exam_day[c]} study[d,c] >= required_time[c];

    

minimize TotalStudyHours:
  sum{d in Days, c in Courses} study[d,c];

solve;

for{d in Days}
{
  printf "%2d:\n",d;
  for{c in Courses : study[d,c]!=0}
    printf "\t%s\t%g\n",c,study[d,c];
}

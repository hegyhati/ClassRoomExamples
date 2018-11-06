/*

We would like to find out, whether it is feasible to pass all of the courses within our exam period.

We know for each Course, when we can get the exam done, and how much time does it require to prepare to get graded as 2 (sarisfactory).
Each day, we have a given amount of free time, that we can decide to use for studying.

*/

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

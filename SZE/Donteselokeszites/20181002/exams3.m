set Courses;
param nDays;
set Days:=1..nDays;

param required_time{Courses};
param free_time{Days};
param exam_day{Courses};
param credits{Courses};

var pass{Courses} binary;
var study{Days,Courses} >= 0;

s.t. FreeTimeConstraint{d in Days}:
  sum {c in Courses} study[d,c] <= free_time[d];


s.t. RequiredTimeConstraint{c in Courses}:
    sum{d in Days:d < exam_day[c]} study[d,c] >= required_time[c]*pass[c];

    

maximize PassedCourses:
  (sum{c in Courses} 2*pass[c]*credits[c])
  /
  (sum{c in Courses} credits[c])
  ;

solve;
printf "Objective: %g\n\n", PassedCourses;

printf "Failed courses: ";
for{c in Courses : pass[c]==0}
  printf "%s ",c;
printf "\n\n";

for{c in Courses : pass[c]==1}
{
  printf "%s: Exam day: %d\n",c,exam_day[c];
  for{d in Days : study[d,c]>0}
    printf"\tDay %2d: %g\n",d,study[d,c];
}

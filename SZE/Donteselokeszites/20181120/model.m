set Courses;

param credits{Courses};
param examday{Courses};

param nDays := max{c in Courses} examday[c];
set Days := 1..nDays;

param freetime{Days}, default 0;

set Grades;

param noPassCoefficient, default 0;
param contextSwitchTime;

param studyhours{Courses,Grades};


var takeExam{Courses} binary;
var getGrade{Courses,Grades} binary;
var study{Courses,Days} >= 0;
var sitDown{Courses,Days} binary;


s.t. Get_single_passing_grade_iff_exam_is_taken {c in Courses}:
  sum{g in Grades} getGrade[c,g] = takeExam[c];

s.t. Study_enough_for_grade{c in Courses}:
  sum{d in 1..examday[c]-1} study[c,d] >= sum{g in Grades} getGrade[c,g]*studyhours[c,g];

s.t. Can_not_study_more_than_free_time{d in Days}:
  sum{c in Courses} study[c,d] <= freetime[d] * (1 - sum{c in Courses:examday[c]==d} takeExam[c]) - sum{c in Courses} sitDown[c,d] * contextSwitchTime;

s.t. Can_only_study_if_sit_down_to_it{d in Days, c in Courses}:
  study[c,d] <= sitDown[c,d] * freetime[d];

s.t. Setting_unnecessary_variables_to_zero{c in Courses}:
  sum{d in Days: d>=examday[c]} ( study[c,d] + sitDown[c,d]) = 0; 

maximize WeightedGrade:
  (sum{c in Courses} credits[c] *
    (
       sum{g in Grades} g*getGrade[c,g]
       +
       (1-takeExam[c]) * noPassCoefficient
    )
  )
  /
  (sum {c in Courses} credits[c]);

solve;

printf "\n\nFinal weighed grade: %g\n", WeightedGrade;

for{c in Courses : takeExam[c]==1}
{
  printf "\n\nCourse %s: Grade %d (%g hours), exam on day %d\n",c,
    sum{g in Grades} g * getGrade[c,g],
    sum{g in Grades} studyhours[c,g] * getGrade[c,g],
    examday[c];
  for{d in Days: study[c,d] > 0}
  {
    printf "\t - Day %2d: %3g hours\n",d,study[c,d];
  }
}

printf "\n\n\n";

for{d in Days}
{
  printf "Day %2d (%3g hours): ",d,freetime[d];
  for{c in Courses: examday[c]==d && takeExam[c]==1} printf "Takes exam from %s",c;
  for{c in Courses: study[c,d] > 0} printf " %s(%g h)",c,study[c,d];
  printf "\n";
}
end;

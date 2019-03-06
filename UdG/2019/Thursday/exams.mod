# INPUT DATA

param nDays;
set Days := 1..nDays;
set Subjects;
param freetime{Days};
param grade5{Subjects};
param credit{Subjects};
param examday{Subjects};


# VARIABLES

var pass{Subjects} binary;
var study{Subjects,Days} >= 0;

# CONSTRAINTS

# I can not study more on a day, than my freetime
s.t. DoNotExceedFreeTime{d in Days}:
  sum{s in Subjects} study[s,d] <= freetime[d];

# It is useless to study after the exam day
s.t. DoNotStudyAfterExam{s in Subjects, d in Days : d >= examday[s]}:
  study[s,d]=0;

# If we decide to pass an exam, we need to studty as much as needed
s.t. StudyEnoughForGrade{s in Subjects}:
    sum{d in Days : d < examday[s]} study[s,d] >= grade5[s] * pass[s];

# If I decide not to pass,don't waste time at all with studying
s.t. DontWasteTime{s in Subjects}:
    sum{d in Days} study[s,d] <= pass[s]*999;

# OBJECTIVE FUNCTION

maximize WeightedGrade:
  (sum{s in Subjects} credit[s]*5*pass[s])
  /
  sum{s in Subjects} credit[s]
  ;




solve;

printf "\n\n\n";

for {d in Days}
{
  printf "Day %d.:\n",d;
  for {s in Subjects: study[s,d]>0}
    printf "\t - %s:%g hours\n",s,study[s,d];
}


printf "\n\n\n";












data;

param nDays := 10;

set Subjects := Energy Architecture OperationsManagement;

param grade5 :=
  Energy                15
  Architecture          20
  OperationsManagement  30
;

param :
                        credit    examday  :=
  Energy                5.5       8
  Architecture          6         5
  OperationsManagement  5         10
;


param freetime :=
  1 8
  2 10
  3 2
  4 4
  5 3
  6 1
  7 7
  8 3
  9 8
  10  2
;

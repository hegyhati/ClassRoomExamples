set Classes;
param credit{Classes};
param hours{Classes};

param examNumber;
set Exams := 1..examNumber;

param examDay{Classes,Exams};

param dayCount;
set Days := 1..dayCount;
param freetime{Days};

param warmup;

var study{Classes,Days} binary;
var studyhour{Classes,Days} >= 0;
var pass{Classes} binary;
var take{Classes,Exams} binary;


s.t. Study_Studyhour{c in Classes, d in Days}:
  studyhour[c,d]<=study[c,d]*freetime[d];

s.t. Exams_Pass{c in Classes}:
  sum{e in Exams} take[c,e] = pass[c];
  
s.t. Study_enough{c in Classes,e in Exams}:
  sum{d in 1..examDay[c,e]-1} studyhour[c,d] >= hours[c]*take[c,e];

s.t. Daily_study_hours {d in Days}:
  sum{c in Classes} (studyhour[c,d] + study[c,d]*warmup)
  <=
  freetime[d]*(1 - sum{c in Classes,e in Exams: examDay[c,e]==d} take[c,e]);


maximize passedcredits: 
  sum{c in Classes} pass[c]*credit[c];


solve;

printf "\n\nPassed classes:\n\n";

for{c in Classes: pass[c]==1}
{
  printf "\t%s: %2d credits, %2d hours of learning\n",c,credit[c],hours[c];  
  for {d in Days: study[c,d]==1}
    printf "\t\tDay %2d: %4g hours\n",d,studyhour[c,d];
  for {e in Exams: take[c,e]==1}
    printf "\t\tDay %2d: Exam %d taken.\n",examDay[c,e], e;
}

printf "\n\nFailed classes:\n\n";

for{c in Classes: pass[c]==0}
   printf "\t%s\n",c;

printf "\n\nDays:\n\n";
for {d in Days}
{
  printf "\t Day %2d: %3g hours free time\n",d,freetime[d];
  for{c in Classes, e in Exams: examDay[c,e]==d && take[c,e]==1}
    printf "\t\t Take exam from %s\n",c;
  for{c in Classes: study[c,d]==1}
    printf "\t\t Study %3g hours for %s\n",studyhour[c,d],c;
}

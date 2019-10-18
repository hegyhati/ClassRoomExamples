param nJobs;
param nWorkers;

set Jobs := 1..nJobs;
set Workers := 1..nWorkers;

param required_skill{Jobs};
param duration{Jobs};

param skill_level{Workers};
param salary{Workers};
param availability{Workers};

set PossibleAssignments :=
  setof {j in Jobs, w in Workers: skill_level[w]>=required_skill[j]} (j,w);



var do{PossibleAssignments} binary;

s.t. WorkAsMuchAsAvailability{w in Workers}:
  sum {(j,w) in PossibleAssignments} duration[j] * do[j,w] <= availability[w];

s.t. DoAllJobs{j in Jobs}:
  sum{(j,w) in PossibleAssignments} do[j,w] = 1;

minimize Cost:
  sum{(j,w) in PossibleAssignments} salary[w]*duration[j]*do[j,w];


solve;

for {w in Workers}
{
  printf "Worker %d:\t%g/%g\n",w,sum{(j,w) in PossibleAssignments : do[j,w]==1}duration[j],availability[w];
  for {(j,w) in PossibleAssignments:do[j,w]==1}
    printf " - Job %d\t%g\n",j,duration[j];
  printf "\n";
}

  

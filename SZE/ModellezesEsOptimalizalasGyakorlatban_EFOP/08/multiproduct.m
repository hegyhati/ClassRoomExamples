# Input data

param unitCount;
set Units := 1..unitCount;

param jobCount;
set Jobs:= 1..jobCount;

param proctime{Jobs,Units};

param M := 100;

# Variables
var start{Jobs,Units}>=0;
var finish{Jobs,Units}>=0;
var before{Jobs,Jobs} binary;
# before[j1,j2] ==1 if j1 is performed before j2

var makespan;

# Constraints

s.t. ProcessingTime{j in Jobs, u in Units}:
  finish[j,u] = start[j,u] + proctime[j,u];

s.t. Precedences{j in Jobs, u in Units: u!=1}:
  start[j,u] >= finish[j,u-1];

s.t. Sequencing{j1 in Jobs, j2 in Jobs, u in Units}:
  start[j2,u] >= finish[j1,u] - M * (1-before[j1,j2]);
  
s.t. Sequencing2{j1 in Jobs, j2 in Jobs:j1!=j2}:
  before[j1,j2] + before[j2,j1]=1;

s.t. MakespanSetter{j in Jobs}:
  makespan>=finish[j,unitCount];

# Objective function
minimize Makespan: makespan;

# Display
solve;

/*
for{p in 0 .. jobCount-1}
{
  for {j in Jobs: sum{j2 in Jobs : j2!=j} before[j2,j] == p}
  {
    printf "Job %2d: ",j;
    for{u in Units}
    {
      printf "U%d: %g-%g\t",u,start[j,u],finish[j,u];
    }
    printf "\n";
  }
}
*/

printf "<svg height='%d' width='%g'>\n",10*unitCount, makespan*10;

for{j in Jobs, u in Units}
{
  printf "\t<rect x='%g' y='%g' width='%g' height='%g'"  
  ,start[j,u]*10,(u-1)*10+1,proctime[j,u]*10, 8;
  
  printf " style='fill:rgb(%d,%d,%d);stroke:black;stroke-width:1'/>\n",
  j/jobCount*255, 255-j/jobCount*255, 100+j/jobCount*100;
}


printf "</svg>";



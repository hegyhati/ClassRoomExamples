set Tasks;
param arrival_time{Tasks} >=0;
param processing_time{Tasks} >=0;   

param machine_count >=0, integer;
set Machines:= 1..machine_count;

param M := sum{t in Tasks} (arrival_time[t]+processing_time[t]);

var starting_time{Tasks} >=0;

set TaskPairs := setof{t1 in Tasks,t2 in Tasks: t1<t2} (t1,t2);
var preceeds{TaskPairs} binary;

var assign{Tasks,Machines} binary;

var makespan>=0;

s.t. CanNotStartTooEarly{t in Tasks}:
    starting_time[t] >= arrival_time[t];

s.t. SetMakespan{t in Tasks}:
    makespan >= starting_time[t] + processing_time[t];


s.t. BigMFirst{(t1,t2) in TaskPairs, m in Machines}:
    starting_time[t2]>=starting_time[t1]+processing_time[t1]
        -M*(3-preceeds[t1,t2]-assign[t1,m]-assign[t2,m]);

s.t. BigMSecond{(t1,t2) in TaskPairs, m in Machines}:
    starting_time[t1]>=starting_time[t2]+processing_time[t2]
        -M*(3-(1-preceeds[t1,t2])-assign[t1,m]-assign[t2,m]);


s.t. SingleMachineAssignment{t in Tasks}:
    sum{m in Machines} assign[t,m]=1;

minimize Makespan : makespan;

solve;

param id{t in Tasks} := sum{tt in Tasks : tt<t} 1;
param height := 40;
param gap := 5;
param barheight:=height-2*gap;
param tuwidth:=40;
param border:=10;
param textoffset:=3;


printf "<svg height='%d' width='%g'>\n",height*card(Machines)+2*border, makespan*tuwidth + 2*border;

printf "<line x1='%d' y1='%d' x2='%d' y2='%d' style='stroke:rgb(0,0,0);stroke-width:5' />", 
    border, height*card(Machines)+border,makespan*tuwidth+border, height*card(Machines)+border;
printf "<line x1='%d' y1='%d' x2='%d' y2='%d' style='stroke:rgb(0,0,0);stroke-width:5' />", 
    border, height*card(Machines)+border,border, border;

for{t in Tasks, m in Machines:assign[t,m]==1}
{
  printf "\t<rect x='%g' y='%g' width='%g' height='%g'"  
  ,border+starting_time[t]*tuwidth,border+(m-1)*height+gap,processing_time[t]*tuwidth, barheight;
  
  printf " style='fill:rgb(%d,%d,%d);stroke:black;stroke-width:1'/>\n",
  id[t]/card(Tasks)*100, 50 + id[t]/card(Tasks)*50, 30+id[t]/card(Tasks)*100;

  printf "<text x='%d' y='%d' fill='white;bold'>",border+starting_time[t]*tuwidth+textoffset, border+m*height-gap-textoffset;
  printf "%s: %d-%d",t,starting_time[t],starting_time[t]+processing_time[t];
  printf "</text>";
}


printf "</svg>";

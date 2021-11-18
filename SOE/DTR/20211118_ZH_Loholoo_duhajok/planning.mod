set Runners;
param max_distance{Runners};

param weeks;
set Weeks := 1..weeks;
param attendance{Runners,Weeks} binary, default 0;

set Routes;
param distance{Routes};
param max_occurence;

var select{Weeks,Routes} binary;

s.t. One_route_a_week{w in Weeks}:
    sum{r in Routes} select[w,r] = 1;

s.t. Max_occurence_for_each_ruote{r in Routes}:
    sum{w in Weeks} select[w,r] <= max_occurence;

s.t. Only_compattible_rouotes{r in Runners}:
    sum{w in Weeks : attendance[r,w]==1}
    sum{c in Routes: distance[c] > max_distance[r]}
    select[w,c] = 0
    ;

maximize TotalDistance:
    sum{w in Weeks, r in Routes} select[w,r] * distance[r];

solve;

for {w in Weeks, c in Routes: select[w,c]==1}:
{
    printf "Week %d: %s (%g km)\n  ",w,c,distance[c];
    for {r in Runners : attendance[r,w]==1}
        printf "%s (%g km) ",r,max_distance[r];
    printf "\n";
}


end;
     
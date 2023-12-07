set ChallengeTypes;
param challengeCount;

set Challenges := 1..challengeCount;

param type{Challenges} symbolic in ChallengeTypes;
param distanceToNext{Challenges} >= 0; # km

param timeLimit >= 0; # h

set Students;

param speed{Students} >= 0; # km/h
param solutionTime{Students,ChallengeTypes} >= 0; # min

var difficulty{Challenges} >= 1, <= 10, integer;
var finishTime{Students} >= 0; # calculated, in hours
var minTime >= 0;
var maxTime >= 0;


s.t. FinishTime{s in Students}:
    finishTime[s] 
    = 
        sum{c in Challenges} (
            distanceToNext[c] / speed[s] # walking time 
            + 
            solutionTime[s,type[c]] * (1 + 0.1 * (difficulty[c] - 5)) / 60 # solving time (minutes converted to hours)
        )
    ;

s.t. CompletionTimeBoundsMin{s in Students}:
    minTime <= finishTime[s];
s.t. CompletionTimeBoundsMax{s in Students}:
    finishTime[s] <= maxTime;

minimize MaxDifference: maxTime - minTime;

solve;

printf "Min time: %f\n", minTime;
printf "Max time: %f\n", maxTime;
printf "Max difference: %f\n", maxTime - minTime;

for {s in Students} {
    printf "Student %s: %f\n", s, finishTime[s];
}

for {c in Challenges} {
    printf "Challenge %s: %s %d\n", c, type[c], difficulty[c];
}

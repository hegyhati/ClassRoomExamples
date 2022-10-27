set Musclegroup;
set Exercise;

param effect{Exercise, Musclegroup} >= 0; /* J */
param duration{Exercise} >= 0; /* s */
param min_effect{Musclegroup} >= 0; /* J */
param max_effect{Musclegroup} >= 0; /* J */

var repetition{Exercise} >= 0, integer; /* - */

s.t. Min_effect_for_musclegroups{m in Musclegroup}: /* J */
  sum{e in Exercise} repetition[e] * effect[e,m] >= min_effect[m];

s.t. Max_effect_for_musclegroups{m in Musclegroup}: /* J */
  sum{e in Exercise} repetition[e] * effect[e,m] <= max_effect[m];

minimize TotalTrainingTime:
    sum{e in Exercise} repetition[e] * duration[e];



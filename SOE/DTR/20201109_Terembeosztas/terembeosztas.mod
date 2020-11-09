set Rooms;
param capacity{Rooms} >=0, integer;
param fee{Rooms} >= 0;

set Courses;
param hours{Courses} >=0, integer;
param students{Course} >=0, integer;

param dailyHours >=0, integer;







var assign{Courses, Rooms} binary;












s.t. OneCourseToOneRoom{c in Courses}:
    sum{r in Rooms} assign[c,r]=1;

s.t. OnlyIfEnoughCapacity{c in Courses, r in Rooms: students[c] > capacity[r]}:
    assign[c,r]=0;

s.t. RedundantWithThePrevious{c in Courses, r in Rooms}:
capacity[r] >= students[c] - M * (1-assign[c,r])



s.t. DontExceedDailyLimit{r in Rooms}:
    sum{c in Courses} assign[c,r] * hours[c] <= dailyHours;

minimize TotalCost: 
    sum{c in Courses, r in Rooms} hours[c]*fee[r]*assign[c,r]

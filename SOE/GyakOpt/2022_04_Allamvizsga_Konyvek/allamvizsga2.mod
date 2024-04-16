# Input data
set People;
set Courses;
param beer{People,Courses} >= 0;

# Variables = Decisions
var do{People,Courses} binary;

# Constraints

s.t. Do_each_course_once{c in Courses}:
    sum{p in People} do[p,c] = 1;

s.t. Everyone_does_2_courses{p in People}:
    sum{c in Courses} do[p,c] = 2;

minimize Beer_cost:
    sum{p in People, c in Courses} beer[p,c] * do[p,c];

solve;

/*
for {p in People}
{
    printf "%s:\n" , p;
    for {c in Courses : do[p,c]==1}
        printf " - %s (%g)\n", c, beer[p,c];
}
*/

printf "{\n";
for {p in People}
{
    printf '" %s" :[' , p;
    for {c in Courses : do[p,c]==1}
        printf ' "%s" , ', c, beer[p,c];
    printf "]\n";
}

printf "}\n";

end;

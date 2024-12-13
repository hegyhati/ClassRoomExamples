# Modified model to minimize time "spent" in the camp


set Lecturers;
set Groups;

param classes{Groups, Lecturers} >= 0 integer;

param classCount >= 1 integer;
set Classes := 1.. classCount;

param start{Classes};

param classDuration >= 0;
param M := max{c in Classes} start[c] + classDuration;


var teach{Lecturers, Groups, Classes} binary;
var arrive{Lecturers};
var depart{Lecturers};


s.t. Must_teach_each_class{l in Lecturers, g in Groups}:
    sum{c in Classes} teach[l,g,c] = classes[g,l];

s.t. Exactly_on_class_taught_at_a_time_for_a_group{c in Classes, g in Groups}:
    sum{l in Lecturers} teach[l,g,c] = 1;

s.t. At_most_one_class_is_taught_by_a_lecturer_at_a_time{c in Classes, l in Lecturers}:
    sum{g in Groups} teach[l,g,c] <= 1;

s.t. Lecturer_must_arrive_before_taught_class{l in Lecturers, c in Classes}:
    arrive[l] <= start[c] + M * (1 - sum{g in Groups}teach[l,g,c]);

# Could be the same as above, but a different approach:
s.t. Lecturer_must_depart_after_taught_class{l in Lecturers, c in Classes, g in Groups}:
    depart[l] >= (start[c] + classDuration) * teach[l,g,c];

# Not necessary but makes it faster
s.t. Must_depart_later_than_arriving{l in Lecturers}:
    depart[l] >= arrive[l];

minimize TotalPresence:
    sum{l in Lecturers} (depart[l]-arrive[l]);

solve;

printf "\n\n                       ";
for {g in Groups}
    printf " %12s",g;
printf "\n";

for {c in Classes}
{
    printf "  Class %d: %5.2f-%5.2f ", c, start[c], start[c]+classDuration;
    for {g in Groups} 
        for {l in Lecturers : teach[l,g, c] = 1} 
            printf " %12s", l;
    printf "\n";
}
printf "\n\n";

for {l in Lecturers}
    printf "%12s: %5.2f-%5.2f  => %5.2f hours\n", l, arrive[l], depart[l], depart[l]-arrive[l];









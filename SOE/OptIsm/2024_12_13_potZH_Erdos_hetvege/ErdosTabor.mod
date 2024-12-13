set Lecturers;
set Groups;

param classes{Groups, Lecturers} >= 0 integer;

param dayCount >= 1 integer;
set Days := 1.. dayCount;

param classCount{Days} >= 0 integer;

set Classes := setof{d in Days, c in 1..classCount[d]}(d,c);


var teach{Lecturers, Groups, Classes} binary;
var nights{Lecturers} >= 0 integer;


s.t. Must_teach_each_class{l in Lecturers, g in Groups}:
    sum{(d,c) in Classes} teach[l,g,d,c] = classes[g,l];

s.t. Exactly_on_class_taught_at_a_time_for_a_group{(d,c) in Classes, g in Groups}:
    sum{l in Lecturers} teach[l,g,d,c] = 1;

s.t. At_most_one_class_is_taught_by_a_lecturer_at_a_time{(d,c) in Classes, l in Lecturers}:
    sum{g in Groups} teach[l,g,d,c] <= 1;

s.t. Lecutrers_must_sleep_between_taught_classes_on_diffent_days{l in Lecturers, (d1,c1) in Classes, (d2,c2) in Classes: d2 > d1}:
    nights[l] >= (d2-d1) - dayCount * ( 2 - sum{g in Groups} teach[l,g,d1,c1]  - sum{g in Groups} teach[l,g,d2,c2] );

minimize TotalNights:
    sum{l in Lecturers} nights[l];

solve;

printf "\n\n";
for {d in Days}
{
    printf "Day %d     ", d;
    for {g in Groups}
        printf " %12s",g;
    printf "\n";

    for {(d,c) in Classes}
    {
        printf "  Class %d ", c;
        for {g in Groups} 
            for {l in Lecturers : teach[l,g,d,c] = 1} 
                printf " %12s", l;
        printf "\n";
    }
    printf "\n";
}
printf "\n\n";
printf "Nights needed:\n";
for {l in Lecturers : nights[l] > 0}
    printf " - %d for %s\n", nights[l], l;









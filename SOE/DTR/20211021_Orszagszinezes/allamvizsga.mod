set Students;
set Classes;

param hours{Students,Classes};

var prepare{Students,Classes} binary;
var max_load >= 0;

s.t. Meg_kell_csinalni_a_targyat{class in Classes}:
    sum{student in Students} prepare[student,class] = 1;

s.t. Maximum_terheles{student in Students}:
    sum{class in Classes} hours[student,class] * prepare[student,class]
    <=
    max_load
    ;

minimize Maximal_load: max_load;

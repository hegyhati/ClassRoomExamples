set Courses := T1 T2 T3;

param:
      credits examday:=
  T1  4       8
  T2  2       5
  T3  6       9
  ;

set Grades:= 2 3 4 5;

param contextSwitchTime := 0.5;

param studyhours (tr) :
            T1  T2  T3:=
        2   1   3   5 
        3   2   8   5 
        4   3   12  6 
        5   4   20 20
        ;

param freetime :=
  1 3
  2 5
  3 2
  4 8
  5 4
  6 1
  7 3
  8 9
  ; 



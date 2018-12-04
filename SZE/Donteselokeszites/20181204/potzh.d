set Classes := 
  T1
  T2
  T3
  T4
  T5
  T6
;

param:
      credit  hours := 
  T1  2       8
  T2  4       12
  T3  5       9
  T4  6       15
  T5  2       6
  T6  4       13
;

param examNumber := 4;

param examDay (tr) :
          T1  T2  T3  T4  T5  T6:=
      1   1   3   5   3   6   3
      2   2   8   5   4   7   6
      3   3   12  6   10  8   9
      4   4   14  10  12  9   12
      ;


param dayCount := 14;

param freetime:=
  1 6
  2 7
  3 8
  4 9
  5 3
  6 6
  7 9
  8 1
  9 8
  10  6
  11  12
  12  9
  13  5
  14  10
  ;

param warmup := 0.5;




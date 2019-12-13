param dayCount := 30;

param: freetime rain :=
1	2.1	1
2	1.5	0
3	6.6	0
4	2.4	1
5	1.6	0
6	5.6	0
7	0	1
8	6.1	1
9	4.8	1
10	4.9	0
11	2.7	1
12	0	0
13	4.8	1
14	6	0
15	7	1
16	2.3	0
17	7.7	0
18	4.5	1
19	8	1
20	1.7	0
21	4.2	1
22	0	1
23	6.4	0
24	0.2	1
25	1.5	1
26	0	0
27	6.4	0
28	7.9	1
29	0.5	0
30	2.6	1
;

set Sports := Running Cycling Skating Swimming;
set DrySports := Skating;

param:    speed mindistance overhead :=
Running	  12	  150	        0.5
Skating	  18	  100	        0.7
Cycling	  25	  600	        0.7
Swimming	2.2	  10	        1.2
;

param favorite := Running;

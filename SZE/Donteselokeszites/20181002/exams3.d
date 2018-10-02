set Courses:=
  ExpertSystems
  ComputerNetworks
  Programming
  Finance
  DeceisonSupport
  ;

param nDays := 42;

param:            # []      [day]     [hours]
                    credits exam_day  required_time :=
  ExpertSystems     3       16        40
  ComputerNetworks  6       7         20
  Programming       4       23        40
  Finance           4       25        30
  DeceisonSupport   3       40        50
  ;

param free_time :=
  1	5.3
  2	3.8
  3	8.0
  4	5.5
  5	4.7
  6	4.8
  7	4.5
  8	4.0
  9	6.8
  10	9.5
  11	0.9
  12	0.2
  13	0.8
  14	9.5
  15	5.7
  16	3.5
  17	10.0
  18	2.9
  19	0.3
  20	7.7
  21	0.5
  22	7.3
  23	5.9
  24	7.8
  25	2.2
  26	9.7
  27	0.0
  28	4.3
  29	7.1
  30	3.4
  31	1.6
  32	7.1
  33	6.0
  34	4.6
  35	6.0
  36	6.2
  37	3.1
  38	2.5
  39	4.3
  40	8.7
  41	3.6
  42	5.3
  ;


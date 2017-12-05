set Places := Crydee Moraelin Elvandar CarseJonril Tulan Lan Walinor Hush Natal Bordon; 

set Routes := North East South;

param visit (tr):   North   East    South :=
        Crydee      1       0       0
        Moraelin    1       0       0
        Elvandar    1       0       0
        CarseJonril 1       0       1
        Tulan       0       0       1
        Lan         0       1       1
        Walinor     0       1       0
        Hush        0       1       0
        Natal       0       1       0
        Bordon      0       1       1
        ;


param ordercount:=42;

param :     deadline    weight  place:=
        1	5	6.70	Crydee
        2	5	6.17	Moraelin
        3	4	5.30	Crydee
        4	3	6.81	Moraelin
        5	3	6.08	Elvandar
        6	1	6.21	CarseJonril
        7	2	3.01	Walinor
        8	2	7.52	Hush
        9	4	4.84	Natal
        10	3	4.23	Bordon
        11	1	3.46	Crydee
        12	7	7.32	Moraelin
        13	7	4.71	Elvandar
        14	6	6.28	CarseJonril
        15	7	6.46	Moraelin
        16	3	5.07	Elvandar
        17	5	5.19	CarseJonril
        18	2	5.46	Tulan
        19	4	2.01	Lan
        20	5	6.11	Walinor
        21	1	7.28	Hush
        22	7	6.37	Natal
        23	3	6.96	Elvandar
        24	6	2.09	CarseJonril
        25	2	6.20	Tulan
        26	7	3.90	Lan
        27	1	3.87	CarseJonril
        28	2	7.78	Tulan
        29	5	3.99	Lan
        30	1	4.46	Elvandar
        31	5	6.03	CarseJonril
        32	5	3.96	Tulan
        33	2	3.47	Lan
        34	6	5.72	Walinor
        35	5	7.23	Hush
        36	2	3.57	Elvandar
        37	2	5.19	CarseJonril
        38	1	6.21	Crydee
        39	6	7.03	Moraelin
        40	5	6.93	Elvandar
        41	3	5.35	CarseJonril
        42	4	5.73	CarseJonril
        ;


param capacity:=10;
param slotcount:=7;



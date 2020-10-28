param nCars;
set Cars:=1..nCars;
param dist{Cars} >=0; # tengelytavolsag
param nMount;
set Mounts:=1..nMount;
param maxd; # max tavolsag tengely es lekotesi pont kozott
param mind; # minimum tavolsag ket mountpoint kozott
param M := 2*max{c in Cars} dist[c];

var pos{Mounts} >= 0;
var ok{Cars} binary;
var mount{Cars,Mounts} binary;

s.t. IfNotOKDontMount{c in Cars, m in Mounts}:
	mount[c,m] <= ok[c];

s.t. IfOKMountSomewhere{c in Cars}:
	# Ha ok[c]==1 akkor sum{m in Mounts} mount[c,m]>=1; 
	sum{m in Mounts} mount[c,m] >= ok[c];

s.t. MinimumMountDistance{m in Mounts : m!=1}:
	# A permutaciokat implicit kizarjuk.
	pos[m]-pos[m-1]>=mind;

s.t. IfMountedGoodDistance1{c in Cars, m in Mounts}:
	# Ha c-t az m-hez kotom, akkor a tengelytavolsag es az m tavolsaga jo legyen
	#    pos[m]-2*maxd  <= dist[c] <= pos[m]+2*maxd 
	pos[m]-2*maxd - M*(1-mount[c,m]) <= dist[c];
	
s.t. IfMountedGoodDistance2{c in Cars, m in Mounts}:
	# Ha c-t az m-hez kotom, akkor a tengelytavolsag es az m tavolsaga jo legyen
	#    pos[m]-2*maxd  <= dist[c] <= pos[m]+2*maxd 
	dist[c] <= pos[m]+2*maxd + M*(1-mount[c,m]);

maximize TotalOKCars : sum {c in Cars} ok[c];

solve;

for {m in Mounts}
{
	printf "Mount %d at %d -> [%d,%d]:\n"
		,m,pos[m],pos[m]-2*maxd, pos[m]+2*maxd;
	for{c in Cars : mount[c,m]}
		printf " - Car %d (%d)\n",c,dist[c];
}



data;

param nMount := 3;
param maxd :=20;
param mind := 50;

param nCars:=299;
param dist :=
1	315
2	731
3	722
4	291
5	735
6	728
7	483
8	397
9	721
10	321
11	658
12	365
13	301
14	493
15	380
16	406
17	532
18	282
19	421
20	687
21	348
22	612
23	482
24	383
25	529
26	354
27	720
28	257
29	616
30	436
31	424
32	355
33	378
34	443
35	325
36	435
37	529
38	333
39	419
40	614
41	420
42	641
43	367
44	633
45	656
46	578
47	643
48	528
49	656
50	673
51	732
52	329
53	710
54	387
55	590
56	287
57	617
58	511
59	345
60	730
61	390
62	568
63	742
64	663
65	550
66	642
67	510
68	334
69	590
70	734
71	426
72	674
73	574
74	313
75	407
76	619
77	283
78	420
79	583
80	338
81	447
82	302
83	417
84	298
85	432
86	641
87	496
88	598
89	655
90	689
91	648
92	740
93	491
94	421
95	722
96	655
97	750
98	728
99	408
100	450
101	631
102	614
103	338
104	502
105	653
106	299
107	581
108	373
109	621
110	433
111	601
112	257
113	500
114	318
115	453
116	286
117	584
118	459
119	576
120	626
121	534
122	501
123	570
124	414
125	295
126	664
127	547
128	499
129	741
130	526
131	351
132	450
133	676
134	656
135	328
136	652
137	534
138	479
139	487
140	310
141	516
142	288
143	557
144	509
145	555
146	528
147	478
148	488
149	350
150	414
151	321
152	385
153	518
154	677
155	680
156	461
157	326
158	294
159	286
160	630
161	749
162	361
163	718
164	312
165	556
166	687
167	585
168	373
169	603
170	625
171	717
172	695
173	426
174	280
175	287
176	681
177	691
178	253
179	542
180	503
181	625
182	671
183	379
184	692
185	437
186	413
187	374
188	383
189	533
190	567
191	581
192	460
193	332
194	431
195	370
196	636
197	316
198	396
199	608
200	446
201	559
202	478
203	735
204	713
205	629
206	546
207	316
208	510
209	617
210	598
211	681
212	282
213	489
214	429
215	747
216	546
217	417
218	374
219	452
220	399
221	640
222	589
223	578
224	647
225	574
226	387
227	450
228	523
229	587
230	365
231	599
232	457
233	524
234	733
235	391
236	307
237	385
238	399
239	670
240	568
241	722
242	529
243	268
244	463
245	669
246	704
247	326
248	617
249	250
250	471
251	683
252	726
253	713
254	530
255	535
256	470
257	418
258	632
259	388
260	397
261	254
262	609
263	380
264	536
265	526
266	465
267	477
268	612
269	701
270	284
271	270
272	257
273	561
274	586
275	540
276	681
277	717
278	514
279	748
280	669
281	670
282	381
283	594
284	461
285	498
286	579
287	378
288	707
289	712
290	258
291	652
292	553
293	348
294	431
295	394
296	464
297	656
298	582
299	417
;

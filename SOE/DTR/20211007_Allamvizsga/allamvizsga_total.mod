var KV1 binary; var DV1 binary; var GV1 binary; 
var KV2 binary; var DV2 binary; var GV2 binary; 
var KTI binary; var DTI binary; var GTI binary; 
var KVG binary; var DVG binary; var GVG binary; 
var KDR binary; var DDR binary; var GDR binary; 
var KOA binary; var DOA binary; var GOA binary; 
var KKG binary; var DKG binary; var GKG binary; 

s.t. Klau_min:
    KV1 + KV2 + KTI + KVG + KDR + KOA + KKG >=2; 

s.t. Klau_max:
    KV1 + KV2 + KTI + KVG + KDR + KOA + KKG <=3; 

s.t. Dia_min:
    DV1 + DV2 + DTI + DVG + DDR + DOA + DKG >=2; 

s.t. Dia_max:
    DV1 + DV2 + DTI + DVG + DDR + DOA + DKG <=3;

s.t. Gellert_min:
    GV1 + GV2 + GTI + GVG + GDR + GOA + GKG >=2; 

s.t. Gellert_max:
    GV1 + GV2 + GTI + GVG + GDR + GOA + GKG <=3;

s.t. VIR1:
    KV1 + DV1 + GV1 = 1;

s.t. VIR2:
    KV2 + DV2 + GV2 = 1;

s.t. TermelesInfo:
    KTI + DTI + GTI = 1;

s.t. VallGazd:
    KVG + DVG + GVG = 1;

s.t. DTR:
    KDR + DDR + GDR = 1;

s.t. OptAlg:
    KOA + DOA + GOA = 1;

s.t. KozGaz:
    KKG + DKG + GKG = 1;

# s.t. C_7: 
#   x17+x27+x37=1

# s.t. Kozgazdasagtan_jegyzet_pontosan_egyszer:
#   Klau_megcsinalja_kozgaz + Dia_megcsinalja_kozgaz + Gellert_megcsinalja_kozgaz = 1

minimize Osszesora:
10 * KV1 + 12*  DV1+ 21* GV1+  
12 * KV2 + 13*  DV2+ 31* GV2+  
43 * KTI + 14*  DTI+ 41* GTI+  
23 * KVG + 15*  DVG+ 51* GVG+  
12 * KDR + 16*  DDR+ 61* GDR+  
3 * KOA + 17*  DOA+ 71* GOA + 
7 * KKG + 18*  DKG+ 81* GKG
;  

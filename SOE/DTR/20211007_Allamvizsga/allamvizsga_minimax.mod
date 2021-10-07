var KV1 binary; var DV1 binary; var GV1 binary; 
var KV2 binary; var DV2 binary; var GV2 binary; 
var KTI binary; var DTI binary; var GTI binary; 
var KVG binary; var DVG binary; var GVG binary; 
var KDR binary; var DDR binary; var GDR binary; 
var KOA binary; var DOA binary; var GOA binary; 
var KKG binary; var DKG binary; var GKG binary; 

var max_load >= 0;

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


s.t. Max_Klau: 
max_load >= 10 * KV1+12 * KV2+43 * KTI+23 * KVG+12 * KDR+3 * KOA +7 * KKG ;  

s.t. Max_Dia:
max_load >= 12*  DV1+  13*  DV2+  14*  DTI+  15*  DVG+  16*  DDR+  17*  DOA + 18*  DKG;  

s.t. Max_Gellert:
max_load >= 21* GV1+  31* GV2+  41* GTI+  51* GVG+  61* GDR+  71* GOA + 81* GKG;

minimize Maximal_load: max_load;

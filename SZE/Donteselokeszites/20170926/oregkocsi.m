# Adott a het ot napja, valamit 5 autofajta. Minden nap pontosan egy autot szeretnenk megvenni, hogy hetvegere mindegyik tipusbol legyen egy. Adott minden napra minden tipusnak az ara. Hogy vasarolgassunk, hogy minimalis koltseggel megusszuk a dolgot?

var HW binary; var HL binary; var HF binary; var HT binary; var HS binary;
var KW binary; var KL binary; var KF binary; var KT binary; var KS binary;
var SW binary; var SL binary; var SF binary; var ST binary; var SS binary;
var CW binary; var CL binary; var CF binary; var CT binary; var CS binary;
var PW binary; var PL binary; var PF binary; var PT binary; var PS binary;

s.t. Hetfo:
 HW + HL + HF + HT + HS = 1;

s.t. Kedd:
 KW + KL + KF + KT + KS = 1;

s.t. Szerda:
 SW + SL + SF + ST + SS = 1;

s.t. Csutortok:
 CW + CL + CF + CT + CS = 1;

s.t. Pentek:
 PW + PL + PF + PT + PS = 1;


s.t. Wartburg:
 HW + KW + SW + CW + PW = 1;
 
s.t. Lada:
 HL + KL + SL + CL + PL = 1;
 
s.t. Fiat:
 HF + KF + SF + CF + PF = 1;
 
s.t. Trabant:
 HT + KT + ST + CT + PT = 1;
 
s.t. Skoda:
 HS + KS + SS + CS + PS = 1;

minimize Koltsegek:
60000*HW+ 65000*HL+ 61000*HF+ 66000*HT+ 60000*HS+
50000*KW+ 55000*KL+ 63000*KF+ 60000*KT+ 52000*KS+
30000*SW+ 32000*SL+ 33000*SF+ 30000*ST+ 27000*SS+
70000*CW+ 65000*CL+ 77000*CF+ 85000*CT+ 100000*CS+
65000*PW+ 70000*PL+ 75000*PF+ 90000*PT+ 70000*PS;

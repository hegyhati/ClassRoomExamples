var KF >= 0;
var NF >= 0;
var HL >= 0;
var HM >= 0;
var VH >= 0;
var PF >= 0;
var KR >= 0;
var SF >= 0;
var HF >= 0;

s.t. Bor_keszlet_korlatozas:
1*KF + 2*NF + 1*HL + 3*HM + 2*VH + 6*PF + 9*KR + 1*SF + 1*HF <= 1000;

s.t. Szoda_keszlet_korlatozas:
1*KF + 1*NF + 2*HL + 2*HM + 3*VH + 3*PF + 1*KR + 9*SF + 3*HF <= 1500;

maximize Bevetel:
100*KF + 180*NF + 110*HL + 260*HM + 200*VH + 520*PF + 800*KR + 150*SF + 120*HF;

end;
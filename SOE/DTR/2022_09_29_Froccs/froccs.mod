var KF >=0 integer;
var NF >=0 integer;
var HL >=0 integer;

s.t. Bor:
    KF + 2*NF + HL <= 1000;


s.t. Szoda:
    KF + NF + 2*HL <= 1500;

maximize Profit:
    200*KF + 380*NF + 220*HL;

end;

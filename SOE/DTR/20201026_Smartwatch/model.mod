set Parts;
param unit_price{Parts} >=0;

set Groups;
param needs{Groups,Parts} binary, default 0;
param max_price{Groups}>=0;
param size{Groups};

param target_price >=0;
param max_component_price >=0;

var buildin{Parts} binary;
var buy{Groups} binary;

s.t. MaxPartPriceConstraint:
    sum{p in Parts} unit_price[p] * buildin[p] <= max_component_price;

s.t. WillNotBuyIfTooExpensive{g in Groups: target_price>max_price[g]}:
    buy[g]=0;

s.t. WontBuyIfNeededPartIsNotBuiltIn{p in Parts, g in Groups: needs[g,p]==1}:
    buildin[p] >= buy[g];

maximize Profit:
    sum{g in Groups} buy[g]*target_price*size[g];

data;

set Parts := GPS HRM SPO2 ACC NFC ;

param unit_price :=
    GPS 	10000
    HRM 	14000
    SPO2   	13000
    ACC 	20000
    NFC 	12000
;


set Groups := G1	G2	G3	G4	G5	G6;

param needs (tr):
            G1	G2	G3	G4	G5	G6 :=
    GPS	    1	1	1	0	1	0
    HRM	    0	1	1	0	0	0
    SPO2	1	0	0	1	0	0
    ACC	    1	1	0	0	1	1
    NFC	    0	1	0	0	0	0
;



param :
        size    max_price:=
    G1	13665	93000
    G2	13132	86000
    G3	12272	81000
    G4	21528	88000
    G5	14869	87000
    G6	19712	90000
;

param target_price := 87500;
param max_component_price := 36000;

end;

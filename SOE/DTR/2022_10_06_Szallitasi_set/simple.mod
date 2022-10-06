var AD >=0; var AE >=0; var AF >=0; var AG >=0; 
var BD >=0; var BE >=0; var BF >=0; var BG >=0; 
var CD >=0; var CE >=0; var CF >=0; var CG >=0; 

s.t. A_capacity:
    AD + AE + AF + AG <= 50 ;

s.t. B_capacity:
    BD + BE + BF + BG <= 150 ;

s.t. C_capacity:
    CD + CE + CF + CG <= 250 ;

s.t. D_demand:
    AD + BD + CD >= 75 ;

s.t. E_demand:
    AE + BE + CE >= 125 ;

s.t. F_demand:
    AF + BF + CF >= 130 ;

s.t. G_demand:
    AG + BG + CG >= 120 ;

minimize Cost:
+129*AD	+37*AE	+116*AF	+108*AG
+40*BD	+47*BE	+127*BF	+117*BG
+110*CD	+126*CE	+83*CF	+94*CG
;

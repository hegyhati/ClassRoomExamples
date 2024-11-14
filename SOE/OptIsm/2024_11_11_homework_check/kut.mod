set Hazak;
set Kutak;

param napi_vizigeny{Hazak}; # l - d
param max_tarkapacitas{Kutak}; # l - S max
param furas_ara{Kutak}; # $ - p inv
param kapcsolatok{Hazak,Kutak} binary;
param uzemeletetes_koltseg{Kutak}; # $/l/nap - p op
param M;
set bunti_kutak within Kutak;
param bunti_limit;
param bunti_koltseg;

var megepitve{Kutak} binary; # build
var hazhoz_eljutott_viz{Hazak, Kutak} >= 0; # t  l/nap
var elszallitott_viz{Kutak} >= 0; # S w l/nap
var van_e_bunti binary;


s.t. minden_haz_kap_eleg_vizet {h in Hazak}:
    sum {k in Kutak} hazhoz_eljutott_viz[h,k] >= napi_vizigeny[h];

s.t. nem_szallitunk_tul_egy_kutbol {k in Kutak}:
    sum {h in Hazak} hazhoz_eljutott_viz[h,k] <= elszallitott_viz[k];

s.t. max_kapacitas {k in Kutak}:
    elszallitott_viz[k] <= max_tarkapacitas[k] * megepitve[k];

s.t. mindenki_a_maga_kutjat_hasznalja {h in Hazak, k in Kutak: kapcsolatok[h,k] == 0}:
    hazhoz_eljutott_viz[h,k] = 0;

s.t. haha_bunti:
    sum {k in bunti_kutak} elszallitott_viz[k] <= bunti_limit + M * van_e_bunti;

minimize koltseg:
    (sum{ k in Kutak}megepitve[k] * furas_ara[k]) 
    + 
    (sum{k in Kutak} elszallitott_viz[k] * uzemeletetes_koltseg[k]) * 365
    +
    bunti_koltseg * van_e_bunti
    ;

solve;

end;
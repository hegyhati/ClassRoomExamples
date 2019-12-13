/*

Szenvedélyünk a gyerekkorunkat meghatározó autók gyűjtése. Öt egymást követő napon tervezünk
vásárolni egy Trabantot, egy Ladát, egy Wartburgot, egy Skodát, valamint egy Kispolskit. Minden nap
pontosan egy autóval szeretnénk meglepni magunkat, azonban az autók ára a világpiaci helyzettől
függően naponta változik az alábbi táblázatban prognosztizált módon. Milyen sorrendben vásároljuk
meg az autókat, hogy a kollekciónk teljes legyen a lehető legkisebb költségek mellett?

            Hétfő   Kedd    Szerda  Csütörtök   Péntek
Wartburg    60000   65000   61000   66000       60000
Lada        50000   55000   63000   60000       52000
Kispolski   30000   32000   33000   30000       27000
Trabant     70000   65000   77000   85000       100000
Skoda       65000   70000   75000   90000       70000

*/

var WH binary;
var WK binary;
var WS binary;
var WC binary;
var WP binary;

var LH binary;
var LK binary;
var LS binary;
var LC binary;
var LP binary;

var KH binary;
var KK binary;
var KS binary;
var KC binary;
var KP binary;

var TH binary;
var TK binary;
var TS binary;
var TC binary;
var TP binary;

var SH binary;
var SK binary;
var SS binary;
var SC binary;
var SP binary;


s.t. Hetfo:
    WH + LH + KH + TH + SH = 1;
s.t. Kedd:
    WK + LK + KK + TK + SK = 1;
s.t. Szerda:
    WS + LS + KS + TS + SS = 1;
s.t. Csutortok:
    WC + LC + KC + TC + SC = 1;
s.t. Pentek:
    WP + LP + KP + TP + SP = 1;

s.t. Wartburg:
    WH + WK + WS + WC + WP = 1;
s.t. Lada:
    LH + LK + LS + LC + LP = 1;
s.t. Kispolski:
    KH + KK + KS + KC + KP = 1;
s.t. Trabant:
    TH + TK + TS + TC + TP = 1;
s.t. Skoda:
    SH + SK + SS + SC + SP = 1;

minimize totalCost:
60000*WH+   65000*WK+   61000*WS+   66000*WC+   60000*WP+
50000*LH+   55000*LK+   63000*LS+   60000*LC+   52000*LP+
30000*KH+   32000*KK+   33000*KS+   30000*KC+   27000*KP+
70000*TH+   65000*TK+   77000*TS+   85000*TC+   100000*TP+
65000*SH+   70000*SK+   75000*SS+   90000*SC+   70000*SP;

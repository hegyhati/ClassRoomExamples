set dolgozok;

param munkafolyamatok_szama >= 1 integer;
set munkafolyamatok := 1..munkafolyamatok_szama;
param orak_szama;

set orak := 1..orak_szama;

param sebesseg{dolgozok, munkafolyamatok}>=0;
param munkaora <=1 >=0;

param seta_sebesseg{dolgozok} >= 0; # km/h


var dolgozas{orak,dolgozok, munkafolyamatok } binary;
var elorehaladas{orak union {0},munkafolyamatok} >= 0;

param M := sum{d in dolgozok} seta_sebesseg[d];


s.t. csak_egy_feladat{d in dolgozok, o in orak}:
    sum{m in munkafolyamatok} dolgozas[o,d,m]<=1;

s.t. elorehaladas_kezdet{m in munkafolyamatok}:
    elorehaladas[0,m]=0;


s.t. munka_elorehaladas { o in orak, m in munkafolyamatok}:
    elorehaladas[o,m]<=elorehaladas[o-1,m]+ munkaora * sum{d in dolgozok} dolgozas[o,d,m]*sebesseg[d,m];

s.t.  megelozo_folyamat { o in orak, m in munkafolyamatok : m!= 1}:
    elorehaladas[o,m]<= elorehaladas[o, m-1];


# Minden oraban, minden emberre igaz kell, hogy legyen, hogy a maradek 0.25 oraban legyen ideje atmenni oda, ahol a kovetkezo oraban dolgozni fog.

#    A d dolgozo aterjen a megelezo munkafolyamatabol a kovetkezore.
#    Az ido, ami d-nek kell, hogy aterjen az elozobol a kovetkezobe kisebb mint a 0.25 ora alatt tud menni
#    az ido, amig ater <= (1-munkaora) * seta_sebesseg[d]
#    ABS(elorehaladas[ahol most van] - elorehaladas[ahova megy]) <= (1-munkaora) * seta_sebesseg[d]
#    ABS(sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o,d,m] - sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o+1,d,m]) <= (1-munkaora) * seta_sebesseg[d]

# Non-linear, needs further linearization:
# s.t. Legyen_ido_atmenni_1{o in orak, d in dolgozok : o!=orak_szama}:
#     (
#         sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o,d,m] 
#         - 
#         sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o+1,d,m]
#     ) 
#     <= 
#     (1-munkaora) * seta_sebesseg[d]
#     ;
# 
# s.t. Legyen_ido_atmenni_2{o in orak, d in dolgozok : o!=orak_szama}:
#     (
#         sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o+1,d,m]
#         - 
#         sum{m in munkafolyamatok} elorehaladas[o,m] * dolgozas[o,d,m] 
#     ) 
#     <= 
#     (1-munkaora) * seta_sebesseg[d]
#     ;

s.t. Legyen_ido_atmenni{o in orak, d in dolgozok, m_most in munkafolyamatok, m_kov in munkafolyamatok : o!= orak_szama}:
# Ha a d az o vegen az m_most-bol az m_kov-re megy at, akkor legyen ideje....
(if m_kov < m_most then 1 else -1) * elorehaladas[o,m_kov] - elorehaladas[o,m_most] <= (1-munkaora) * seta_sebesseg[d] + M * (2 - dolgozas[o,d,m_most] - dolgozas[o+1, d, m_kov]);



maximize  kesz : elorehaladas[orak_szama,munkafolyamatok_szama];
end;















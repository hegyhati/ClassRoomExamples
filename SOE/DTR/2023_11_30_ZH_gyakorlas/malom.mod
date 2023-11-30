# Szeretnenk minimalis benzinkoltseggel megoldani egy kenyergyar supply chain folyamatat
# Adott nehany mezo, malom, es pek.
# A mezorol a buzat a malmokba, a malmokbol a lisztat a pekekhez kell elszallitani.
# Minden tavolsag adott, valamint adott az egyes mezokon megtermett buza mennyisege, illetve a malmok maximalis kapacitasa kg-ban.
# a benzinfogyasztast ugy kozelitjuk, hogy adott az ures teherautok fogyasztasa, valamint az is, hogy ez a fogyasztas mennyivel no meg minden kg teher utan. A fogyasztas termeszetesen tavolsagaranyos.
# A teherautoknak vissza is kell jonniuk minden szallitas utan.



set Mezo;
set Malom;
set Pek;

param tavolsag {Mezo, Malom};
param tavolsag2 {Malom, Pek};

param buza_mennyiseg {Mezo}; # kg
param malom_kapacitas {Malom}; # kg
param pek_igeny{Pek}; # kg

param benzinfogyasztas; # l/km/kg
param benzinar; # Ft/l

# Dontesek

var szallitott_mennyiseg {Mezo, Malom} >= 0; # kg
var szallitott_mennyiseg2 {Malom, Pek} >= 0; # kg   

# Korlatozasok

s.t. Mezo_korlat {me in Mezo}: 
    sum {ma in Malom} szallitott_mennyiseg[me,ma] <= buza_mennyiseg[me];

s.t. Malom_kapacitas{ma in Malom}:
    sum {me in Mezo} szallitott_mennyiseg[me,ma] <= malom_kapacitas[ma];

s.t. Pek_igeny{pe in Pek}:
    sum {ma in Malom} szallitott_mennyiseg2[ma,pe] >= pek_igeny[pe];

s.t. Malom_egyensuly{ma in Malom}:
    sum {me in Mezo} szallitott_mennyiseg[me,ma] >= sum {pe in Pek} szallitott_mennyiseg2[ma,pe];


# Cel

minimize osszkoltseg: 
    sum {me in Mezo, ma in Malom} tavolsag[me,ma] * szallitott_mennyiseg[me,ma] * benzinfogyasztas * benzinar +
    sum {ma in Malom, pe in Pek} tavolsag2[ma,pe] * szallitott_mennyiseg2[ma,pe] * benzinfogyasztas * benzinar;
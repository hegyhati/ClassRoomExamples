# Halmazok

# froccs tipusok
set Froccsok;

# set Alapanyagok := {bor, szoda};
set Alapanyagok;

# Valtozok

# mibol mennyit adunk el
var mennyit{Froccsok} >= 0, integer;


# Parameterek

# melyik froccsot mennyiert arulunk
param ar{Froccsok} >= 0;

# melyik froccsben mennyi bor es szoda van
# param tartalom{Froccsok,{'bor', 'szoda'}};
param tartalom{Froccsok,Alapanyagok} >= 0;

# mennyi bor es szoda all rendelkezesre
param keszlet{Alapanyagok} >= 0, default 0;


# Korlatozasok

# s.t. Bormennyiseg:
#     sum{f in Froccsok} tartalom[f,bor] * mennyit[f] <= keszlet[bor];

# s.t. Szodamennyiseg:
#     sum{f in Froccsok} tartalom[f,szoda] * mennyit[f] <= keszlet[szoda];

s.t. Keszletkorlat{a in Alapanyagok}:
    sum{f in Froccsok} tartalom[f,a] * mennyit[f] <= keszlet[a];


# Celfuggveny

maximize Profit:
    sum{f in Froccsok} mennyit[f] * ar[f];


data;

set Froccsok := KF NF HL;

set Alapanyagok := bor szoda;

param ar :=
    KF 200
    NF 380
    HL 220
;

param tartalom
    : bor szoda :=
    KF  1   1
    NF  2   1
    HL  1   2
;

param keszlet :=
    bor 1000
    szoda 1500
;

end;

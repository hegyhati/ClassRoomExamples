# Vizsgaeredmenyek maximalizalasa

## Halmazok

set Targyak := {'Prog', 'Kozgaz', 'Angol'};
set Napok := 1..10;

## Parameterek

# Targyak napja
param vizsgaNap{Targyak} integer;

# Targyak krediterteke
param kredit{Targyak} integer, default 4;

# Mennyi ido kell a felkeszulesre adott targybol
param szuksIdo{Targyak}, default 15;

# Napi szabadido
param szabadIdo{Napok}, default 4;


## Valtozok

# Adott napon adott targybol hany orat tanulunk
var tanulas{Napok, Targyak} >= 0;

# Elmegyunk-e egy vizsgara
var elmegyunk{Targyak} binary;

## Cel: az elert kreditek osszeget maximalizalni
maximize eredm: sum{t in Targyak} kredit[t] * elmegyunk[t];

## Korlatozasok

# Korlatos szabadido
s.t. Szabadido{n in Napok}:
    szabadIdo[n] >= sum{t in Targyak} tanulas[n, t];

# Minden targybol maximum annyit tanuljunk, amennyi szukseges
s.t. SzuksegesIdo{t in Targyak}:
    szuksIdo[t] >= sum{n in Napok} tanulas[n,t];

# Csak akkor megyunk vizsgazni, ha eleget keszultunk
# elmegyunk == sikeresVizsga
s.t. CsakSikeresVizsga{t in Targyak}:
    elmegyunk[t] <= sum{n in Napok: n < vizsgaNap[t]} tanulas[n,t] / szuksIdo[t];

# +1: 5 napnal regebbre nem emlekszunk
s.t. CsakSikeresVizsga{t in Targyak}:
    elmegyunk[t] <= sum{n in Napok: n < vizsgaNap[t] and n >= vizsgaNap[t] - 5 } tanulas[n,t] / szuksIdo[t];

#TODO
#s.t. JegyhezSzuksIdo{t in Targyak, j in Jegyek}:
#    szerzunk[t,j] <= sum{n in Napok: n < vizsgaNap[t]} tanulas[n,t] / szuksIdo[t,j];


data;

param vizsgaNap :=
    'Prog' 7
    'Kozgaz' 8
    'Angol' 10
;

param szabadIdo :=
    4 7
    5 8
;
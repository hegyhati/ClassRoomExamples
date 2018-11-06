# Szeretnenk minimalis benzinkoltseggel megoldani egy kenyergyar supply chain folyamatat
# Adott nehany mezo, malom, es pek.
# A mezorol a buzat a malmokba, a malmokbol a lisztat a pekekhez kell elszallitani.
# Minden tavolsag adott, valamint adott az egyes mezokon megtermett buza mennyisege, illetve a malmok maximalis kapacitasa kg-ban.
# a benzinfogyasztast ugy kozelitjuk, hogy adott az ures teherautok fogyasztasa, valamint az is, hogy ez a fogyasztas mennyivel no meg minden kg teher utan. A fogyasztas termeszetesen tavolsagaranyos.
# A teherautoknak vissza is kell jonniuk minden szallitas utan.


set Mezo;
set Malom;
set Pek;

param tav1{Mezo,Malom}; #km
param tav2{Malom,Pek}; #km

param orlesarany;
param teherautokapacitas; #kg

param buza{Mezo}; #kg
param kapacitas{Malom}; #kg

param ures_fogyasztas; # l / 100 km
param valtozo_fogyasztas; # l / kg / 100 km

param benzinar; # Ft / 100 km

# Valtozok

var fuvar1{Mezo,Malom}, integer, >=0;
var szallit1{Mezo,Malom} >=0;
var fuvar2{Malom,Pek}, integer, >=0;
var szallit2{Malom,Pek} >=0;

# Korlatozasok

s.t. MindenMezorolAmennyiVan{mezo in Mezo}:
    sum{malom in Malom} szallit1[mezo,malom] = buza[mezo];

s.t. EgyMalombaMaxAmennyitElbir{malom in Malom}:
    sum{mezo in Mezo} szallit1[mezo,malom] <= kapacitas[malom];

s.t. MalombolMindentElszallit{malom in Malom}:
    orlesarany * sum{mezo in Mezo} szallit1[mezo,malom] = sum{pek in Pek} szallit2[malom,pek];

s.t. Teherautokszama1{mezo in Mezo, malom in Malom}:
    fuvar1[mezo,malom] * teherautokapacitas >= szallit1[mezo,malom];

s.t. Teherautokszama2{malom in Malom, pek in Pek}:
    fuvar2[malom,pek] * teherautokapacitas >= szallit2[malom,pek];

# Celfuggveny

minimize Benzinkoltseg: benzinar * (
    sum{mezo in Mezo, malom in Malom} tav1[mezo,malom] *
        (2 * ures_fogyasztas*fuvar1[mezo,malom] + szallit1[mezo,malom]*valtozo_fogyasztas)
    + 
    sum{malom in Malom, pek in Pek} tav2[malom,pek] *
        (2 * ures_fogyasztas*fuvar2[malom,pek] + szallit2[malom,pek]*valtozo_fogyasztas)
    )/100;

solve;



printf "\n\t";
for{malom in Malom} printf "%s\t",malom;
printf "\n";
for{mezo in Mezo}
{
    printf "%s\t", mezo;
    for{malom in Malom} printf "%d(%.0f)\t",fuvar1[mezo,malom],szallit1[mezo,malom];
    printf "\n";
}

printf "\n\t";
for{pek in Pek} printf "%s\t",pek;
printf "\n";
for{malom in Malom}
{
    printf "%s\t", malom;
    for{pek in Pek} printf "%d(%.0f)\t",fuvar2[malom,pek],szallit2[malom,pek];
    printf "\n";
}


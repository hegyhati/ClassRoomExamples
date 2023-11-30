/*
Egy bringás futárcégnek dolgozunk be szabadúszóként. 8 órát tervezünk tekerni, méghozzá olyan módon, hogy minden órában néhány jól bejáratott kör egyikére megyünk el, miközben az útvonalhoz közel eső helyekre kézbesítünk csomagokat. A futárcég egy csomaglistát bocsát rendelkezésünktre, amiből mi eldönthetjük, hogy melyikeket vállaljuk el, és melyikeket nem. Minden csomaghoz adott egy kézbesítési határidő, valamint a kiszállítás címe, ami vagy rajta van valamelyik útvonalunkon, vagy nincs. Ismert továbbá a csomagok tömege.

Hogy semmiképp ne csússzunk meg, sosem viszünk el egy körre 5-nél több csomagot, vagy tekerünk 10 kilónál több teherrel. Mindemellett, hogy tényleg biztosra menjünk, csak akkor viszünk el egy körre egy csomagot, ha annak a kézbesítési határideje később van, minthogy azt a kört befejeznénk. A késő kézbesítésekért ugyanis a futárcégnek díjat kell fizetnie, amit aztán rajtunk ver le kamatostul.

Célunk az, hogy ez alatt a 8 óra alatt maximalizáljuk  a kiszállított csomagok számát.

*/

set Utvonalak;
set Cimek;
param erinti{Utvonalak,Cimek} binary;
set ErintettCimek{u in Utvonalak} within Cimek := setof {c in Cimek : erinti[u,c] == 1} c;
# pythonban igy lenne: erinti = { {c for c in Cimek if erinti[u,c] == 1} for u un Utvonalak}


param csomagszam >= 0, integer;
set Csomagok := 1..csomagszam;
param tomeg{Csomagok} >=0; #kg
param hatarido{Csomagok} >=0; #óra
param cim{Csomagok} symbolic in Cimek;

param korok >= 0, integer; 
set Korok:= 1..korok;
param teherbiras >= 0; #kg
param max_csomagszam >= 0, integer;


# Dontesek

var elvisz{Csomagok,Korok} binary;
var megy{Utvonalak,Korok} binary;

# Korlatozasok

s.t. Egy_korben_egy_utvonalra_megyunk_pontosan{k in Korok}: sum{u in Utvonalak} megy[u,k] = 1;

s.t. Egy_csomagot_legfeljebb_egyszer_szallitunk_ki{c in Csomagok}: sum{k in Korok} elvisz[c,k] <= 1;

s.t. Egy_korben_nem_vihetek_tobb_csomagot_mint_a_maximum{k in Korok}: sum{c in Csomagok} elvisz[c,k] <= max_csomagszam;

s.t. Egy_korben_nem_cipelhetek_tobb_tomeget_mint_a_teherbirasom{k in Korok}: sum{c in Csomagok} elvisz[c,k] * tomeg[c] <= teherbiras;

/*
 Keson nem vihetunk ki csomagot
 aktualis kor >= hatarido akkor elvisz[cs,k] = 0
*/

s.t. Keson_nem_szallitunk_ki_csomagot{c in Csomagok, k in Korok: k >= hatarido[c]}: elvisz[c,k] = 0;

/*
    Olyan csomagot nem vihetek el, ami az aktualisan valasztott koron nincs rajta
    Ha az aktualisan valasztott koron nincs rajta a csomag, akkor nem vihetem el
    Ha c nem eleme ErintettCimek[u] az aktualis u-ra,  akkor elvisz[c,u] = 0
    Ha megy[u,k] == 1 es einti[u,c]==0 akkor elvisz[c,k] = 0
    elvisz[c,k] <= 2 - megy[u,k] - ( 1 - erinti[u,c])
*/

# s.t. Csak_olyan_csomagot_vihetek_el_ami_az_aktualis_koron_van{c in Csomagok, k in Korok, u in Utvonalak}: elvisz[c,k] <= 2 - megy[u,k] - (1-erinti[u,cim[c]]);

# s.t. Csak_olyan_csomagot_vihetek_el_ami_az_aktualis_koron_van_2{c in Csomagok, k in Korok, u in Utvonalak:erinti[u,cim[c]]==0}: elvisz[c,k] + megy[u,k] <=1;


/*
    Ha egy csomagot elviszek, akkor olyan korre kell mennem, amelyiken rajta van
    Ha elvisz[c,k] == 1 akkor megy[u,k] == 1 valamely u-ra, amelyre erinti[u,c] == 1
    Ha elvisz[c,k] == 1 akkor sum{u in Utvonalak : erinti[c,u]==1} megy[u,k] == 1 
    sum{u in Utvonalak : erinti[c,u]==1} megy[u,k] == 1  >= elvisz[c,k]
*/

# s.t. Ha_elviszek_egy_csomagot_akkor_neki_megfelelo_utvonalra_kell_mennem{c in Csomagok, k in Korok}: 
#    sum{u in Utvonalak : erinti[u,cim[c]]==1} megy[u,k] >= elvisz[c,k];

set ErintoUtvonalak{c in Csomagok} := setof {u in Utvonalak : erinti[u,cim[c]]==1} u;

s.t. Ha_elviszek_egy_csomagot_akkor_neki_megfelelo_utvonalra_kell_mennem_2{c in Csomagok, k in Korok}: 
    sum{u in ErintoUtvonalak[c]} megy[u,k] >= elvisz[c,k];

# Celfuggveny

maximize KiszallitottCsomagokSzama: sum{c in Csomagok, k in Korok} elvisz[c,k];

solve;

for {k in Korok}
{
    printf "Kor %d:", k;
    for {u in Utvonalak: megy[u,k]==1}
    {
        printf " Utvonal %s\n", u;
        for {c in Csomagok: elvisz[c,k]==1}
        {
            printf " - Csomag %d (%s, %g kg, Deadline: %d)\n", c, cim[c], tomeg[c], hatarido[c];
        }
    }
}

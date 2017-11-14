set Kutak;
set Hazak;

param epitesi_ktg{Kutak};			# [millio dh]
param fenntartasi_ktg{Kutak};		# [ezer dh/ev]
param ellat{Hazak, Kutak}, binary;	# egy hazat ellat-e vizzel az adott kut

param idotav;						# [ev]

# elozo Pareto-optimalis megoldas celfuggveny-erteke a masik cel szerint
param max_fenntartas default sum{k in Kutak} fenntartasi_ktg[k];

var megepit{Kutak}, binary;

s.t. MindenkitEllatunk{h in Hazak}:
	sum{k in Kutak} megepit[k] * ellat[h,k] >= 1;

# az elozo Pareto-optimalisnal jobb legyen a masik szempont szerint
s.t. AlacsonyabbFenntartas:
	sum{k in Kutak} megepit[k] * (fenntartasi_ktg[k]) <= max_fenntartas;

# Celfuggveny

minimize BeruhazasiKtg: sum{k in Kutak} megepit[k] * epitesi_ktg[k];
#minimize UzemeltetesiKtg: sum{k in Kutak} megepit[k] * (fenntartasi_ktg[k]/1000*idotav);

#minimize AggregaltKtg: sum{k in Kutak} megepit[k] * (epitesi_ktg[k] + fenntartasi_ktg[k]/1000*idotav);

solve;

printf "\nMegepitendo kutak:";
for {k in Kutak : megepit[k]}{
	printf " %s", k;
}
printf "\n";

printf "\nBeruhazasi koltseg: %fM dh\n", sum{k in Kutak} megepit[k] * epitesi_ktg[k];
printf "\nFenntartasi koltseg: %fk dh/ev\n", sum{k in Kutak} megepit[k] * (fenntartasi_ktg[k]);
printf "\nOsszes fenntartasi koltseg: %fM dh\n", sum{k in Kutak} megepit[k] * (fenntartasi_ktg[k]/1000*idotav);
printf "\nAggregalt koltseg: %fM dh\n", sum{k in Kutak} megepit[k] * (epitesi_ktg[k] + fenntartasi_ktg[k]/1000*idotav);

end;

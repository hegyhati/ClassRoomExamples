/*
Feladatunk az éjszakai zenei felhozatal optimális megtervezése a 25. Jubileumi Veszprémi Egyetemi Napok 1-es csapatának, a Luck'VEN'Roll-nak a kocsmájában. A csapat diákrektor jelöltje, Őkoboldsága Vadpocok meghívott néhány prominens vendéget, akiket célunk minél tovább szórakoztatni, ezért a csapat stílusához illő zenék közül gondosan válogatjuk meg a lejátszási listára kerülő számokat. Minden vendégnek ismerjük a zenei ízlését, s tudjuk, hogy a harmadik olyan számnál, amit nem szeretnek, elhagynák a kocsmát. Készítsünk olyan lejátszási listát, melyben a lehető legtöbb szám szerepel úgy, hogy mindegyik vendég a kocsmában maradjon.
*/

set People;
set Tracks;
param like{Tracks,People};

var play{Tracks} binary;

s.t. ShouldntPlayThreeUnlikedSongs{p in People}:
    sum{t in Tracks:like[t,p]==0} play[t] <= 2;

maximize Tracklist: sum{t in Tracks} play[t];

solve;

printf "Tracklist: \n";
for{t in Tracks:play[t]==1}
    printf " - %s\n",t;
printf "\nPeople:\n";
for{p in People}
    printf " - %s (%d)\n",p,sum{t in Tracks:like[t,p]==0} play[t];

data;

set People:= Andi Guszti Patrik Tina Mate;
set Tracks:= Freedom Highway_to_Hell Shipping_up_to_Boston Its_my_life Whisky_in_the_jar Summer_of_69 I_love_R_n_R;

param like:
                        Andi    Guszti  Patrik  Tina    Mate :=
Freedom                 1       1       1       1       1
Highway_to_Hell         1       0       1       0       1
Shipping_up_to_Boston   1       0       0       1       0
Its_my_life             0       1       1       1       0
Whisky_in_the_jar       0       0       0       0       1
Summer_of_69            1       1       0       0       1
I_love_R_n_R            0       1       0       0       0
;   

end;

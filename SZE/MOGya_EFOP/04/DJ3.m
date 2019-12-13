/*
10 szambol allo tracklist

Emberek:
    - szeretik szamot: tancolnak
    - 1. nem szeretett szam: isznak
    - 2. nem szeretett szam: elmennek

Cel: sorfogyasztas maximalizalas

*/

set People;
set Tracks;
param like{Tracks,People};
param trackcount;
set TrackList := 1..trackcount;

var play{Tracks,TrackList} binary;
var dance{People, TrackList}, binary;
var drink{People, TrackList}, binary;
var away{People, TrackList}, binary;

s.t. PlayExactlyOneSong {l in TrackList}:
    sum {t in Tracks} play[t,l]=1;

s.t. ExactlyOneState{l in TrackList, p in People}:
    dance[p,l]+drink[p,l]+away[p,l]=1;

s.t. DoesntDanceIfDoesntLike{p in People, l in TrackList}:
    dance[p,l]<=1-sum{t in Tracks:like[t,p]==0} play[t,l];

s.t. TwoDoesntLikeInARowThenAway{p in People, l in TrackList: l!=1}:
    away[p,l] >= -1 + sum{t in Tracks:like[t,p]==0} play[t,l] + sum{t in Tracks:like[t,p]==0} play[t,l-1];

s.t. OnceAwayAlwaysAway{p in People, l in TrackList: l!=1}:
    away[p,l]>=away[p,l-1];

s.t. IfNotAwayAndLikeThenDance{p in People, l in TrackList}:
    dance[p,l]>=sum{t in Tracks:like[t,p]==1} play[t,l] - away[p,l];

s.t. NotAwayTheFirtTime{p in People}:
    away[p,1]=0;

maximize Tracklist:
    sum{l in TrackList, p in People} drink[p,l];

solve;

printf "%20s"," ";
for{p in People}
    printf "\t%s",p;
printf "\n";
for {l in TrackList}{
    for {t in Tracks:play[t,l]==1}{
        printf "%2d. %16s",l,t;
    }
    for{p in People} {
        for {{0}:dance[p,l]==1} printf "\tDance";
        for {{0}:drink[p,l]==1} printf "\tDrink";
        for {{0}:away[p,l]==1} printf "\tAway";        
    }
    printf "\n";  
}       


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

param trackcount:=5;
end;

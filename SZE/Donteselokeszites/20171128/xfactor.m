set Resztvevok;

param adasok_szama:=card(Resztvevok)-1;

set Adasok := 1..adasok_szama;

param sms{Resztvevok};

var pbe{Adasok,Resztvevok}, binary;
var pki{Adasok,Resztvevok}, binary;

s.t. EgyValakiEsikKi{a in Adasok}:
    sum{r in Resztvevok} pki[a,r] = 1;

s.t. EgyValakiMaradBent{a in Adasok}:
    sum{r in Resztvevok} pbe[a,r] = 1;

#redundans
s.t. EgyValakiNemLehetMindketto{a in Adasok, r in Resztvevok}:
    pki[a,r]+pbe[a,r] <= 1;


s.t. LegfeljebbKetszerGyoz {r in Resztvevok}:
    sum{a in Adasok} pbe[a,r] <= 2;

#redundans
s.t. AkiKiesettKintIsMarad{r in Resztvevok, a in Adasok, av in Adasok: a < av}:
    pki[av,r] <= 1-pki[a,r];

#redundans
s.t. AkiKiesettKintIsMarad2{r in Resztvevok, a in Adasok, av in Adasok: a < av}:
    pbe[av,r] <= 1-pki[a,r];

#redundans
s.t. ElozokettoEgyben{r in Resztvevok, a in Adasok, av in Adasok: a < av}:
    pki[av,r] + pbe[av,r] <= 1-pki[a,r];

s.t. ElozoPluszRegebbiEgyben{av in Adasok, r in Resztvevok}:
    pki[av,r]+pbe[av,r] <= 1 - sum{a in Adasok: a<av} pki[a,r];



# TODO cfv
maximize TotalSMS : sum{a in Adasok, r in Resztvevok} sms[r]*(pki[a,r]+pbe[a,r]);

solve;

printf "\n\n";
for {a in Adasok}
{
    printf "Adas %d: ",a;
    for{r in Resztvevok: pbe[a,r]==1}
        printf "\tBentmarad: %s (%d)",r,sms[r];
    for{r in Resztvevok: pki[a,r]==1}
        printf "\tKiesik: %s (%d)",r,sms[r];
    printf "\n";
}

printf "\n\nOsszes SMS: %d\n\n",TotalSMS;

data;

set Resztvevok := Gizike DJSanyee Rockkati TucTuci MsLady Belaba Maunika Popapi;

param sms:=
    Gizike      12
    DJSanyee    23
    Rockkati    123
    TucTuci     45
    MsLady      369
    Belaba      125
    Maunika     255
    Popapi      1
;

end;

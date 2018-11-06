# Adott a het ot napja, valamit 5 autofajta. Minden nap pontosan egy autot szeretnenk megvenni, hogy hetvegere mindegyik tipusbol legyen egy. Adott minden napra minden tipusnak az ara. Hogy vasarolgassunk, hogy minimalis koltseggel megusszuk a dolgot?

# Data

set Kocsik;
set Napok;

param ar{k in Kocsik,n in Napok};

# Variables
var megvesz{k in Kocsik, n in Napok} binary;

# Constraints

s.t. EgyNapLegfeljebbEgyAuto {n in Napok}:
    sum {k in Kocsik} megvesz[k,n] <= 1;

s.t. MindenKocsibolEgyetSzeretnenk {k in Kocsik}:
    sum {n in Napok} megvesz[k,n] = 1;

# Objective
minimize Koltseg:
    sum{k in Kocsik, n in Napok} megvesz[k,n] * ar[k,n];

solve;

for{k in Kocsik, n in Napok : megvesz[k,n]=1}
{
    printf "A %s-t %s napon vesszuk meg %d Ft-ert.\n",k,n,ar[k,n];
}


end;

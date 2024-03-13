import os
import shutil
from sys import argv

masolando = argv[1]
ujkonyvtar = argv[2]
fajltipusok = argv[3:]

print(fajltipusok)

if os.path.exists(ujkonyvtar):
    print("Mar letezik")
    exit()

os.mkdir(ujkonyvtar)

fajlok = os.listdir(masolando)
for fajl in fajlok:
    if len(fajltipusok) == 0 or os.path.splitext(fajl)[1][1:] in fajltipusok:
        shutil.copy(os.path.join(masolando,fajl),ujkonyvtar)
print(fajlok)

# python3 copy.py base feluletkezeles ods jpg bmp
# python3 copy.py base aramkorok txt odt
# python3 copy.py base dendrologia
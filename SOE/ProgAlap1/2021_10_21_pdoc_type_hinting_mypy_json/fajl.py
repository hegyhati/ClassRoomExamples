soreim = []

with open("sor.txt") as file:
    for sor in file:
        soreim.append(sor[:-1])

print(soreim)

uj_sor = input("Mit iszol eppen? ")
soreim.append(uj_sor)

uj_fajl = open("sor.txt","w")
for sor in soreim:
    uj_fajl.write(sor + "\n")
uj_fajl.close()




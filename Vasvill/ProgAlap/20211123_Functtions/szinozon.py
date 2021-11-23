
# Balint
def helyes_formatumu_tipp(szinek,feladvany_meret,tipp):
    if len(tipp) != feladvany_meret:
        return False, "Nem " + str(feladvany_meret)+ " hosszu a tipp"
    for elem in tipp:
        if elem not in szinek:
            return False, elem + " szin nem letezik."
    return True, "Minden ok."

# Kristof
def tipp_bekerese(szinek, hossz):
    tipp = input("Kerlek add meg a tippedet (pl: p,p,k,p): ").split(",")
    jo,uzenet = helyes_formatumu_tipp(szinek,hossz,tipp) 
    while not jo :
        print("Nem helyes a tipp formatuma: "+uzenet)
        tipp = input("Tipp helyesen: ").split(",")
        jo,uzenet = helyes_formatumu_tipp(szinek,hossz,tipp) 
    return tipp

# Gergo
def kiertekel(feladvany,tipp):
    jo_indexek=[]
    jo_jo_helyen = 0
    for idx in range(len(feladvany)):
        if feladvany[idx] == tipp[idx]:
            jo_jo_helyen+=1
            jo_indexek.append(idx)
    jo_indexek.reverse()
    feladvany=feladvany[:]
    tipp=tipp[:]
    for idx in jo_indexek:
        del feladvany[idx]
        del tipp[idx]
    jo_rossz_helyen = 0
    for szin in szinek:
        jo_rossz_helyen += min(feladvany.count(szin), tipp.count(szin))
    return jo_jo_helyen,jo_rossz_helyen

# Mark
def tipp_beker_kiertekel(szinek,feladvany):
    tipp = tipp_bekerese(szinek,len(feladvany))
    jo_jo_helyen, jo_rossz_helyen = kiertekel(feladvany,tipp)
    print(
        jo_jo_helyen," db jo van jo helyen, es ",
        jo_rossz_helyen, "db jo, de rossz helyen.")
    return tipp


# Zoli
szinlista = ['p','s','z','k','f']
feladvany = ['p','p','k','z'] 

tipp = tipp_beker_kiertekel(szinlista,feladvany)
lepesek=1
while tipp != feladvany:
    tipp = tipp_beker_kiertekel(szinlista,feladvany)
    lepesek+=1
print("Grat, megfejtetted",lepesek,"lepesbol.")

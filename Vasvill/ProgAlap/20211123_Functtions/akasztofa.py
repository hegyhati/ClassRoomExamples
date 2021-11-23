# Gabor
def meg_van_e_fejtve(rejtett_szo, tippelt_betuk):
    for betu in rejtett_szo:
        if betu not in tippelt_betuk:
            return False
    return True

# Lenard
def elet_fancy_kiirasa(eletek_szama, max_elet):
    print(" ♥ " * eletek_szama + " 💀 " * (max_elet-eletek_szama))

# Kevin
def feldvany_fancy_kiirasa(rejtett_szo, tippelt_betuk):
    for betu in rejtett_szo:
        if betu in tippelt_betuk:
            print(betu, end=" ")
        else:
            print("_", end=" ")
    print()


# Levente
def jatekallas_kiiras(rejtett_szo, tippelt_betuk, eletek_szama, max_elet):
    elet_fancy_kiirasa(eletek_szama, max_elet)
    feldvany_fancy_kiirasa(rejtett_szo, tippelt_betuk)

# Attila
feladvany = "focilabda"
eletek = 10
max = eletek
tippek = ['i','a']

while not meg_van_e_fejtve(feladvany,tippek) and eletek > 0: 
    jatekallas_kiiras(feladvany,tippek,eletek,max)
    uj = input("Adj meg egy betut: ") # todo: ismetlest ne engedjen
    if uj not in feladvany:
        eletek-=1
    tippek.append(uj)

if eletek > 0:
    jatekallas_kiiras(feladvany,tippek,eletek,max)
    print("GRATULALOK, megfejtetted! Nyalhat.") # Eretlenek
else:
    print("GAME OVER")



"""
Amig nincs megfejtve es nem haltunk meg:
    Kiirni a jatek allasat
    kerjunk be egy olyan betut ami meg nem volt
    ellenorizzuk a betut:
      - vagy felfedunk valamit
      - vagy elmegy egy eletunk
Ha nem haltunk meg: grat, kulonben : game over
"""

# Kerjen be egy sebesseget km/h-ban, majd irja ki m/s-ban.

def kmh_to_ms(sebesseg):
   return sebesseg / 3.6

def feladat_1():
   sebesseg = float(input("Add meg a sebesseget km/h-ban: "))
   print(sebesseg,"km/h =",kmh_to_ms(sebesseg),"m/s")


### Kerjen be egy sebesseget km/h-ban, majd irja ki a tempot perc/km-ben.

def kmh_to_pace(sebesseg):
   percperkm = 60 / sebesseg
   perc = int(percperkm)
   masodperc = int(60 * (percperkm % 1))
   return perc,masodperc

def feladat_2():
   sebesseg = float(input("Add meg a sebesseget km/h-ban: "))
   tempo = kmh_to_pace(sebesseg)
   print(f"A tempo: {tempo[0]}:{tempo[1]:02}")


### Kerjen be egy szamot, es irja ki a szamjegyeinek osszeget (tizes szamrendszerben).

def szamjegyosszeg(szam):
   osszeg = 0
   while szam != 0:
      osszeg += szam % 10
      szam //= 10
   return osszeg

def szamjegyosszeg2(szamszoveg):
   osszeg = 0
   for szamjegy in szamszoveg:
      osszeg += int(szamjegy)
   return osszeg


def feladat_3():
   szamszoveg = input()
   szam = int(szamszoveg)
   print(szamjegyosszeg(szam))
   print(szamjegyosszeg2(szamszoveg))

### Kerjen be egy szot es irja ki, hogy palindrom-e?

def feladat_4():
   szo = input()
   print("Palindroom" if szo[::-1] == szo else "Nem palindrom")

### Kerjen be egy szamot, es irjon ki annyi `#` jelet egy sorban szokozok nelkul.


def teljessor(db):
   print("#" * db)

def feladat_5():
   db = int(input())
   teljessor(db)



### Kerjen be ket szamot, es rajzoljon ki egy akkora teglalapot `#` karakterekbol.
def feladat_6():
   sz = int(input())
   m = int(input())
   for _ in range(m):
      teljessor(sz)


### Ugyanaz, mint az elozo, csak a teglalap legyen belul ures:


def kozbulsosor(sz):
      print("#", end='')
      print(" " * (sz-2), end='')
      print("#")

def feladat_7():
   sz = int(input())
   m = int(input())
   teljessor(sz)
   for _ in range(m-2):
      kozbulsosor(sz)
   teljessor(sz)

### Egy szamot kerjen be, es egy oylan magas haromszoget irjon ki.

def feladat_8():
   db = int(input())
   for i in range(db):
      teljessor(i+1)

### Hasonlo, csak piramis legyen.

def behuzas(szokoz_db):
   print(" " * szokoz_db, end='')

def feladat_9():
   db = int(input())
   for i in range(db):
      behuzas(db-i)
      teljessor(2*i+1)

feladat_9()
   
# [Python](https://python.org) nyelv főbb tulajdonságai

 - Magas szintű, általános célú programozási nyelv.
 - Alapvetően interpretált nyelv.
 - Dinamikusan típusos nyelv, garbage collector-ral rendelkezik.
 - Több programozási paradigmát is támogat: procedurális, objektum-orientált, funkcionális.
 - Gazdag alapértelmezett modulkönyvtár.
 - 40 éves nyelv, jelenleg a 3-as változat támogatott, mely visszafele nem kompatibilis a 2-es (2.7.18-as) változattal

Ebből néhányról pár szó most, a többi majd bővebben ki lesz fejtve később.

### Magas szintű nyelv
Nem hardverhez közeli utasítások az alapvető építőkövek (pl.: regiszterben lévő érték növelése adott memóriacímen található értékkel), hanem magasabb szintűek (változó értékének növelése másik változóval), valamint adottak magas szintű vezérlési szekezetek, összetett adattípusok, stb.

### Általános célú
A nyelv [Turing teljes](https://en.wikipedia.org/wiki/Turing_completeness), azaz tetszőleges algoritmus megvalósítható benne.

### Interpretált
Bár létezik JIT fordító, valamint a nyelv egyes részhalmazaihoz C/C++ fordító, a referencia implementáció ([CPython](https://github.com/python/cpython)) egy interpreter.


# Korábbi utasítások, vezérlési szerkezetek Python megfelelője

| Pszeudo kód          | Python               |
|----------------------|----------------------|
| Amíg (feltétel)      | `while expression:`  |
| Ha (feltétel)        | `if expression:`     |
| Különben             | `else:`              |
| Be: változó          | `variable = input()` |
| Ki: változó          | `print(variable)`    |
| Ki: szöveg           | `print("some text")` |
| változó = kifejezés  | `variable=expression`|
| Vége                 | `exit()`             |

# Minta kód
## Első példa
Az egyik egyszerű algoritmus múlt hétről addig kért be számokat, amíg 0-t nem adtunk meg:

```
Be: szám
Amíg (szám≠0)
──┐ Be: szám
```

A fentieknek megfelelően így nézne ki ennek a Python megfelelője:

```python
num=input()
while num!=0:
    num=input()
```

Ha ezt a kódot elmentjük egy `ask_numbers_until_zero.py` fájlba, akkor egy `python ask_numbers_until_zero.py` paranccsal tudjuk futtatni.

Futtatást követőenzt fogjuk tapasztalni, hogy van, akinek helyesen működik, másnak nem. Utóbbi esetben hiába adunk meg 0-t, továbbra is kér tőlünk bemenetet a program.

Itt jön ki a különbség a Python 2-es és 3-as változata között: az `input()` az előbbi esetben számot ad vissza, utóbbiban *szöveget*. Különböző típusokról pár hét múlva lesz szó, egyenlőre jegyezzük meg, hogyha számot szeretnénk bekérni, akkor azt `num=int(input())` módon tehetjük meg. Így a helyes kód:

```python
num=int(input())
while num!=0:
    num=int(input())
```

## Összetettebb példa

A Kollatz sejtéshez kapcsolódó sorozat pszeudo kódja így nézett ki:

```
Be: szám
Amíg (szám≠1)
──┐ Ki: szám
  │ Ha (szám páros)
  ├──┐ szám=szám/2
  │ 
  │ Különben
  ├──┐ szám=3⋅szám+1
Ki: szám
```
Aminek a python megvalósítása:

```python
num=int(input())
while num!=1:
    print(num)
    if num%2==0:
        num//=2
    else:
        num=3*num+1
print(num)
```
# Néhány megjegyzés

## További Python 2 és 3 közötti eltérések
Az `input()` típusán kívül még a sima osztás (`/`) is másképp működik egész számok esetén 2-es és 3-as Python esetében. 
Python 3-ban a sima `/` minden esetben *lebegőpontos* számot ad vissza, azaz `4/2` eredménye nem `2` lesz mint Python 2-nél, hanem `2.0`. 
Ezért ha a fenti kódban `num/=2`-t írtunk volna, akkor az 3-as Python esetében furán működne.

Jegyezzük meg, hogyha egész osztást szeretnénk végezni 3-as Pythonban, akkor a `//` operátort kell használnunk. 
Ez az operátor természetesen "levágja" a törtrészt, tegát `5//3` az `1` lesz.

## Bekérés szöveggel
Az `input()`-nak a zárójel között adhatunk meg egy tetszőleges szöveget, amit kiír bemenet kérése esetén, pl: `num=input("Please give me a number: ")`

## " és ' szövegeknél
Egy szöveget (pontosabban string literált) tetszőlegesen lehet macskakörmök és aposztrófok közé tenni. A kettő között semmilyen szemantikai különbség nincs, de törekedjünk a konzisztenciára. 
Ha magában a szövegben volna valamelyik, akkor érdemes a másikat használni és akkor nincs szükség escape-elésre.

Az alábbi két sor ugyanazt írja ki:
```python
print("\"Run you fools!\" - Gandalf")
print('"Run you fools!" - Gandalf')
```

"""

## 1. Hazassagi nevek - 4 pont
 - **a)** Keszits programot, mely beolvassa valaki nevet, es kiirja kulon a vezeteknevet es a keresztnevet, pl.:
```
Kerem a nevet: Bolyai Farkas
Vezeteknev: Bolyai
Keresztnev: Farkas
```
 - **b)** Modositsd a programot ugy, hogy beolvassa a ferj nevet es a feleseg leanykori nevet, es kiirja a feleseg lehetseges hazassagi neveit. Pl.:
```
Kerem a ferj nevet: Bolyai Farkas
Kerem a feleseg leanykori nevet: Benko Zsuzsanna
A lehetséges házassági nevek:
 - Benko Zsuzsanna
 - Bolyai Farkasne
 - Bolyai Farkasne Benko Zsuzsanna
 - Bolyaine Benko Zsuzsanna
 - Bolyai Zsuzsanna
 - Bolyai-Benko Zsuzsanna
 - Benko-Bolyai Zsuzsanna
 ```

"""

husband = input("Ferj neve ").split()
wife = input("Feleseg neve: ").split()

print("Ferj vezetekneve:", husband[0])
print("Ferj keresztneve:", husband[1])
print("Feleseg vezetekneve:", wife[0])
print("Feleseg keresztneve:", wife[1])


print("Lehetseges hazassagi nevek felesegnek:")
print(f" - {wife[0]} {wife[1]}")
print(f" - {husband[0]} {husband[1]}ne")
print(f" - {husband[0]} {husband[1]}ne {wife[0]} {wife[1]}")
print(f" - {husband[0]}ne {wife[0]} {wife[1]}")
print(f" - {husband[0]} {wife[1]}")
print(f" - {husband[0]}-{wife[0]} {wife[1]}")
print(f" - {wife[0]}-{husband[0]} {wife[1]}")


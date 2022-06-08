csapat_szam = int(input("Hány csapat van a bajnokságban? "))
if csapat_szam == 1:
    print("Nem lesznek meccsek.")
else:
    meccs_szam = csapat_szam * (csapat_szam - 1) // 2
    print(meccs_szam, "meccs lesz.")
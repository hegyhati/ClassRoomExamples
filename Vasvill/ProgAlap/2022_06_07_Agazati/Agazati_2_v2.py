szamok = [ szam.strip() for szam in input("Kérem a számokat vesszővel elválasztva: ").split(',')]
egyedul = [ szam for szam in szamok if szamok.count(szam)==1 ]
print(f"{len(egyedul)} db:", ", ".join(egyedul))

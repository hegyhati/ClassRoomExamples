kabinszam = int(input("Add meg, hany kabin van: "))
kabinok = [0]*kabinszam
index=0
while index < len(kabinok):
	kabinok[index]=int(input("Hanyan vannak a(z) "+str(index+1)+". kabinban? "))
	index+=1

print(kabinok)

minidx=0
index=1

while index < len(kabinok):
	if kabinok[index] < kabinok[minidx]:
		minidx=index
	index+=1

print( "A(z) " + str(minidx+1) + ". kabinba menjunk be, mert ott csak " + str(kabinok[minidx]) + " utas van.")

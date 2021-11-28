import  json

input_file=open("kihogyall.json","rt")
content=input_file.read()
input_file.close()
data=json.loads(content)

print(data)


while True:
    print("kilep: Kilepes a programbol es mentes.")
    print("megoldas: valaki uj megoldast adott le.")
    valasz=input("Mit szeretnel? ")
    if valasz=="kilep":
        jsondata=json.dumps(data)
        output=open("kihogyall.json","wt")
        output.write(jsondata)
        output.close()
        exit()
    elif valasz=="megoldas":
        ki=input("Ki adott le uj megoldast?")
        if ki in data:
            data[ki]+=1
    else:   
        print("Rossz parancs.")

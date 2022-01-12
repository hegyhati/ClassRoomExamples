def koszones(szerep="diak", nyelv="HU"):
    if szerep=="tanar":
        if nyelv=="EN":
            return "Good day!"
        elif nyelv=="HU":
            return "Jo napot kivanok!"
    elif szerep=="diak":
        if nyelv=="EN":
            return "Hi!"
        elif nyelv=="HU":
            return "Szia!"


print( koszones("tanar") )
print( koszones("diak","EN") )
print( koszones() )
print( koszones(nyelv="EN") )
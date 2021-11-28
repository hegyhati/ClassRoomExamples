def havikoltseg(hasznalat,dijszabas):
    return hasznalat["perc"]*dijszabas["percdij"]+hasznalat["sms"]*dijszabas["smsdij"]

def havibeker():
    perc=int(input())
    sms=int(input())
    return {"sms":sms,"perc":perc}

def egeszevetbeker():
    honapok=[]
    for i in range(12):
        honapok.append(havibeker())
    return honapok


honapok=egeszevetbeker()
print(honapok)
for i in range(12):
    print("Honap ",i,havikoltseg(honapok[i],telekom_m_saver))

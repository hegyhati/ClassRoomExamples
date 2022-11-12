// Valosagban jon valahonnet

data = {
    "ZTE KK" : {
        "short name" : "ZTE KK",
        "full name" : "Zalaegerszegi Kosarlabda Klub",
        "hometown" : "Zalaegerszeg",
        "players" : {
            "Kiss Jozsef" :{},
            "Szabo Laszlo":{},
            "Nemeth Valentin":{},
            "Makkos David" :{ 
                "position" : "center",
                "number" : 15,
                "points" : {
                    "2021": 23,
                    "2020" : 43,
                    "2019" : 123
                },
                "birthdate": "1992.02.45.",
                "height": 134.5
            },
            "Kiss Barnabas":{},
            "James Kinney":{}
        }
    },
    "Soproni Tigrisek" : {
        "full name" : "Soproni Tigrisek Barati Kosarlabda Pajtasok",
        "hometown" : "Sopron"
    },
    "Soproni Sportiskola" : {},
    "Soproni Darazsak" : {},
    "Budapesti Honved" :{},
    "Falco" : {}
}

szoveg = "Melyik csapat erdekel?"

for (csapat in data)
    szoveg = szoveg + "\n - " + csapat

csapat = prompt(szoveg)

csapatinfo = 
    data[csapat]["full name"] + "\n" + 
    "Szekhely: " + data[csapat]["hometown"] + "\n"
    "Jatekosok: \n"; 

for (jatekos in data[csapat]["players"])
    csapatinfo += " - " + jatekos + "\n"

alert(csapatinfo)



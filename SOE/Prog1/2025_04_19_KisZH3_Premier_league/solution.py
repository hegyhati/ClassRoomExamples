import os, os.path

basepath = "Premier_league"

nationality = input()

for club in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath,club)):
        for player in os.listdir(os.path.join(basepath, club)):
            [num, name, nat] = os.path.splitext(player)[0].split("_")
            if nat == nationality:
                print(f"{name} - {club} ({num})")
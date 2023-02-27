import json
import os

SAVESDIR = "saves"
SAVEFILETYPE = ".json"

def list_saves():
    saves = os.listdir(SAVESDIR)

    for save in saves:
        [filename, extension] = os.path.splitext(save) 
        if extension == SAVEFILETYPE:
            print(f" - {filename}")


def load_character():
    print("Szia, valassz mentest:")
    list_saves()
    savefile = os.path.join(SAVESDIR, input() + SAVEFILETYPE)

    if not os.path.exists(savefile):
        print("Nem jot adtal meg.")
        exit()

    with open(savefile) as file:
        character = json.load(file)
    
    return character


character = load_character()
print(character['name'])
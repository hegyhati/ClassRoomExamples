import json


def get_filename():
    return input("Filename: ")

def load_data(filename):
    with open(filename) as f:
        return json.load(f)

filename=get_filename()
try:
    data=load_data(filename)
except FileExistsError:
    print("File does not exists.")
    exit()
except json.decoder.JSONDecodeError:
    print("File is not a valid JSON file.")
    exit()
except Exception as e:
    print("I have no idea, but something is wrong.")
    raise e

print(data["names"])

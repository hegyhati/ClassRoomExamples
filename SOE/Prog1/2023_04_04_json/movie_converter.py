import json


def parse_entry(line):
    data = line.split(",")
    return {
        "person" : data[0].strip(), 
        "movie": data[1].strip(), 
        "character": data[2].strip(),
        "watched_in_theatre": False if int(data[3]) == 0 else True
    }

def display_entry(entry):
    print(f"{entry['person']} kedvenc filmje: {entry['movie']}. A kedvenc karaktere a filmben: {entry['character']}.")

f = open("kedvenc_filmek.csv")
data = []
for line in f:
    entry = parse_entry(line)
    display_entry(entry)
    data.append(entry)
f.close()
print(data)
with open("kedvenc_filmek.json", "w") as f:
    json.dump(data,f,indent=2)
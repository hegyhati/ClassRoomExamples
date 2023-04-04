import json

DATABASE_FILE = "kedvenc_filmek.json"

def load_movies():
    with open(DATABASE_FILE) as f:
        data = json.load(f)
        return data
    
def persist_movies(movies):    
    with open(DATABASE_FILE, "w") as f:
        json.dump(movies,f,indent=2)

def read_new_entry():
    return {
        "person" : input("Name of person: "),
        "movie" : input("Title of favorite movie: "),
        "character" : input("Name of favorite character in the movie: "),
        "watched_in_theatre" : True if "yes" in input("Watched in theatre? ") else False 
    }

def fetch_entry(movies, person):
    for entry in movies:
        if entry['person'] == person:
            return entry
    return None

movies = load_movies()
entry = read_new_entry()
old_entry = fetch_entry(movies, entry["person"])
if old_entry:
    print(f"{entry['person']} already has a favorite movie: {old_entry['movie']}.")
    overwrite = input("Do you want to replace it (yes/no)? ")
    if "yes" in overwrite:
        # todo: meglevot kiszedni
        movies.append(entry)
else:
    movies.append(entry)
persist_movies(movies)



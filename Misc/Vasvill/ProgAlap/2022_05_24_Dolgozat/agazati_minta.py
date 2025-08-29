import json

def load_characters_from_file_1(filename):
    with open(filename) as f:
        movies = json.load(f)
    all_characters = []
    for movie in movies:
        for character in movie['characters']:
            if character not in all_characters:
                all_characters.append(character)
    return all_characters

def load_characters_from_file_2(filename):
    with open(filename) as f:
        movies = json.load(f)
    all_characters = []
    for movie in movies:
        all_characters +=  movie['characters']
    return list(set(all_characters))

def movie_count(character, filename):
    with open(filename) as f:
        movies = json.load(f)
    count = 0
    for movie in movies:
        if character in movie['characters']:
            count += 1
    return count



filename = "hp.json"
characters = load_characters_from_file_2(filename)
for character in characters:
    print(f"{character} összesen {movie_count(character, filename)} filmben szerepel.")




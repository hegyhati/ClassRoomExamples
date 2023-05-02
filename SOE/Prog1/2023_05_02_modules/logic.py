from json import load, dump

_DATABASE_FILE = "hu_en.json"

def _read_words_from_file():
    with open(_DATABASE_FILE) as f:
        return load(f)

def _persist_words_to_file(words):
    with open(_DATABASE_FILE, "w") as f:
        dump(words,f,indent=2)

def update_with_word(hu, en):
    words = _read_words_from_file()
    words[hu] = en
    _persist_words_to_file(words)

def has_word(hu):
    words = _read_words_from_file()
    return hu in words

def translate(hu):
    words = _read_words_from_file()
    return words[hu]

def delete_word(hu):
    words = _read_words_from_file()
    del words[hu]
    _persist_words_to_file(words)

def _test():
    print("OK" if not has_word("qwe") else "ERROR") 
    update_with_word("qwe","asd")
    print("OK" if has_word("qwe") else "ERROR") 
    print("OK" if translate("qwe") == "asd" else "ERROR")
    delete_word("qwe")
    print("OK" if not has_word("qwe") else "ERROR") 

if __name__ == "__main__":
    _test()
import json

def load_language(lang:str) -> dict:
    with open("hangman_ui_literals.json") as f:
        return json.load(f)[lang]

def available_languages() -> list[str]:    
    with open("hangman_ui_literals.json") as f:
        return json.load(f).keys()
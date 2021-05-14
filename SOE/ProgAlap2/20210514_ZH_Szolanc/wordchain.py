import json
import random


class WordChain:
    _source = "wordlist.json"

    def __init__(self, match_length: int = 1):
        with open(self._source) as words:
            wordlist = json.load(words)
            initial_word = random.choice(wordlist)
            self.wordlist = set(wordlist)
        self.chain = [initial_word]
        self.match_length = match_length

    def length(self):
        return len(self.chain)

    def append(self, word: str):
        if word not in self.wordlist:
            raise Exception("Incorrect word.")
        if word in self.chain:
            raise Exception("Word already used.")
        if self.chain[-1][-self.match_length:] != word[:self.match_length]:
            raise Exception("Cannot chain word to previous one")
        self.chain.append(word)



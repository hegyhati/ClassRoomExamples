import os
from os.path import join, splitext
import matplotlib.pyplot as plt

class ArticleSearch:
    def __init__(self, basedir) -> None:
        self.basedir = basedir

    def __count(self, site_path:str, term:str) -> int:
        count = 0
        for article in os.listdir(site_path):
            if splitext(article)[1] == ".txt":
                with open(join(site_path,article)) as f:
                    for line in f:
                        count += [word.strip().lower() for word in line.split()].count(term.lower())
        return count

    def search(self, term:str) -> None:
        data = {
            site : self.__count(join(self.basedir,site),term)
            for site in os.listdir(self.basedir)
        }
        f,a = plt.subplots()
        a.bar(data.keys(),data.values())
        a.set_title(f"Talalatok \"{term}\"-re")
        f.savefig(f"{term}_py.png")

    def __average_word_length(self, article_path, min_length):
        with open(article_path) as f:
            lengths = [ len(word)
                for line in f
                for word in line.split()
                if len(word) >= min_length
            ]
        return sum(lengths) / len(lengths)

    def website_average_word_statistics(self, sites: list, min_length: int = 5):
        data = {
            site : [ self.__average_word_length(join(self.basedir,site,article), min_length)
                for article in sorted(os.listdir(join(self.basedir,site)))
                if splitext(article)[1] == ".txt"
            ]
            for site in sites
        }
        f,a = plt.subplots()
        for site in data:
            a.plot(data[site], label=site)
        a.set_title(", ".join(sites) + " szohossz atlagok")
        a.legend()
        f.savefig("_".join(sites)+"_py.png")

search = ArticleSearch('articles')
search.search('egY')
search.website_average_word_statistics(['hvg', 'index', 'origo'], 4)
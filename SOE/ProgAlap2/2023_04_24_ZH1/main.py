import json
import matplotlib.pyplot as plt
import os
from os.path import join


class Grade_Statistics:
    def __init__(self, path:str) -> None:
        self.path = path

    def __filename(self, subject:str, year: str):
        return join(self.path, year,f"{subject}.json")
    
    def result_plot(self, subject: str, year: int) -> None:
        try:
            with open(self.__filename(subject,str(year))) as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
            return
        list_of_grades = list(data.values())
        f,a = plt.subplots()
        grades = [1,2,3,4,5]
        a.bar(grades,[list_of_grades.count(grade) for grade in grades])
        a.set_title(f"{subject} results in {year}")
        f.savefig(f"{subject}_{year}_results_py.png")

    def percentage(self, subject: str, year: str) -> float:
        try:
            with open(self.__filename(subject,str(year))) as f:
                data = json.load(f)
        except FileNotFoundError:
            return 0
        return 1 - list(data.values()).count(1) / len(data)


    def result_plot_over_years(self, subjects: list):
        years = os.listdir(self.path)
        years.sort()
        f,a = plt.subplots()
        for subject in subjects:
            percentages = [self.percentage(subject,year) for year in years]
            a.plot(years,percentages)
        a.set_title("Pass statistics for " + " ".join(subjects))
        a.legend(subjects)
        f.savefig("_".join(subjects)+"_results_py.png")


stats = Grade_Statistics('./results')
stats.result_plot('math', 2020)
stats.result_plot_over_years(['math', 'music'])
#!/usr/bin/env python3

import json
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def get_contribution_stats(git_history:list[dict]) -> dict[str,int]:
    commit_count = {}
    for commit in git_history:
        email = commit["email"]
        if email in commit_count: commit_count[email] += 1
        else: commit_count[email] = 1
    return commit_count

def get_top_10_contributors(git_history:list[dict]) -> list[dict]:
    commit_count = get_contribution_stats(git_history)
    commit_count_list = [
        {"email": email, "commits": commit_count[email]} 
        for email in commit_count
    ]
    commit_count_list.sort(key=lambda x: x["commits"], reverse=True)
    return commit_count_list[:10]        

def top_contributor_plot(filename:str, git_history:list[dict]) -> None:
    tops = get_top_10_contributors(git_history)
    fig, ax = plt.subplots()
    ax.barh([top["email"] for top in tops], [top["commits"] for top in tops])
    ax.set_xlabel("Commits")
    fig.tight_layout()
    fig.savefig(filename)
    
def get_year(commit:dict) -> int:
    return int(commit["date"][:4])

def growth_plot(filename:str, git_history:list[dict]) -> None:
    changes_by_year = {
        year : 0
        for year in range(get_year(git_history[-1]), 2025)
    }
    for commit in git_history:
        changes_by_year[int(commit["date"][:4])] += commit["changes"]
    fig, ax = plt.subplots()
    ax.plot(changes_by_year.keys(), changes_by_year.values())
    ax.set_xlabel("Year")
    ax.set_ylabel("File changes")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.tight_layout()
    fig.savefig(filename)            

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as f:
        data = json.load(f)

    try:
        top_contributor_plot(file + "_top10_contributors.png", data)
    except KeyError:
        print("No email in the data, toplist plot will not be generated")
        
    try:
        growth_plot(file + "_annual_file_changes.png", data)
    except KeyError:
        print("No changes or date in the data, growth plot will not be generated")

from typing import List
import json

def load_data() -> List[dict]:
    with open("data.json") as f:
        data = json.load(f)
    return data

def save_data(data : List[dict]) -> None:
    with open("data.json","w") as f:
        json.dump(data,f)

def save_new_run(date:str, runners: List[int]) -> None:
    data = load_data()
    data.append(
        {
            "date" : date,
            "runners" : runners
        }
    )
    save_data(data)

def list_of_runners(data:List[dict]) -> List[str]:
    runners = set()
    for run in data:
        runners = runners.union(run["runners"])
    runners = list(runners)
    runners.sort()
    return runners

def count_runs(data:List[dict],runner:str) -> int:
    count = 0
    for run in data:
        if runner in run["runners"]:
            count += 1
    return count

def svg_export_runners(data:List[dict]) -> None:
    runners = list_of_runners(data)
    with open("export.svg","w") as f:   
        f.write(f'<svg width="100" height="{20*len(runners)}">\n')
        for idx,runner in enumerate(runners):
            f.write(f'<rect x="10" y="{idx*20+5}"  width="{count_runs(data,runner)*10}" height="10" style="fill:rgb(0,0,255);stroke-width:2;stroke:rgb(0,0,0)" />\n')
            f.write(f'<text x="{count_runs(data,runner)*10+15}" y="{idx*20+15}" >{runner}</text>\n')
        f.write('</svg>')



 

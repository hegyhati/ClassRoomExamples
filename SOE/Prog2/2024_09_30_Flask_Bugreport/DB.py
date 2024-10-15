import json
from datetime import datetime
DATABASE_FILE = "database.json"
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"

def __load_data() -> list[dict]:
    with open(DATABASE_FILE) as f:
        return json.load(f)

def __persist_data(bugs:list[dict]) -> None:
    with open(DATABASE_FILE, "w") as f:
        json.dump(bugs,f,indent=1)
    

def load_bug_list(keys=["id","title"]) -> list[dict]:
    return __load_data()

def add_bug(bug:dict) -> int:
    bugs = __load_data()
    id = len(bugs)
    bug["id"] = id
    bug["open"] = True
    bug["comments"] = []
    bug["creation_date"] = datetime.now().strftime(TIMEFORMAT)
    bugs.append(bug)
    __persist_data(bugs)
    return id

def fetch_bug(id:int) -> dict | None:
    for bug in __load_data():
        if bug["id"] == id:
            return bug

def add_comment(bugid:int, text:str) -> None:
    bugs = __load_data()
    for bug in bugs:
        if bug["id"] == bugid:
            bug["comments"].append({
                "date" : datetime.now().strftime(TIMEFORMAT),
                "text" : text
            })
            break
    __persist_data(bugs)
    
def mark_solution(bugid:int, commentidx:int) -> None:
    bugs = __load_data()
    for bug in bugs:
        if bug["id"] == bugid:
            if 0 <= commentidx < len(bug["comments"]):
                bug["open"] = False
                bug["solution_idx"] = commentidx
            break
    __persist_data(bugs)
    
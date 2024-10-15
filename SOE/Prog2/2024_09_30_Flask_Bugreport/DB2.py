import sqlite3
from datetime import datetime
DATABASE_FILE = "database.sqlite"
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


__connection = None
def connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect(DATABASE_FILE)
        __connection.row_factory = sqlite3.Row
    return __connection
    
    

def load_bug_list() -> list[dict]:
    bug_list = connection().execute("SELECT * FROM bugs").fetchall()
    return [
        {
            **{key : bug[key] for key in ["title", "description", "id", "creation_date"]},
            "open" : bug["solution"] is None,
            "comments" : connection().execute("SELECT * FROM comments WHERE bug = ?", (bug["id"],)).fetchall()
        }
        for bug in bug_list
    ]

def add_bug(bug:dict) -> int:
    bug["creation_date"] = datetime.now().strftime(TIMEFORMAT)
    cur = connection().cursor()
    cur.execute("""
    INSERT INTO bugs (title, description, creation_date)
    VALUES (:title, :description, :creation_date)
    """, bug)
    connection().commit()
    return cur.lastrowid

def fetch_bug(id:int) -> dict | None:
    bug = connection().execute("SELECT * FROM bugs WHERE id = ?", (id,)).fetchone()
    return {
        **{key : bug[key] for key in ["title", "description", "id", "creation_date"]},
        "open" : bug["solution"] is None,
        "solution_idx" : -1, # coupling issue
        "comments" : connection().execute("SELECT * FROM comments WHERE bug = ?", (bug["id"],)).fetchall()
    }

def add_comment(bugid:int, text:str) -> None:
    pass
    
def mark_solution(bugid:int, commentidx:int) -> None:
    pass
    
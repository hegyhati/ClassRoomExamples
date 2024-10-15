import datetime
import sqlite3

from typing import Optional

_conn = sqlite3.connect("database.sqlite")
_conn.row_factory = sqlite3.Row

class Bug:
    
    def __str__(self) -> str:
        return f"Title: {self.title}\n  Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n  Description: {self.description}"
    
    @staticmethod
    def create_new_bug(title:str, description: str) -> None:
        _conn.execute("INSERT INTO bugs (title, description, creation_date) VALUES (?, ?, ?)", (title, description, datetime.datetime.now().isoformat()))
        _conn.commit()
    
    @staticmethod
    def __build_from_res(res: sqlite3.Row) -> Optional["Bug"]:
        if res is None: return None
        b = Bug()
        for key in res.keys():
            setattr(b, key, res[key])
        b.creation_date = datetime.datetime.fromisoformat(b.creation_date)
        return b
    
    @staticmethod
    def get_all_bugs() -> list["Bug"]:
        return [
            Bug.__build_from_res(res)
            for res in _conn.execute("SELECT * FROM bugs").fetchall()
        ]
    
    @staticmethod
    def get_bug_by_id(id:int) -> Optional["Bug"]:
        return Bug.__build_from_res(_conn.execute("SELECT * FROM bugs WHERE id = ?;", (id,)).fetchone())
    
    # 2 days or older
    def is_too_old(self):
        return datetime.datetime.now() > self.creation_date + datetime.timedelta(days=2)
        

if __name__ == "__main__":
    if input("Do you want to create a new bug? (y/n): ") == "y":
        title = input("Title: ")
        description = input("Description: ")
        Bug.create_new_bug(title, description)
    for bug in Bug.get_all_bugs():
        if bug.is_too_old():
            print("OLD!!!!", end=" ")
        print(bug)
            
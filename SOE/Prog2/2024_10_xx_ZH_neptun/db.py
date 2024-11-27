import datetime
import sqlite3
from typing import Optional
import requests


DATABASE = "gain.db"

class Student:
    
    def __init__(self, neptun: str, name: str):
        self.neptun = neptun
        self.name = name
    
    def first_name(self) -> str:
        return self.name.split(" ")[-1]
    
    def has_nameday(self) -> bool:
        res = requests.get(f"https://api.nevnapok.eu/ma")
        if res.status_code != 200: return False
        for day, namelist in res.json().items():
            if self.first_name() in namelist: return True
        return False
    
    def get_courses(self) -> dict[str,int|None]:
        with sqlite3.connect(DATABASE) as conn:
            return {
                data[0]: data[1]
                for data in conn.execute("""
                    WITH studentgrades AS (
                        SELECT course_id, grade FROM grades WHERE student_id = ?
                    )
                    SELECT courses.name, studentgrades.grade
                    FROM studentgrades
                    FULL JOIN courses ON studentgrades.course_id = courses.neptun
                """, (self.neptun,)).fetchall()
            }
        
        
    @staticmethod
    def get_by_neptun(neptun: str) -> Optional["Student"]:
        with sqlite3.connect(DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            data = conn.execute("SELECT neptun, name FROM students WHERE neptun = ?", (neptun,)).fetchone()
            if data: return Student(**data)

    @staticmethod
    def get_all() -> list["Student"]:
        with sqlite3.connect(DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            return [
                Student(**data)
                for data in conn.execute("SELECT neptun, name FROM students").fetchall()
            ]


def get_course_list() -> dict[str, str]:
    with sqlite3.connect(DATABASE) as conn:
        return {
            data[0]: data[1]
            for data in conn.execute("SELECT neptun, name FROM courses").fetchall()
        }

def register_grade(student_id: str, course_id: str, grade: int) -> None:
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO grades (student_id, course_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, course_id, grade, datetime.datetime.now().isoformat()))
        conn.commit()

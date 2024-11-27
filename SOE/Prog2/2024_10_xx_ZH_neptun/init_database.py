import sqlite3

conn = sqlite3.connect('gain.db')


conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    neptun TEXT PRIMARY KEY,
    name TEXT NOT NULL
);""")

conn.executemany("INSERT INTO students (neptun, name) VALUES (?, ?)", [
    ("ABC123", "Kiss Elemer"),
    ("BLELLE", "Balaton Lelle"),
    ("FFINGE", "Feher Inge"),
    ("FOOBAR", "Foonay Barnabas")
])

conn.execute("""
CREATE TABLE IF NOT EXISTS courses (
    neptun TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    semester INTEGER NOT NULL,
    credits INTEGER NOT NULL    
);""")

subjects = [
    ("FB0013", "Bevezeto matematika", 1, 5),
    ("FB0091", "Informatikai Alapismeretek", 1, 5),
    ("FB0137", "Programozasi Alapok", 1, 5),
    ("FB0132", "Operacios rendszerek es szamitogep architekturak", 1, 5),
    ("FB0196", "Vallalat- es vallalkozasgazdasagtani ismeretek", 1, 4),
    ("FB0062", "Hackathon 0", 1, 1),
    ("SOE001", "Testneveles 1", 1, 0),
    ("FB0006", "Analizis es linearis algebra", 2, 5),
    ("FB0169", "Szamitastudomany alapjai", 2, 5),
    ("FB0135", "Programozas 1", 2, 5),
    ("FB0150", "Szamitogep halozatok", 2, 5),
    ("FB0200", "Vezetes es szervezes", 2, 4),
    ("FB0063", "Hackathon 1", 2, 1),
    ("SOE002", "Testneveles 2", 2, 0)
]

conn.executemany("INSERT INTO courses (neptun, name, semester, credits) VALUES (?, ?, ?, ?)", subjects)
conn.commit()

conn.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    course_id TEXT NOT NULL,
    grade INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(neptun)
);""")
    
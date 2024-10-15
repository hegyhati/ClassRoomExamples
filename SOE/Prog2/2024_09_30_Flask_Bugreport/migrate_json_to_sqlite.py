import json
import sqlite3
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument("jsonfile")
argparser.add_argument("sqlitefile")
args = argparser.parse_args()

conn = sqlite3.connect(args.sqlitefile)

# Create tables
conn.execute("""
CREATE TABLE bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    solution INTEGER,
    creation_date TEXT NOT NULL,
    FOREIGN KEY (solution) REFERENCES comments(id)
)
""")

conn.execute("""
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    text TEXT NOT NULL,
    bug INTEGER NOT NULL,
    FOREIGN KEY (bug) REFERENCES bugs(id)
)
""")

# migrate bugs

with open(args.jsonfile) as f:
    data = json.load(f)

for bug in data:
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO bugs (title, description, creation_date)
    VALUES (:title, :description, :creation_date)
    """, bug)
    conn.commit()
    bugid = cur.lastrowid
    for idx,comment in enumerate(bug["comments"]):
        comment["bug"] = bugid
        cur.execute("""
        INSERT INTO comments (date, text, bug)
        VALUES (:date, :text, :bug)
        """, comment)
        if "solution_idx" in bug and idx == bug["solution_idx"]:
            cur.execute("""
            UPDATE bugs
            SET solution = ?
            WHERE id = ?
            """, (cur.lastrowid, bugid))
        conn.commit()
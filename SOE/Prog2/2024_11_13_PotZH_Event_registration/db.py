import sqlite3
import requests
from datetime import date

__conn = sqlite3.connect("potzh.sqlite", check_same_thread=False)
__conn.row_factory = sqlite3.Row



def __create_tables():
    __conn.execute("""CREATE TABLE events (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   organizer_name TEXT,
                   organizer_email TEXT,
                   location TEXT,
                   date TEXT,
                   registration_limit INTEGER
                   )""")
    __conn.execute("""CREATE TABLE registrations (
                   attendee_name TEXT,
                   attendee_email TEXT,
                   event_id INTEGER,
                   FOREIGN KEY (event_id) REFERENCES events (id)
                    )""")
    __conn.commit()

def __validate_email(email:str) -> bool:
    return requests.get(f"https://api.usercheck.com/email/{email}").status_code == 200

def check_and_convert_event_data(event_data:dict) -> None:
    if event_data["name"] == "": raise ValueError("Event name cannot be empty.")
    if event_data["organizer_name"] == "": raise ValueError("Organizer name cannot be empty.")
    if event_data["organizer_email"] == "": raise ValueError("Organizer e-mail cannot be empty.")
    if event_data["location"] == "": raise ValueError("Event location cannot be empty.")
    if event_data["date"] == "": raise ValueError("Event date cannot be empty.")
    if event_data["registration_limit"] == "": raise ValueError("Registration limit cannot be empty.")
    if not __validate_email(event_data["organizer_email"]): raise ValueError("Invalid organizer e-mail.")
    try: 
        date.fromisoformat(event_data["date"])
    except ValueError:
        raise ValueError("Event date format incorrect, should be YYYY-MM-DD.")
    if date.fromisoformat(event_data["date"]) < date.today(): raise ValueError("Cannot advertise past events.")
    try:
        event_data["registration_limit"] = int(event_data["registration_limit"])
    except ValueError:
        raise ValueError("Registration limit must be integer.")
    if event_data["registration_limit"] <= 0: raise ValueError("Registration limit must be positive.")


def add_event(event_data:dict) -> int:
    check_and_convert_event_data(event_data)
    c = __conn.cursor()
    c.execute(f"""INSERT INTO events ({','.join(event_data.keys())})
                       VALUES ({','.join([f':{key}' for key in event_data.keys()])});
                   """, event_data)
    __conn.commit()
    return c.lastrowid


def format_event(event_data:sqlite3.Row) -> dict:
    event_data = dict(event_data)
    event_data["registration_count"] = __conn.execute("SELECT COUNT(*) FROM registrations WHERE event_id = :id;", {"id":event_data["id"]}).fetchone()[0]
    event_data["upcoming"] = date.fromisoformat(event_data["date"]) >= date.today()
    return event_data

def get_all_events() -> list[dict]:
    return [format_event(result) for result in __conn.execute(f"""SELECT * FROM events;""").fetchall()]

def get_event(id:int) -> dict:
    return format_event(__conn.execute("""SELECT * from events WHERE id = :id;""", {"id":id}).fetchone())

def register_person_for_event(event_id:int, attendee:dict):
    for a in get_attendees(event_id):
        if a["attendee_name"] == attendee["attendee_name"] and a["attendee_email"]==attendee["attendee_email"]: 
            raise ValueError(f"{attendee['attendee_name']} already registered.")
    event = get_event(event_id)
    if event["registration_count"] == event["registration_limit"]: raise ValueError("Ecent limit reached.")
    if not event["upcoming"]: raise ValueError("Event already happened.")
    __conn.execute("""INSERT INTO registrations (event_id, attendee_name, attendee_email) VALUES (?,?,?)""", (event_id, attendee["attendee_name"], attendee["attendee_email"]))
    __conn.commit()

def get_attendees(event_id:int) -> list[dict]:
    return [dict(registration) for registration in __conn.execute("SELECT * FROM registrations WHERE event_id = ?;", (event_id,)).fetchall()]

if __name__ == "__main__":
    __create_tables()
    add_event({
        "name" : "Prog2 POTZH",
        "organizer_name" : "Mate Hegyhati",
        "organizer_email" : "hegyhati.mate@uni-sopron.hu",
        "location" : "A030",
        "date" : "2024-11-13",
        "registration_limit" : "15"
    })

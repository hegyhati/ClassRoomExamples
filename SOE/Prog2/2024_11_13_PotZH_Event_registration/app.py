from flask import Flask, render_template, request, redirect, url_for
from datetime import date
import db

app = Flask(__name__)




@app.get("/")
def event_list():
    return render_template("event_list.html", 
            past_events= filter(lambda x: not x["upcoming"], db.get_all_events()),
            future_events= filter(lambda x: x["upcoming"], db.get_all_events())
    )

@app.get("/event/<int:id>")
def event_details(id:int):
    return render_template("event_details.html", event = db.get_event(id), registrations=db.get_attendees(id))


@app.post("/event/<int:event_id>/register")
def register(event_id:int):
    try: 
        db.register_person_for_event(event_id, dict(request.form))
        return redirect(url_for("event_details", id=event_id))
    except ValueError as e:
        return render_template("error.html", message=str(e))

@app.get("/new")
def new_event_form():
    return render_template("new_event.html")

@app.post("/new")
def new_event():
    try:
        data = dict(request.form)
        id = db.add_event(data)
        return redirect(url_for("event_details", id=id))

    except ValueError as e:
        return render_template("error.html", message=str(e))
from flask import Flask, render_template, request, redirect, url_for

# import DB  # previous json based implementation
import DB2 as DB # new sqlite based implementation

# UI and logic is more coupled than should be, thus DB module replacement is not as easy as it should be

app = Flask(__name__)


MAINPAGE_TEMPLATE = "mainpage.html"
BUG_TEMPLATE = "bug.html"


@app.get("/")
def main_page():
    return render_template(MAINPAGE_TEMPLATE, bugs=DB.load_bug_list())

@app.post("/bug")
def new_bug():    
    id = DB.add_bug(request.form.to_dict())
    return redirect(url_for("bug_detail", id=id))
    
@app.get("/bug/<int:id>")
def bug_detail(id:int):
    print(type(id))
    bug = DB.fetch_bug(id)
    if bug is None:
        return render_template('notfound.html')
    else:
        return render_template(BUG_TEMPLATE,bug=bug)
    
@app.post("/bug/<int:bugid>/comment")
def new_comment(bugid:int):
    text = request.form.to_dict()["text"].strip()
    if text != "": DB.add_comment(bugid,text)
    return redirect(url_for("bug_detail", id=bugid))
    
@app.post("/solution")
def mark_solution():
    bugid = int(request.form["bugid"])
    commentidx = int(request.form["commentidx"])
    DB.mark_solution(bugid, commentidx)
    return redirect(url_for("bug_detail", id=bugid))
    
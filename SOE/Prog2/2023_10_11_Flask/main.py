from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route("/error")
def error():
    return render_template("error.html")

def fetch_all_runners() -> list[str]:
    runners = set()
    with open("sortabla.yaml") as f:
        for line in f:
            runners.update(parse_entry(line)[1])
    return sorted(list(runners))

@app.route("/")
def main():
    return render_template("main.html", runners=fetch_all_runners())

def parse_entry(entry:str) -> tuple[str,list[str]]:
    date, runners = entry.split(":")
    return date.strip(),[runner.strip() for runner in runners.split(",")]


def fetch_toplist(max_run_count:int|None) -> tuple[int,list[dict]]:
    runs = []
    runcount = 0
    with open("sortabla.yaml") as f:
        for line in f:
            runs.extend(parse_entry(line)[1])
            runcount += 1
            if runcount == max_run_count: break
    return runcount, sorted([
        {
            "name" : runner,
            "count" : runs.count(runner)
        }
        for runner in set(runs)
    ], key= lambda x: x["count"], reverse=True)

@app.route("/toplist")
@app.route("/toplist/<int:run_count>")
def toplist(run_count:int|None = None):
    if run_count and run_count < 1: return redirect(url_for("error"))
    max, data = fetch_toplist(run_count)
    return render_template("toplist.html", count = run_count, data=data, max=max)

@app.route("/toplist", methods=["POST"])
def toplist_generator():
    if "run_count" not in request.form: return redirect(url_for("error"))
    run_count = request.form["run_count"]
    return toplist(None if run_count=="" else int(run_count))
    
def fetch_runs(user:str) -> list[str]:
    runs = []
    with open("sortabla.yaml") as f:
        for line in f:
            date, runners = parse_entry(line)
            if user in runners:
                runs.append(date)
    return runs

@app.route("/runner/<id>")
def runner(id:str):
    runs = fetch_runs(id)
    if len(runs) == 0: return redirect(url_for("error"))
    return render_template("runner.html", runner=id, runs=runs)

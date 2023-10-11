from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

def fetch_toplist(max_run_count:int|None) -> tuple[int,list[dict]]:
    runs = []
    runcount = 0
    with open("sortabla.yaml") as f:
        for line in f:
            runs.extend([ runner.strip() for runner in line.split(":")[1].split(",")])
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
    print(fetch_toplist(run_count))
    max, data = fetch_toplist(run_count)
    return render_template("toplist.html", count = run_count, data=data, max=max)
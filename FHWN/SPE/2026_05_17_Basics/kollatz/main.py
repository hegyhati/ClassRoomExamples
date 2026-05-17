from flask import Flask, jsonify, redirect, url_for
import kollatz.kollatz as kollatz
import random

app = Flask(__name__)


@app.route("/normal/")
def random_normal():
    num = random.randint(1, 1000000000000000000)
    return redirect(url_for("normal_kollatz_route", num=num))


@app.route("/normal/<int:num>")
def normal_kollatz_route(num: int):
    seq = kollatz.get_sequence(num)
    return jsonify({
        "steps" : len(seq)-1,
        "sequence": seq
    })

@app.route("/cached/")
def random_cached():
    num = random.randint(1, 1000000000000000000)
    return redirect(url_for("cached_kollatz_route", num=num))


@app.route("/cached/<int:num>")
def cached_kollatz_route(num: int):
    seq = kollatz.get_sequence_cached(num)
    return jsonify({
        "steps" : len(seq)-1,
        "sequence": seq
    })


@app.route("/dummy/")
def dummy():
    return jsonify({
        "steps" : 0,
        "sequence": [1]
    })

if __name__ == "__main__":
    app.run(debug=True)
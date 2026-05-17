from flask import Flask, jsonify, redirect, url_for
import random

app = Flask(__name__)



def is_prime(int: num) -> bool:
    for div in range(2,num):
        if num % div == 0:
            return False
    return True


def primes_in_range(start: int, end:int|None = None) -> list[int]:
    if end is None: end = 2*start
    return [num for num in range(start,end) if is_prime(num)]
            

@app.route("/primes/<int:num>")
def primes_in_range_1(num: int):
    return jsonify(primes_in_range(num))

@app.route("/primes/<int:num>/<int:num2>")
def primes_in_range_2(num: int, num2: int):
    return jsonify(primes_in_range(num, num2))

if __name__ == "__main__":
    app.run()
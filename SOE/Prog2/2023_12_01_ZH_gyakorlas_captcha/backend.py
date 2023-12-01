from time import sleep
from flask import Flask, send_file
import os
from random import choice, randint

app = Flask(__name__)

@app.route('/animals')
def animals():
    return os.listdir('animals')

@app.route('/random/<animal>')
def random(animal):
    sleep(randint(1,200)/10)
    file = choice(os.listdir('animals/' + animal))
    return send_file('animals/' + animal + '/' + file)
from flask import render_template, request
from main import app
from main.forms import RPSbuttons
import random


@app.route('/', methods=['GET', 'POST'])
@app.route('/play', methods=['GET', 'POST'])
def play():
    vs = 'vs'
    form = RPSbuttons()
    elements = {'ROCK': 0, 'PAPER': 1, 'SCISSORS': 2}
    if request.method == "POST":
        if request.form['submit_button'] in elements.keys():
            played = request.form['submit_button']
            c_played = random.choice([k for k in elements.keys()])
            played_value = elements[played]
            c_played_value = elements[c_played]
            result = get_winner(played_value, c_played_value)
            return render_template('play.html', form=form, played=played, c_played=c_played, result=result, vs=vs)
    elif request.method == "GET":
        return render_template('play.html', form=form)


def get_winner(a, b):
    if (a + 1) % 3 == b:
        return 'Computer wins'
    elif a == b:
        return 'Draw'
    else:
        return 'Player wins'

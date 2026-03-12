#!/usr/bin/python3
""" Flask app to display a list of states """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('/states_list', strict_slashes=True)
def states_list():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    storage.close()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

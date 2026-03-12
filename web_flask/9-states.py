#!/usr/bin/python3
""" Flask app to display a list of states """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the database connection at the end of the request """
    storage.close()

@app.route('/states', strict_slashes=True)
def states():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=True)
def state_by_id(id):
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', state=state)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

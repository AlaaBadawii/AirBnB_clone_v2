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

@app.route('/hbnb_filters', strict_slashes=True)
def hbnb_filters():
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

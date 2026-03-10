#!/usr/bin/python3
"""scritp that starts Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Home():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return  "C {}".format(text.replace('_', ' '))

@app.route("/python")
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):    
    return "Python {}".format(text.replace('_', ' '))

@app.route("/number/<int:n>", strict_slashes=True)
def number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
def py():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def num(n):
    return f'{n}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Flask app to display a list of states """
from flask import Flask
from models import storage

states = storage.all()
storage.close()


app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

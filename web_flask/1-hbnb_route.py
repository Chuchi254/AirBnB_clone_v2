#!/usr/bin/python3
"""
This module starts a Flask web application with two routes.
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' when accessing the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB' when accessing the /hbnb route.
    """
    return "HBNB"


if __name__ == "__main__":
    """
    Run the Flask web application.
    """
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3
"""
This module starts a Flask web application with five routes.
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
    Display 'HBNB' when accessing the /HBNB route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable, with
    underscores replaced by splaces.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Display 'Python ' followed by the value of the text variable, with
    underscores replaced by spaces. The default value is value is 'is cool'
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display '<n> is a number' only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    """
    Run the Flask web application.
    """
    app.run(host="0.0.0.0", port=5000)

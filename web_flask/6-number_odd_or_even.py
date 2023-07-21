#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Returns a string"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
def display_python(text='cool'):
    """Returns a string"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """Returns a string"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_html(n):
    """Returns HTML page"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Returns HTML page"""
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    if isinstance(n, int):
        return render_template('6-number.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

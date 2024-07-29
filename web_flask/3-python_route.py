#!/usr/bin/python3
"""
This script starts a new flask web application
The requirements are:
    / to display "Hello HBNB!"
    /hbnb to display "HBNB"
    /c/<text> -  C text
    /python/<text> - Python text
    default value of text is "is cool"
"""


from flask import Flask

# instantiate a Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """This function returns string 'Hello HBNB' in the / directory"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_2():
    """This function returns string 'HBNB' in the /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_world_3(text):
    """Function returns 'C' followed by (space replaced underscores) text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_world_4(text):
    """Returns 'Python' followed by (space replaced underscores) text
    Note: <text> defaults to 'is cool' if undefined"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000)

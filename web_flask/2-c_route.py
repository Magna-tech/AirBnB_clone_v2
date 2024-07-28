#!/usr/bin/python3
""" Starts a Flask application that MUST be listening on 0.0.0.0, port 5000.
        routes: /:display "Hello HBNB!", /hbnb: display "HBNB" &
               /c/<text>: display "C" forllowed by 'text' variable (with any
               underscores replaced by a space)
        MUST use the option 'strict_slashes=False in route definition
"""


from flask import Flask, escape

# instantiate a Flask app
app = Flask(__name__)


# define a route to trigger the function defined right after
@app.route('/', strict_slashes=False)
def hello_world():
    """ Display 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_2():
    """ Display 'HBNB' """
    return "HBNB"


# the route captures a value (text) from the URL & passes to the function
@app.route('/c/<text>', strict_slashes=False)
def hello_world_3(text):
    """ Returns 'C' followed by (space replaced underscores) text """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
This module starts a Flask application listening on 0.0.0.0, port 5000.
It defines the following routes:
    - /:display "Hello HBNB!"
    - /hbnb: display "HBNB"
    - /c/<text>: display "C" forllowed by 'text' variable (with any
      underscores replaced by a space).
      'strict_slashes=False in route definition
"""


from flask import Flask

# instantiate a Flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Display 'Hello HBNB' at the root route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_2():
    """ Display 'HBNB' at the /hbnb route. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_world_3(text):
    """ Returns 'C' followed by (space replaced underscores) text """
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    # Run the Flask app on all public IPs, port 5000
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
Required
    routes: /:display "Hello HBNB!", /hbnb: display "HBNB" &
            /c/<text>: display "C" forllowed by 'text' variable (with any
                underscores replaced by a space)
            /python/(<text>): display "Python" + what /c/<text> does...
                with 'text' having the default value "is cool"
            /number/<n>: display "n is a number" ONLY IF n is an int
    MUST use the option 'strict_slashes=False in route definition
"""


from flask import Flask

# instantiate a Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """This function returns 'Hello HBNB' in the home directory"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world_2():
    """This function returns 'HBNB' in the /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_world_3(text):
    """Returns 'C' followed by (space replaced underscores) text"""
    return "C {}".format(text.replace('_', ' '))


# route to trigger if no 'text' in url (defaults to defaults value)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
# route to trigger if 'text' in url
@app.route('/python/<text>', strict_slashes=False)
def hello_world_4(text):
    """Returns 'Python' followed by (space replaced underscores) text
    Note: <text> defaults to 'is cool' if undefined"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """returns "n is a number" if n is an int"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000)

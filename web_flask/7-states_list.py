#!/usr/bin/python3
"""
Starts a Flask application that MUST be listening on 0.0.0.0, port 5000.
Required:
    MUST use 'storage' for fetching data from the storage engine (
    FileStorage or DBStorage) & remove the current session after each
    request
    routes: /:display "Hello HBNB!"
    strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models.state import State

# instantiate a Flask application
app = Flask(__name__)


@app.teardown_appcontext
def close_context(exception):
    """ Tear down/removes current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Render an HTML template with all the States """
    # get dict values from all() results
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # Run the flask app to listen on all public IPs, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

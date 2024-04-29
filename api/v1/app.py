#!/usr/bin/python3
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
<< << << < HEAD
""" instance of Flask"""


app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    """status of api"""
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    """return render template"""
    return jsonify(err="Not found"), 404


== == == =
"""
app
"""


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }


>>>>>> > 12d342685be55844afd9d0c2d329e685845f7265

resp = jsonify(data)
resp.status_code = 404

<< << << < HEAD
if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True)
== == == =
return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
>>>>>> > 12d342685be55844afd9d0c2d329e685845f7265

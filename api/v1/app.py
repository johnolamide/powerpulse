#!/usr/bin/python3
"""
This script contains the api entry point for powerpulse
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from model import storage
from os import getenv


app = Flask(__name__)
host = '0.0.0.0'
cors = CORS(app, resources={r'/*': {'origins': host}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ handles 404 error """
    response = {'error': "Not Found"}
    return jsonify(response), 404


if __name__ == "__main__":
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)

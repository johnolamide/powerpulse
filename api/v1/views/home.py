#!/usr/bin/python3
"""
Home views api
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from model import storage


@app_views.route('/home', methods=['GET'], strict_slashes=False)
def get_homes():
    """ gets all the home data """
    homes = []
    for home in storage.all():
        homes.append(home)
    return jsonify(homes)

@app_views.route('/home/<home_id>', methods=['GET'], strict_slashes=False)
def get_home(home_id):
    """ get specific home data """
    home = storage.get(home_id)
    if home:
        response = home
        return jsonify(response)
    abort(404)

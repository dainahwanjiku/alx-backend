#!/usr/bin/env python
"""
how to setup a basic Flask app
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_app():
    """single route and an index.html template"""
    return 'First Flask application!'

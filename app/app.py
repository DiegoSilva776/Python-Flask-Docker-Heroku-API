# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import request

from werkzeug.serving import WSGIRequestHandler

# Construction
app = Flask(__name__)

# Routing
@app.route('/')
def hello():
    return 'My app API'

'''
    Initilization
'''
if __name__ == '__main__':
	app.run(host='0.0.0.0')
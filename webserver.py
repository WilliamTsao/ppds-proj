#!/usr/bin/python3

from flask import Flask, render_template, request
from datetime import datetime
import urllib
app = Flask(__name__)

import api


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    """process request.params"""
    searchString = request.args.get('s')
    data={
        "q": searchString
    }
    """make api call """
    api_res = api.searchFood(data)
    """clean up api respond """
    print(api_res)
    hits = api_res['hits']
    """send back respond"""
    return render_template('search.html', hits=hits)


@app.route('/login')
def login():
    return render_template('login.html')



app.run(host='0.0.0.0', port=8000, debug=True)


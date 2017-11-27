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
    for hit in hits:
        hit['ref'] = hit['recipe']['uri'].split('#')[1]

    """send back respond"""
    return render_template('search.html', hits=hits)

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/recipe/<ref>')
def recipe(ref):
    recipe = api.recipe(ref)
    nutritions = []
    for (key, value) in recipe['totalNutrients'].items():
        nutritions.append(value)
        pass
    return render_template('recipe.html', recipe=recipe, nutritions=nutritions)

@app.route('/log', methods=['POST'])

app.run(host='0.0.0.0', port=8000, debug=True)


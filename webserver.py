#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

import api, db

def validate(form):
    if('username' not in form):
        return False
    if ('password' not in form):
        return False
    if (form['username'] == ''):
        return False
    if (form['password'] == ''):
        return False
    return True



@app.route('/')
def home():
    url_for('static', filename='style.css')
    return render_template('index.html')

@app.route('/search')
def search():
    url_for('static', filename='style.css')
    """process request.params"""
    searchString = request.args.get('s')
    data={
        "q": searchString
    }
    """make api call """
    api_res = api.searchFood(data)
    """clean up api respond """
    hits = api_res['hits']
    for hit in hits:
        hit['ref'] = hit['recipe']['uri'].split('#')[1]

    """send back respond"""
    return render_template('search.html', hits=hits)

@app.route('/signup', methods=['GET'])
def signup():
    url_for('static', filename='style.css')
    return render_template('signup.html')

@app.route('/login', methods=['GET'])
def login():
    url_for('static', filename='style.css')
    return render_template('login.html')


@app.route('/signup', methods=['POST'])
def register():
    if (not validate(request.form)):
        return render_template('signup.html', error = "Missing username or password")

    u = User(request.form.username, request.form.password)
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def authenticate():
    return render_template('login.html')



@app.route('/recipe/<ref>')
def recipe(ref):
    url_for('static', filename='style.css')
    recipe = api.recipe(ref)
    nutritions = []
    for (key, value) in recipe['totalNutrients'].items():
        nutritions.append(value)
        pass
    return render_template('recipe.html', recipe=recipe, nutritions=nutritions)

@app.route('/log', methods=['POST'])
def log():
    # redirect to /dashboard
    return "haha"

app.run(host='0.0.0.0', port=8000, debug=True)


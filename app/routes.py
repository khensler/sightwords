from flask import current_app as app
from flask import render_template, redirect, flash, request

@app.route('/')
@app.route('/index')
def index():
     return render_template('words.html',word='asdf')
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request
from domain import emojify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('landing_page.html')
    elif request.method == 'POST':
        return emojify(request.form['text'])
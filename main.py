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
        # print(request.get_json()['text'])
        # return '{method:"POST",url:"http://127.0.0.1:5000", "headers":{"Content-Type":["application/x-www-form-urlencoded"]}, body:"text=india"}'
        result = emojify(request.get_json()['text'])
        # print(result)
        return {"text" : str(result)}

@app.route("/robots.txt")
def robots():
    return "User-agent: *\nAllow: /"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    
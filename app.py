#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def form():
    if request.method== 'POST':
         username=request.form['nom']
    else :
        username="try again"

    return render_template('index.html',username=username)


if __name__ == '__main__':
    app.run(debug=True) 
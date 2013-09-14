#!/usr/bin/env python
# coding=utf-8

"""
main entrance to the web app
"""

from flask import (Flask, render_template, url_for,
                   request,
                   redirect)

from jinja2 import Environment

from jinja2_highlight.highlight import HighlightExtension

from etpaste import vdb


app = Flask(__name__)
app.jinja_env.add_extension(HighlightExtension)


@app.route("/")
def home():
    return redirect(url_for("new_paste"))


@app.route("/t1")
def t1():
    return render_template('t1.html')


@app.route("/about")
def about():
    raise Exception("not_implemented")


@app.route("/paste/new")
def new_paste():
    return render_template('new_paste.html')


@app.route("/paste/<paste_id>")
def show_paste(paste_id):
    try:
        paste_id = int(paste_id)
    except ValueError as e:
        return "Bad paste_id."
    p = vdb.get_paste(paste_id)
    return render_template('show_paste.html', paste=p, paste_id=paste_id)


@app.route("/paste", methods=("POST",))
def post_paste():
    lang = request.form['lang']
    content = request.form['content']
    if not lang or not content:
        redirect(url_for('new_paste'))
    paste_id = vdb.new_paste(lang, content)
    return redirect(url_for('show_paste', paste_id=paste_id))


if __name__ == "__main__":
    app.run(debug=True)

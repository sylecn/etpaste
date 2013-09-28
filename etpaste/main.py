#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2013  Yuanle Song <sylecn@gmail.com>
#
# This file is part of etpaste.
#
# etpaste is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# etpaste is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with etpaste.  If not, see <http://www.gnu.org/licenses/>.
#

"""
main entrance to the web app
"""

import pygments

from flask import (Flask, render_template, url_for,
                   request,
                   redirect, abort)

from etpaste import vdb

from etpaste.utils import highlight_text, guess_language
from etpaste.version import VERSION


app = Flask(__name__)
app.jinja_options = {"trim_blocks": True}


@app.context_processor
def inject_version():
    return {'VERSION': VERSION}


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/guess")
def guess():
    return render_template('guess.html')


@app.route("/guess", methods=("POST",))
def post_guess():
    content = request.form['content']
    if not content:
        return "Paste in some text below"
    lang = guess_language(content)
    if lang:
        return "Guessed language for this text is " + lang
    else:
        return "Guess has failed."


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
    if not p['ok']:
        abort(404)
    p['html'] = highlight_text(p['content'], p['lang'])
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

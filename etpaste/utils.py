#!/usr/bin/env python
# coding=utf-8

"""
utils
"""

import pygments
import pygments.lexers
import pygments.formatters
import pygments.util


HTML_FORMATTER = pygments.formatters.html.HtmlFormatter()


def highlight_text(text, lang):
    lexer = pygments.lexers.get_lexer_by_name(lang)
    return pygments.highlight(text, lexer, HTML_FORMATTER)


def guess_language(text):
    """guess the programming language used in given text.

    return a string if guess is successful, return None if guess failed.

    """
    if not text:
        return "emtpy string"
    try:
        lexer = pygments.lexers.guess_lexer(text)
        return lexer.name
    except pygments.util.ClassNotFound as e:
        return None


def error(**kwargs):
    r = dict(kwargs)
    r['ok'] = False
    return r


def ok(**kwargs):
    r = dict(kwargs)
    r['ok'] = True
    return r

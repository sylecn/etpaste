#!/usr/bin/env python
# coding=utf-8

"""
utils
"""

import pygments
import pygments.lexers
import pygments.formatters


HTML_FORMATTER = pygments.formatters.html.HtmlFormatter()


def highlight_text(text, lang):
    lexer = pygments.lexers.get_lexer_by_name(lang)
    return pygments.highlight(text, lexer, HTML_FORMATTER)


def error(**kwargs):
    r = dict(kwargs)
    r['ok'] = False
    return r


def ok(**kwargs):
    r = dict(kwargs)
    r['ok'] = True
    return r

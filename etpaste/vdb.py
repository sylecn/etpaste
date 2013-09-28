#!/usr/bin/env python
# coding=utf-8

"""
vdb
"""

import arrow

from .utils import error, ok


db = []


def new_paste(lang, content):
    db.append({
        "id": len(db),
        "lang": lang,
        "content": content,
        "post_time": arrow.utcnow()})
    return len(db) - 1          # this is fragile, only works for single
                                # thread program.


def get_paste(paste_id):
    try:
        return ok(**db[paste_id])
    except IndexError as e:
        return error(msg="not found")


def get_recent_paste():
    """return most recent 10 paste.

    Return recent 10 pastes's paste_id as an iterable.

    """
    return (p for p in db[-1:-10:-1])

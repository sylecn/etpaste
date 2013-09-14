#!/usr/bin/env python
# coding=utf-8

"""
vdb
"""

db = []


def new_paste(lang, content):
    db.append({"lang": lang,
               "content": content})
    return len(db) - 1


def get_paste(paste_id):
    try:
        return db[paste_id]
    except IndexError as e:
        return {}

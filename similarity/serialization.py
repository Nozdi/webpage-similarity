"""
.. module:: train
    :synopsis: This module provides pickling objects
"""
from pickle import (
    dump,
    load,
)
from os import path
import __main__


def dump_objects(objects, filename="db"):
    with open(filename, 'wb') as f:
        dump(objects, f, -1)


def load_objects(filename="db"):
    try:
        with open(filename, 'rb') as f:
            return load(f)
    except IOError:
        if path.basename(__main__.__file__) != "create_db.py":
            print("To use this library you need to train the system - use create_db.py")

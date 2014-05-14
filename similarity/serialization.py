"""
.. module:: train
    :synopsis: This module provides pickling objects
"""
from pickle import (
    dump,
    load,
)


def dump_objects(objects, filename="db"):
    with open(filename, 'wb') as f:
        dump(objects, f, -1)


def load_objects(filename="db"):
    with open(filename, 'rb') as f:
        return load(f)

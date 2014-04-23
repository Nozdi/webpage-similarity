"""
.. module:: train
    :synopsis: This module provides document training, dumping and loading
"""
from os import path
from glob import glob
from pickle import (
    dump,
    load,
)
from similarity.text.document import TrainingDocument
from similarity.text.category import Category


def create_categories_with_documents(directory="./texts/"):
    id_categories = [path.basename(path.normpath(full_dirname))
                  for full_dirname in glob(directory + "*/")]

    categories = []
    for category_name in id_categories:
        cat = Category(category_name)
        for filename in glob(directory + category_name + "/[0-9]*.txt"):
            with open(filename) as f:
                td = TrainingDocument(
                    name=filename,
                    text=f.read().decode("utf-8")
                )
                td.calculate_terms_belongness()
                cat.add_document(td)
        # cat.count_local_terms_weights()
        categories.append(cat)
    return categories


def dump_categories_with_documents(filename="db"):
    with open(filename, 'w') as f:
        dump(create_categories_with_documents(), f)

def load_categories_with_documents(filename="db"):
    with open(filename) as f:
        return load(f)
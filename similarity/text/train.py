"""
.. module:: train
    :synopsis: This module provides document training, dumping and loading
"""
from os import path
from glob import glob

from similarity.text.category import (
    Category,
    term_to_cat_relevance,
)
from similarity.text.document import TrainingDocument


def create_categories_with_documents(directory="./texts/"):
    id_categories = [path.basename(path.normpath(full_dirname))
                     for full_dirname in glob(directory + "*/")]

    categories = []
    for category_name in id_categories:
        cat = Category(category_name)
        for filename in glob(directory + category_name + "/[0-9]*.txt"):
            td = TrainingDocument.from_file(filename, filename)
            cat.add_document(td)
        categories.append(cat)
    return categories


def create_terms_to_categories_relevance():
    categories = create_categories_with_documents()
    terms_revelance = {}
    for category in categories:
        terms_revelance[category.identifier] = {}
        for term in category.termsQuantity:
            terms_revelance[category.identifier][term] = term_to_cat_relevance(
                term,
                category,
                categories,
            )
    return terms_revelance

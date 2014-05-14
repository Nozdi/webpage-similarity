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
from similarity.text.category import (
    Category,
    term_to_cat_relevance,
)


def create_categories_with_documents(directory="./texts/"):
    from similarity.text.document import TrainingDocument
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


def dump_objects(objects, filename="db"):
    with open(filename, 'wb') as f:
        dump(objects, f, -1)


def load_objects(filename="db"):
    with open(filename, 'rb') as f:
        return load(f)


if __name__ == '__main__':
    dump_objects(create_categories_with_documents(), "cats")
    print(load_objects("cats"))
    dump_objects(create_terms_to_categories_relevance("db"))
    print(load_objects("db"))

#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""

from similarity.text.document import AnalizedDocument
from similarity.text.train import load_categories_with_documents
from similarity.fuzzy import jaccard

categories = load_categories_with_documents()

test_doc_file = open('test_doc', 'r')
test_doc_file2 = open('test_doc', 'r')

test_doc = AnalizedDocument(name="Testing", text=test_doc_file.read())
test_doc.calculate_belongness_to_categories(categories)

test_doc2 = AnalizedDocument(name="Testing2", text=test_doc_file2.read())
test_doc2.calculate_belongness_to_categories(categories)

for cat in test_doc.belongnessToCategories.keys():
    print cat.identifier
    print test_doc.belongnessToCategories[cat]
    print

for cat in test_doc2.belongnessToCategories.keys():
    print cat.identifier
    print test_doc2.belongnessToCategories[cat]
    print

print jaccard(
    test_doc.belongnessToCategories,
    test_doc2.belongnessToCategories,
    min,
    max,
)

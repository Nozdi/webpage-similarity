#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""
from operator import itemgetter
from sys import argv
from similarity.text.document import AnalizedDocument
from webpage import WebPage


def print_sorted_dict(dictionary, name):
    print name
    shit = sorted(dictionary.iteritems(), key=itemgetter(1), reverse=True)
    for key, value in shit:
        print str(key), ":", value


if __name__ == '__main__':
    if len(argv) == 3:
        w1 = WebPage(AnalizedDocument.from_file(argv[1]))
        w2 = WebPage(AnalizedDocument.from_file(argv[2]))
    else:
        w1 = WebPage(AnalizedDocument.from_file('test_doc'))
        w2 = WebPage(AnalizedDocument.from_file('test_doc2'))
    print w1.get_text_similarity(w2)
    # from similarity.serialization import load_objects
    # categories = load_objects("cats")
    # w1.content.calculate_belongness_to_categories(categories)

    print_sorted_dict(w1.content.categories_membership, "dog")
    print_sorted_dict(w2.content.categories_membership, "cat")

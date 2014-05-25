#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""
from operator import itemgetter
from sys import argv
from similarity.text.document import AnalizedDocument
from similarity.img.compare import compare
from PIL import Image
from webpage import WebPage


def print_sorted_dict(dictionary, name):
    print name
    sdict = sorted(dictionary.iteritems(), key=itemgetter(1), reverse=True)
    for key, value in sdict:
        print str(key), ":", value


if __name__ == '__main__':
    if len(argv) == 3:
        ad1 = AnalizedDocument.from_file(argv[1])
        ad2 = AnalizedDocument.from_file(argv[2])
    else:
        w1 = WebPage(url="http://en.wikipedia.org/wiki/Zebra")
        w2 = WebPage(url="http://en.wikipedia.org/wiki/Gothic_architecture")
        # ad1 = AnalizedDocument.from_file('test_doc')
        # ad2 = AnalizedDocument.from_file('test_doc2')
    print w1.get_text_similarity(w2)
    # print ad1.compare(ad2)

    # print_sorted_dict(ad1.categories_membership, "zyrafy")
    # print_sorted_dict(ad2.categories_membership, "zebry")
    print_sorted_dict(w1.content.categories_membership, "zebry")
    print_sorted_dict(w2.content.categories_membership, "gotyk")

    print("\nImages similarity:")
    print(compare(Image.open("red.jpg"), Image.open("pom.png")))

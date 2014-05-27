#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""
from operator import itemgetter
from sys import argv
from similarity.text.document import AnalizedDocument
from similarity.img.compare import compare
from similarity.img.compare import compare_many
from PIL import Image
from similarity import WebPage
from glob import glob


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
        w1 = WebPage(url="http://swimming.about.com/cs/gettingstarted/a/getting_started.htm")
        w2 = WebPage(url="http://biology.about.com/b/2014/05/21/dangerous-bacteria-on-aircraft-cabin-surfaces.htm")
        # ad1 = AnalizedDocument.from_file('test_doc')
        # ad2 = AnalizedDocument.from_file('test_doc2')
    print w1.get_text_similarity(w2)
    # print ad1.compare(ad2)

    # print_sorted_dict(ad1.categories_membership, "zyrafy")
    # print_sorted_dict(ad2.categories_membership, "zebry")
    print_sorted_dict(w1.content.categories_membership, "plywanie")
    print_sorted_dict(w2.content.categories_membership, "bakterie")

    print("\nImages similarity:")
    print(compare(Image.open("./data/red.jpg"), Image.open("./data/pom.png")))

    img_list1 = []
    img_list2 = []

    for filename in glob("./data/test_a/*"):
        img_list1.append(Image.open(filename))

    for filename in glob("./data/test_b/*"):
        img_list2.append(Image.open(filename))

    print(compare_many(img_list1, img_list2))

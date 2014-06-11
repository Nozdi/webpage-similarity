#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""
import fix_path
from similarity.text.document import AnalizedDocument
from similarity.img.compare import (
    compare,
    compare_many
)
from utils import print_sorted_dict
from PIL import Image
from glob import glob
from os import path


if __name__ == '__main__':
    ad1 = AnalizedDocument.from_file("./data/test_doc")
    ad2 = AnalizedDocument.from_file("./data/test_doc2")

    print "Text Similarity for ad1 and ad2"
    comparsion = ad1.compare(ad2)
    print "Result: ", comparsion.similarity_result
    print "Important categories:"
    for cat in comparsion.important_categories:
        print cat

    print_sorted_dict(ad1.categories_membership, "test_doc")
    print_sorted_dict(ad2.categories_membership, "test_doc2")

    print "Two images:"
    im1 = Image.open("./data/red.jpg")
    im2 = Image.open("./data/pom.png")
    print compare(im1, im2)

    print "Many images:"
    first_group = glob("./data/test_a/*")
    sec_group = glob("./data/test_b/*")
    creator = lambda x: (x, Image.open(x))
    comparsion = compare_many(map(creator, first_group), map(creator, sec_group))

    print "Result: ", comparsion.similarity_result
    print "Pictures with each other:"
    for pair, result in comparsion.image_pairs_results.items():
        first, sec = map(lambda x: path.split(x)[-1], pair)
        print "{} : {} is {}".format(first, sec, result)

#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""
import fix_path
from similarity import WebPage
from utils import print_sorted_dict
from os import path


if __name__ == '__main__':
    w1 = WebPage(
        url="http://automotive.about.com/b/2012/06/14/how-to-become-a-new-car-dealer.htm"
    )
    w2 = WebPage(
        url="http://ipod.about.com/od/KidsiPhoneiPodTouch/tp/Roadtrips-With-Iphone-And-Apps.htm"
    )

    print "Text Similarity for w1 and w2"
    comparsion = w1.get_text_similarity(w2)

    print "Result: ", comparsion.similarity_result
    print "Important categories:"
    for cat in comparsion.important_categories:
        print cat

    print_sorted_dict(w1.content.categories_membership, "car")
    print_sorted_dict(w2.content.categories_membership, "ipod")

    print("\nMany images:")
    comparsion = w1.get_image_similatiry(w2)
    print "Result: ", comparsion.similarity_result
    print "Pictures with each other:"
    for pair, result in comparsion.image_pairs_results.items():
        first, sec = map(lambda x: path.split(x)[-1], pair)
        print "{} : {} is {}".format(first, sec, result)

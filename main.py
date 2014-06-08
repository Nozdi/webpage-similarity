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
from html_result import HtmlResultCreator
from PIL import Image
from similarity import WebPage
from glob import glob
import webbrowser


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
        w1 = WebPage(url="http://americanfood.about.com/od/appetizersandsoups/r/roasted-garlic.htm")
        w2 = WebPage(url="http://ipod.about.com/od/KidsiPhoneiPodTouch/tp/Roadtrips-With-Iphone-And-Apps.htm")

    print "TextSimilarity for w1 and w2"
    text_similarity = w1.get_text_similarity(w2)
    print text_similarity

    print_sorted_dict(w1.content.categories_membership, "food")
    print_sorted_dict(w2.content.categories_membership, "ipod")

    print("\nMany images:")
    image_similarity = w1.get_image_similatiry(w2)
    print image_similarity

    html_result_creator = HtmlResultCreator(template_path="template2.html")
    html_result_creator.first_web_page = w1
    html_result_creator.second_web_page = w2
    html_result_creator.text_similarity = text_similarity
    html_result_creator.image_similarity = image_similarity
    created_html_path = "./Output.html"
    html_result_creator.create(created_html_path)

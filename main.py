#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""

from sys import argv
from similarity.text.document import AnalizedDocument
from webpage import WebPage


if __name__ == '__main__':
    if len(argv) == 3:
        w1 = WebPage(AnalizedDocument.from_file(argv[1]))
        w2 = WebPage(AnalizedDocument.from_file(argv[2]))
    else:
        w1 = WebPage(AnalizedDocument.from_file('test_doc'))
        w2 = WebPage(AnalizedDocument.from_file('test_doc2'))
    print w1.get_text_similarity(w2)

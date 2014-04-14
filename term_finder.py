#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from topia.termextract import extract

class TermFinder(object):


    def __init__(self, text):
        self.text = text


    def exctract(self):
        """
            Finds terms in text and returns them as list of tuples
            ( term, term amount, term length in  words)
        """
        extractor = extract.TermExtractor()
        extractor.filter = extract.permissiveFilter
        return extractor(self.text)

if __name__ == "__main__":
    argv=sys.argv
    with open (argv[1], "r") as myfile:
        text=myfile.read().replace('\n', ' ')
    termFinder =  TermFinder(text)
    extracted =  termFinder.exctract()
    print len(extracted)
    print extracted

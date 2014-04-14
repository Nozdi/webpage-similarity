#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from topia.termextract import extract

def exctract(text):
    """
            Finds terms in text and returns them as list of tuples
            ( term, term amount, term length in  words)
    """
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter
    return extractor(text)

if __name__ == "__main__":
    argv=sys.argv
    with open (argv[1], "r") as myfile:
        text=myfile.read().replace('\n', ' ')
    extracted =  exctract(text)
    print len(extracted)
    print extracted

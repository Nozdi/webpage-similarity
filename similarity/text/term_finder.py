#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from topia.termextract import extract

def extract_terms_with_quantity_from_text(text):
    """
            Finds terms in text and returns them as list of tuples
            ( term, term amount)
    """
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter
    return [(term.lower(), quantity)  for term, quantity, words_no in extractor(text)]

def extract_terms_with_quantity_from_file(filename):
    """
        Finds terms in text file and returns them as list of tuples
            ( term, term amount)
    """
    with open (filename, "r") as myfile:
        text=myfile.read().replace('\n', ' ')
        return extract_terms_with_quantity_from_text(text)


def extract_all_terms_from_files(filenames):
    """
        Finds terms in text files and returns them as list
    """
    words = set()
    for filename in filenames:
        words |= set(extract_terms_from_file(filename))
    return list(words)

def extract_terms_from_file(filename):
    """
        Finds terms in text file and returns them as list
    """
    with open (filename, "r") as myfile:
        text=myfile.read().replace('\n', ' ')
        return [term for term, quantity in extract_terms_with_quantity_from_text(text)]


if __name__ == "__main__":
    argv=sys.argv
    result =  extract_all_terms_from_files([argv[1]])
    print len(result)
    print result
    #with open (argv[1], "r") as myfile:
    #    text=myfile.read().replace('\n', ' ')
    #extracted =  exctract(text)
    #print len(extracted)
    #print extracted

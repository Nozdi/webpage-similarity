"""
.. module:: document
    :synopsis: This module provides webpage object
"""

from similarity.serialization import load_objects
from similarity.fuzzy import jaccard
from copy import copy
from operator import itemgetter


class WebPage(object):
    """
        Represents analized webpage.

        :field content: object of Document class
        :type content: Document
        :field url: url to a webpage
        :type url: string
    """
    categories = load_objects('cats')

    def __init__(self, document, url="http://google.com"):
        """
            :param document: object of Document class
            :type document: Document
            :param url: url to a webpage
            :type url: string
        """
        self.url = url
        self.content = document

    def get_text_similarity(self, web_page):
        self.content.calculate_membership_to_categories(self.categories)
        if not web_page.content.categories_membership:
            web_page.content.calculate_membership_to_categories(self.categories)

        changed_membership = copy(self.content.categories_membership)
        categories_by_membership = sorted(
            self.content.categories_membership.iteritems(),
            key=itemgetter(1),
            reverse=True
        )
        maximal_value = categories_by_membership[0][1]

        for key in changed_membership:
            changed_membership[key] /= maximal_value

        importance = len(filter(lambda x: x> .5, changed_membership.values()))
        important_categories = categories_by_membership[:importance]

        return jaccard(
            dict(important_categories),
            web_page.content.categories_membership,
            min,
            max,
        )

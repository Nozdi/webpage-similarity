"""
.. module:: document
    :synopsis: This module provides webpage object
"""

from similarity.serialization import load_objects
from similarity.fuzzy import jaccard


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
        self.content.calculate_belongness_to_categories(self.categories)
        if not web_page.content.belongnessToCategories:
            web_page.content.calculate_belongness_to_categories(self.categories)
        return jaccard(
            self.content.belongnessToCategories,
            web_page.content.belongnessToCategories,
            min,
            max,
        )

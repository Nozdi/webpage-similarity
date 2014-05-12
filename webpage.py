"""
.. module:: document
    :synopsis: This module provides webpage object
"""

from similarity.text.document import categories


class WebPage(object):
    """
        Represents analized webpage.

        :field content: object of Document class
        :type content: Document
        :field url: url to a webpage
        :type url: string
    """

    def __init__(self, document, url):
        """
            :param document: object of Document class
            :type document: Document
            :param url: url to a webpage
            :type url: string
        """
        self.url = url
        self.content = document

    def get_text_similarity(self, webPage):
        # categoryMan = CategoryManager
        diff = 0.0
        for category in CategoryManager.categories
            diff += abs(webPage.document.belongnessToCategory[category]
                    - self.document.belongnessToCategory[category])

        # diff = 0 - high similarity; diff = 1 - no similarity
        diff /= len(CategoryManager.categories)

        return 1 - diff

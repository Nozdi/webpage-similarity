"""
.. module:: webpage
    :synopsis: This module provides webpage object
"""

from similarity.text.document import AnalizedDocument
from similarity.extractor import ExtendedGoose
from unidecode import unidecode
import os
import urllib


class WebPage(object):
    """
        Represents analized webpage.

        :field content: object of Document class
        :type content: Document
        :field url: url to a webpage
        :type url: string
    """
    goose = ExtendedGoose()

    def __init__(self, url="http://google.com"):
        """
            :param document: object of Document class
            :type document: Document
            :param url: url to a webpage
            :type url: string
        """

        self.url = url
        self.article = self.goose.extract(url=self.url)
        self.get_text()

    def get_text(self):
        text = self.article.cleaned_text
        self.content = AnalizedDocument(unidecode(text))

    def get_picture(self, pic_name):
        image = self.article.top_image.src
        extension = os.path.splitext(image)[1]
        urllib.urlretrieve(image, pic_name + extension)

    def get_text_similarity(self, web_page):
        return self.content.compare(web_page.content)

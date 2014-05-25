"""
.. module:: webpage
    :synopsis: This module provides webpage object
"""

from similarity.text.document import AnalizedDocument
from extractor import ExtendedGoose
from unidecode import unidecode
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
        urllib.urlretrieve(image, pic_name)

    def get_text_similarity(self, web_page):
        return self.content.compare(web_page.content)

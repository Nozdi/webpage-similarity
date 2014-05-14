"""
.. module:: document
    :synopsis: This module provides all Document-like objects
"""
from __future__ import division
from topia.termextract import extract

from similarity.fuzzy import (
    algebraic_product,
    algebraic_sum,
    jaccard,
)
from similarity.serialization import load_objects


class Document(object):
    """
        :field text: content of document
        :type text: string
        :field terms: terms extracted from text
        :type terms: list
        :field termsQuantity: key - term, value - weight from range: (0,1]
        :type termsQuantity: dictionary
        :field termsBelongness: key - term, value - term weight / max weight
        :type termsBelongness: dictionary
        :field uniqueTerms: set of terms appearing in text
        :type uniqueTerms: Set
    """
    __slots__ = 'termsQuantity',
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter

    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """

        # d = {<t1, w1>, ... <tm, wm>}
        self.termsQuantity = dict(
            [(term.lower(), quantity)
             for term, quantity, words_no in Document.extractor(text)]
        )

    @classmethod
    def from_file(cls, filename, *args, **kwargs):
        with open(filename) as f:
            return cls(f.read().decode("utf-8"), *args, **kwargs)


class TrainingDocument(Document):
    """
        Used in training phase.
        Degree of belongness to categories is not needed,
        only chrisp sets are used.
    """
    __slots__ = 'name',

    def __init__(self, text, name):
        """
            :param name: document name
            :type name: string
            :param text: content of document
            :type text: string
        """
        super(TrainingDocument, self).__init__(text)
        self.name = name

    def __str__(self):
        return self.name


class AnalizedDocument(Document):
    """
        Used for docuemnt that must be compared in final analizing phase.

        :field belongnessToCategories: key - category, value - belongness to category [0;1]
        :type belongnessToCategories: dictionary
    """
    def __init__(self, text):
        super(AnalizedDocument, self).__init__(text)
        self.termsBelongness = {}
        self.belongnessToCategories = {}

    def calculate_terms_belongness(self):
        """
        mi d(t)
        """
        denumerator = max(self.termsQuantity.values())
        for term in self.termsQuantity:
            self.termsBelongness[term] = (self.termsQuantity[term]
                                          / denumerator)

    def calculate_belongness_to_categories(self, categories):
        """
            :param categories: list of Categories
            :type categories: list
        """
        if not self.termsBelongness:
            self.calculate_terms_belongness()

        terms_revelance = load_objects('db')
        for category in categories:
            self.belongnessToCategories[category] = jaccard(
                self.termsBelongness,
                terms_revelance[category.identifier],
                algebraic_product,
                algebraic_sum,
            )

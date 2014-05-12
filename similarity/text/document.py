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


class Document(object):
    """
        :field text: content of document
        :type text: string
        :field terms: terms extracted from text
        :type terms: list
        :field termsWithWeights: key - term, value - weight from range: (0,1]
        :type termsWithWeights: dictionary
        :field termsBelongness: key - term, value - term weight / max weight
        :type termsBelongness: dictionary
        :field uniqueTerms: set of terms appearing in text
        :type uniqueTerms: Set
    """
    __slots__ = 'termsWithWeights', 'termsBelongness'
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter

    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """

        self.termsWithWeights = dict(
            [(term.lower(), quantity)
             for term, quantity, words_no in Document.extractor(text)]
        )


class TrainingDocument(Document):
    """
        Used in training phase.
        Degree of belongness to categories is not needed,
        only chrisp sets are used.
    """
    __slots__ = 'name',

    def __init__(self, name, text):
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
    def __init__(self, name, text):
        super(AnalizedDocument, self).__init__(text)
        self.termsBelongness = {}
        self.belongnessToCategories = {}
        self.name = name

    def calculate_terms_belongness(self):
        denumerator = max(self.termsWithWeights.values())

        for term in self.termsWithWeights:
            self.termsBelongness[term] = (self.termsWithWeights[term]
                                          / denumerator)

    def calculate_belongness_to_categories(self, categories):
        """
            :param categories: list of Categories
            :type categories: list
        """


        self.calculate_terms_belongness()

        for category in categories:
            # for term in self.termsBelongness:
            #     numerator += algebraic_product(
            #         category.belongingTerms.get(term, default),
            #         self.termsBelongness[term])

            #     denumerator += algebraic_sum(
            #         category.belongingTerms.get(term, default),
            #         self.termsBelongness[term]
            #     )

            # self.belongnessToCategories[category] = numerator / denumerator
            self.belongnessToCategories[category] = jaccard(
                self.termsBelongness,
                category.belongingTerms,
                algebraic_product,
                algebraic_sum
            )

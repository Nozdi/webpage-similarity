"""
.. module:: document
    :synopsis: This module provides all Document-like objects
"""

from topia.termextract import extract

from similarity.fuzzy import (
    algebraic_product,
    algebraic_sum,
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
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter

    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """
        self.text = text

        self.termsWithWeights = dict(
            [(term.lower(), quantity)
             for term, quantity, words_no in Document.extractor(text)]
        )
        self.termsBelongness = {}

    def __str__(self):
        return self.name

    def calculate_terms_belongness(self):
        denumerator = self.termsWithWeights.get(max(self.termsWithWeights))

        for term in self.termsWithWeights:
            self.termsBelongness[term] = (self.termsWithWeights.get(term)
                                          / denumerator)


class TrainingDocument(Document):
    """
        Used in training phase.
        Degree of belongness to categories is not needed,
        only chrisp sets are used.
    """
    def __init__(self, name, text):
        """
            :param name: document name
            :type name: string
            :param text: content of document
            :type text: string
        """
        super(TrainingDocument, self).__init__(text)
        self.name = name


class AnalizedDocument(Document):
    """
        Used for docuemnt that must be compared in final analizing phase.

        :field belongnessToCategories: key - category, value - belongness to category [0;1]
        :type belongnessToCategories: dictionary
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.belongnessToCategories = {}

    def calculate_belongness_to_categories(self, categories):
        """
            :param categories: list of Categories
            :type categories: list
        """
        numerator = 0.0
        denumerator = 0.0

        self.calculate_terms_belongness()

        for category in categories:
            for term, value in self.termBelongness:
                numerator += algebraic_product(
                    category.beloningTerms.get(term),
                    self.termBelongness.get(term))

                denumerator += algebraic_sum(category.beloningTerms.get(term),
                 self.termBelongness.get(term))

            self.belongnessToCategories[category] = numerator / denumerator

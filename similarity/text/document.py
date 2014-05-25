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
from copy import copy
from operator import itemgetter


class Document(object):
    """
        :field text: content of document
        :type text: string
        :field terms_quantity: key - term, value - weight from range: (0,1]
        :type terms_quantity: dictionary
    """
    __slots__ = 'terms_quantity',
    extractor = extract.TermExtractor()
    extractor.filter = extract.permissiveFilter

    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """

        # d = {<t1, w1>, ... <tm, wm>}
        self.terms_quantity = dict(
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
        :field terms_membership: key - term, value - term weight / max weight
        :type terms_membership: dictionary
    """
    categories = load_objects('cats')

    def __init__(self, text):
        super(AnalizedDocument, self).__init__(text)
        self.terms_membership = {}
        self.categories_membership = {}

    def calculate_terms_membership(self):
        """
        mi d(t)
        """
        denumerator = max(self.terms_quantity.values())
        for term in self.terms_quantity:
            self.terms_membership[term] = (self.terms_quantity[term]
                                           / denumerator)

    def calculate_membership_to_categories(self):
        """
            :param categories: list of Categories
            :type categories: list
            sim(d, cj)
        """
        if not self.terms_membership:
            self.calculate_terms_membership()

        terms_revelance = load_objects('db')
        for category in self.categories:
            self.categories_membership[category] = jaccard(
                self.terms_membership,
                terms_revelance[category.identifier],
                algebraic_product,
                algebraic_sum,
            )

    def compare(self, document):
        if not self.categories_membership:
            self.calculate_membership_to_categories()

        if not document.categories_membership:
            document.calculate_membership_to_categories()

        changed_membership = copy(self.categories_membership)
        categories_by_membership = sorted(
            self.categories_membership.iteritems(),
            key=itemgetter(1),
            reverse=True
        )
        maximal = categories_by_membership[0][1]

        for key in changed_membership:
            changed_membership[key] /= maximal

        importance = len(filter(lambda x: x > .5, changed_membership.values()))
        important_categories = categories_by_membership[:importance]

        return jaccard(
            dict(important_categories),
            document.categories_membership,
            min,
            max,
        )

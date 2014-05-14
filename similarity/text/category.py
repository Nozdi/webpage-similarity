"""
.. module:: document
    :synopsis: This module provides categories for documents
"""
from __future__ import division
from collections import defaultdict


class Category(object):
    """
        Category of text

        :field belongingTerms: key - term, value - belongness to category [0;1]
        :type belongingTerms: dictionary
        :field identifier: unique identifier of category
        :type identifier: long
        :field trainingDocuments: list of training documents
        :type trainingDocuments: list
    """

    def __init__(self, identifier):
        """
            :param identifier: unique identifier of category
            :type identifier: long
        """
        self.identifier = identifier
        self.trainingDocuments = []
        self.termsQuantity = defaultdict(int)

    def add_document(self, document):
        """
            Used to add training documents to category.

            :param document: training document
            :type document: TrainingDocument
        """
        self.trainingDocuments.append(document)

        for term, value in document.termsQuantity.iteritems():
            self.termsQuantity[term] += value

    def __str__(self):
        return self.identifier


def term_to_cat_relevance(term, category, all_categories):
    """
    mi R(t, cj)
        :param term: term from document
        :type type: str
        :param category: category in which we look for
        :type Category
        :param all_categories: all categories
        :type list
    """
    return (category.termsQuantity[term] /
            sum([cat.termsQuantity[term] for cat in all_categories]))

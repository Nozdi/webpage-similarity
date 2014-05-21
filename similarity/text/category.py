"""
.. module:: document
    :synopsis: This module provides categories for documents
"""
from __future__ import division
from collections import defaultdict


class Category(object):
    """
        Category of text

        :field identifier: unique identifier of category
        :type identifier: long
        :field training_documents: list of training documents
        :type training_documents: list
    """

    def __init__(self, identifier):
        """
            :param identifier: unique identifier of category
            :type identifier: long
        """
        self.identifier = identifier
        self.training_documents = []
        self.terms_quantity = defaultdict(int)

    def add_document(self, document):
        """
            Used to add training documents to category.

            :param document: training document
            :type document: TrainingDocument
        """
        self.training_documents.append(document)

        for term, value in document.terms_quantity.iteritems():
            self.terms_quantity[term] += value

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
    return (category.terms_quantity[term] /
            sum([cat.terms_quantity[term] for cat in all_categories]))

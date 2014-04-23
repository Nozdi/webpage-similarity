"""
.. module:: document
    :synopsis: This module provides categories for documents
"""


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
        self.belongingTerms = {}

    def add_document(self, document):
        """
            Used to add training documents to category.

            :param document: training document
            :type document: TrainingDocument
        """
        self.trainingDocuments.append(document)

        for term in document.termsWithWeights.items():
            self.belongingTerms[term] = 0

    def count_local_terms_weights(self):
        denumerator = self.trainingDocuments.termsWithWeights[
            max(self.trainingDocuments.termsWithWeights)
        ]

        for document in self.trainingDocuments:
            for term in document.termsWithWeights.items():
                self.belongingTerms[term] += (document.termsWithWeights[term]
                                              / denumerator)


class CategoryManager(object):
    """
        Keeps lists of categories and training documents.
        :field categories: list of known categories
        :type categories: list
        :field trainingDocuments: list of training documents
        :type trainingDocuments: list
    """

    def __init__(self, categories, documents):
        """
            :param categories: list of categories
            :type categories: list
            :param documents: list of training documents
            :type documents: list
        """
        self.categories = categories
        self.trainingDocuments = documents

    def calculate_terms_belongness_to_categories(self):
        denumerator = 0

        for category in self.categories:
            category.count_local_terms_weights()

        for trainingDocument in self.trainingDocuments:
            for term, weight in trainingDocument.termsWithWeights.items():
                denumerator += trainingDocument.termsWithWeights[term]

        for category in self.categories:
            for trainingDocument in self.trainingDocuments:
                for term in trainingDocument.termsWithWeights:
                    category.belongingTerms[term] /= denumerator

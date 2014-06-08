__author__ = 'kacper'

class TextComparisonResult(object):

    def __init__(self, similarity_result, important_categories):
        """
            Used for holding data generated during comparison of two text documents.
        """
        self.similarity_result = similarity_result
        self.important_categories = important_categories
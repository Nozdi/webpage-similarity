def algebraic_sum(x, y):
    return x + y - x * y


def algebraic_product(x, y):
    return x * y


class Category(object):
    """
        Category of text

        :field beloningTerms: key - term, value - belongness to category [0;1]
        :type beloningTerms: dictionary
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
        self.beloningTerms = {}

    def add_document(self, document):
        """
            Used to add training documents to category.

            :param document: training document
            :type document: TrainingDocument
        """
        self.trainingDocuments.append(document)

    def count_local_terms_weights(self):
        for document in self.trainingDocuments:
            for term, weight in document.termsWithWeights:
                self.beloningTerms[term] = 0

        for document in self.trainingDocuments:
            for term, weight in document.termsWithWeights:
                self.beloningTerms[term] += document.termsWithWeights.get(term)


class CategoryManager(object):
    """
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
            for term, weight in document.termsWithWeights:
                denumerator += document.termsWithWeights.get(term)

        for category in self.categories:
            for trainingDocument in self.trainingDocuments:
                for term, weight in document.termsWithWeights:
                    category.beloningTerms[term] /= denumerator

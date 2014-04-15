from re import findall
import fuzzy


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

    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """
        self.text = text

        self.terms = []
        self.termsWithWeights = {}
        self.termsBelongness = {}

    def find_terms(self):
        """
            Splits up the document into words (terms).
            Weight of every term is initally set to 0
        """
        self.terms = findall('\w+', self.text.lower())
        self.uniqueTerms = set(self.terms)

        for term in self.terms:
            self.termsWithWeights[term] = 0.0

    def calculate_terms_weights(self):
        sumOfWords = len(self.terms)
        for term in self.terms:
            if term in self.uniqueTerms:
                self.termsWithWeights[term] += 1

        for term in self.termsWithWeights:
            self.termsWithWeights[term] /= sumOfWords

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
    pass


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

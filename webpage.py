class Document(object):
    """
        :field text: content of document
        :type text: string
        :field terms: terms extracted from text
        :type terms: list
        :field termsWithWeights: key - term, value - weight from range: (0,1]
        :type termsWithWeights: dictionary
        :field belongnessToCategories: key - category, value - degree of belongness to category [0;1]
        :type belongnessToCategories: dictionary
    """
    
    def __init__(self, text):
        """
            :param text: content of document
            :type text: string
        """
        self.text = text
        self.terms = []
        self.termsWithWeights = {}
        self.belongnessToCategories = {}
    
    def findTerms(self):
        pass
        
    def calculateTermsWeights(self):
        pass
        
    def calculateBelongnessToCategories(self):
        pass
        
class WebPage(object):
    """
        Represents analized webpage.
        
        :field content: object of Document class
        :type content: Document
        :field url: url to a webpage
        :type url: string
    """
    
    def __init__(self, document, url):
        """
            :param document: object of Document class
            :type document: Document
            :param url: url to a webpage
            :type url: string
        """
        self.url = url
        self.content = document
    
    def getSimilarity(self, webPage):
        pass
        
class Category(object):
    """
        Category of text
        
        :field identifier: unique identifier of category
        :type identifier: long
        :field sth: to be precised
        :type sth: undefinied
    """
    
    def __init__(self, identifier, sth):
        
        """
            :param identifier: unique identifier of category
            :type identifier: long
            :param sth: to be precised
            :type sth: undefinied
        """
        self.identifier = identifier
        self.sth = sth
        

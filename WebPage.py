class Document:
    _text = ""
    _terms = []
    _termsWithWeights = {}
    _belongnessToCategory = {}
    
    def __init__(self, text):
        self._text = text
    
    def findTerms():
        pass
        
    def calculateTermsWeights():
        pass
        
    def calculateBelongnessToCategories():
        pass
        
class WebPage:
    _content = Document
    _url = ""
    
    def __init__(self, url, document):
        self._url = url
        self._content = document
    
    def getSimilarity(webPage):
        pass
        
class Category:
    _id = 0
    #below field for some kind of information kept by class
    _sth = ""
    
    def __init__(self,identifier,sth):
        self._id = identifier
        self._sth = sth
        

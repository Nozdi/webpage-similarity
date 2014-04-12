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

    def get_similarity(self, webPage):
        pass

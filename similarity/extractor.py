from goose import Goose
from goose.crawler import Crawler


class ExtendedCrawler(Crawler):
    def crawl(self, crawl_candidate):
        super(ExtendedCrawler, self).crawl(crawl_candidate)

        parser = self.extractor.parser
        #get nodes
        nodes = parser.getElementsByTag(
            self.article.raw_doc,
            tag='img'
        )
        #get images
        self.article.images = []
        for node in nodes:
            src = parser.getAttribute(node, attr='src')
            self.article.images.append(self.image_extractor.get_image(node, src))

        return self.article


class ExtendedGoose(Goose):
    def crawl(self, crawl_candiate):
        crawler = ExtendedCrawler(self.config)
        article = crawler.crawl(crawl_candiate)
        return article

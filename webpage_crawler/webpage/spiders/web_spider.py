from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import Selector

from webpage.items import Website

from bs4 import BeautifulSoup

import re
from scrapy.http import Request
from goose import Goose


class WebSpider(BaseSpider):
    name = "web_spider"
    # allowed_domains = ["dogs.about.com"]
    # allowed_domains = ["cats.about.com"]
    # allowed_domains = ["animals.about.com"]
    # allowed_domains = ["womenshealth.about.com"]
    # allowed_domains = ["ancienthistory.about.com"]
    # allowed_domains = ["americanhistory.about.com"]
    # allowed_domains = ["sexuality.about.com"]
    # allowed_domains = ["cars.about.com"]
    allowed_domains = ["artandculture.com"]

    start_urls = [
        #"http://dogs.about.com/",
        # "http://cats.about.com/",
        # "http://animals.about.com/",
        # "http://womenshealth.about.com/",
        # "http://ancienthistory.about.com/",
        # "http://americanhistory.about.com/",
        # "http://sexuality.about.com/",
        # "http://cars.about.com",
        "http://www.artandculture.com/",
    ]

    rules = (Rule(SgmlLinkExtractor(), callback='parse', follow=True), )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()

        # We stored already crawled links in this list
        crawledLinks = []

        # Pattern to check proper link
        linkPattern = re.compile(
            """^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+
                ]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?
                \+=&%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&%@!\-\/\(\)]+))?$""")

        for link in links:
            if linkPattern.match(link) and not link in crawledLinks:
                crawledLinks.append(link)
                yield Request(link, self.parse)

        # tu trzeba zmienic po czym ma wyszukiwac na stronie, znaczniki html    
        # paragraphs = hxs.select("//div[@id='articlebody']/p")
        # alltexts = []

        # for par in paragraphs:
        #     soup = BeautifulSoup(par.extract())
        #     text = soup.get_text()
        #     if text.isspace() or not text:
        #         pass
        #     alltexts.append(text)

        g = Goose()
        raw_html = response.body
        article = g.extract(raw_html=raw_html)
        text = article.cleaned_text
        if text.isspace() or not text:
            pass
  
        item = Website()
        # text = ' '.join(alltexts)
        # if text.isspace() or not text:
        #        pass
        item['text'] = text
        item['filename'] = '1.txt'
        yield item

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from webpage.items import Website

from bs4 import BeautifulSoup

import re
from scrapy.http import Request


class WebSpider(Spider):
    name = "web_spider"
    #allowed_domains = ["history1900s.about.com"]
    #allowed_domains = ["boardgames.about.com"]
    #allowed_domains = ["pcsupport.about.com"]
    #allowed_domains = ["ufos.about.com"]
    #allowed_domains = ["architecture.about.com"]
    allowed_domains = ["geography.about.com"]
    start_urls = [
        #"http://history1900s.about.com/",
        #"http://boardgames.about.com/",
        #"http://pcsupport.about.com/",
        #"http://ufos.about.com/",
        #"http://architecture.about.com/",
        "http://geography.about.com/",
    ]

    rules = (Rule(SgmlLinkExtractor(), callback='parse', follow=True), )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select("//a/@href").extract()

        #We stored already crawled links in this list
        crawledLinks = []

        #Pattern to check proper link
        linkPattern = re.compile(
            """^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+
                ]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?
                \+=&%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&%@!\-\/\(\)]+))?$""")

        for link in links:
            if linkPattern.match(link) and not link in crawledLinks:
                crawledLinks.append(link)
                yield Request(link, self.parse)

        # tu trzeba zmienić po czym ma wyszukiwać na stronie, znaczniki html    
        paragraphs = hxs.select("//div[@id='articlebody']/p")
        alltexts = []

        for par in paragraphs:
            soup = BeautifulSoup(par.extract())
            text = soup.get_text()
            if text.isspace() or not text:
                pass
            alltexts.append(text)

        item = Website()
        text = ' '.join(alltexts)
        if text.isspace() or not text:
                pass
        item['text'] = text
        item['filename'] = '1.txt'
        yield item

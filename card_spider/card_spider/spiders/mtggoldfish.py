import scrapy


class MtggoldfishSpider(scrapy.Spider):
    name = 'mtggoldfish'
    allowed_domains = ['www.mtggoldfish.com']
    start_urls = ['http://www.mtggoldfish.com/']

    def parse(self, response):
        pass

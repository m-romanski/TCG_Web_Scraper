import scrapy


class Mtgstocks(scrapy.Spider):
    name = 'mtgstocks'
    allowed_domains = ['www.mtgstocks.com']
    start_urls = ['https://www.mtgstocks.com/sets']

    def parse(self, response):
        set_links = response.xpath('//li/a[contains(@href, "sets")]/@href').getall()

        for link in set_links:
            yield {
                'set_link': link
                
            }
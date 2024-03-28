import scrapy
import pandas as pd


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

class Mtgstocks_cards(scrapy.Spider):
    name = 'mtgstocks_cards'
    allowed_domains = ['www.mtgstocks.com']
    start_urls = ['https://www.mtgstocks.com/sets']

    def parse(self, response):
        set_links = pd.read_csv('../../spiders/links.csv')
        card_list = pd.read_csv(
        card_links = response.xpath('//

        for link in set_links:
            for set_name in                           
            
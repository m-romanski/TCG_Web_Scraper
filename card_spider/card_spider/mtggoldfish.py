import scrapy


class MtggoldfishSpider(scrapy.Spider):
    name = 'mtggoldfish'
    allowed_domains = ['www.mtggoldfish.com']
    start_urls = ['https://www.mtggoldfish.com/price/Dominaria+United/Sheoldred+the+Apocalypse#paper']

    def parse(self, response):
        current_price = response.xpath('//div[@class="price-box-paper"]//div[@class="price-box-price"]/text()').get()
        highest_price = response.xpath('//table[@class="price-card-statistics-table price-card-statistics-table-2"]//tr[3]/td[2]/text()').get()

        yield{
            'current_price': current_price,
            'highest_price': highest_price
        }

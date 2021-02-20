import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    start_urls = ['http://www.gmarket.co.kr/']

    def parse(self, response):
        print(response.text)

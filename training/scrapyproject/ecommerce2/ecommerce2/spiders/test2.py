import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        print(response.text)

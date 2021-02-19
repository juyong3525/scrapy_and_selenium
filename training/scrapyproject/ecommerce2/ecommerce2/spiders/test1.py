import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        pass

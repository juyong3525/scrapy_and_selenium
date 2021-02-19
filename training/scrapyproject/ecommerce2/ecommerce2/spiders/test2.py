import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/', 'http://promotion.gmarket.co.kr/Event/CouponZone.asp']

    def parse(self, response):
        print(response.url)

import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    # __init__ 개념 (프로그램 실행 시 해당 메소드가 실행됨)
    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers/', callback=self.parse_mainpages)
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01', callback=self.parse_subcategories)

    def parse_mainpages(self, response):
        print("parse_mainpages")

    def parse_subcategories(self, response):
        print("parse_subcategories")

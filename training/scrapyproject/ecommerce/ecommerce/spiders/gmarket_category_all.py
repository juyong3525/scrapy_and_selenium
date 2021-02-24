import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    # __init__ 개념 (프로그램 실행 시 해당 메소드가 실행됨)
    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers/', callback=self.parse_mainpages)

    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css(
            'div.gbest-cate ul.by-group li a::attr("href")').getall()
        category_names = response.css(
            'div.gbest-cate ul.by-group li a::text').getall()
        for index, category_link in enumerate(category_links):
            print(
                f'http://corners.gmarket.co.kr{category_link}', category_names[index])

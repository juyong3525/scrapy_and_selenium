import scrapy
from re_ecommerce.items import ReEcommerceItem


class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_best'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list > ul > li > a::text').getall()
        prices = response.css(
            'div.best-list > ul > li > .item_price > .s-price > strong > span > span::text').getall()

        for num, title in enumerate(titles):
            item = ReEcommerceItem()
            item['title'] = title
            item['price'] = prices[num].strip().replace(
                '원', '').replace(',', '')
            yield item

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

        # 1st category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{category_link}', callback=self.parse_items, meta={'maincategory_name': category_names[index]})
        # 2nd category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{category_link}', callback=self.parse_subcategory, meta={'maincategory_name': category_names[index]})

    def parse_subcategory(self, response):
        print("parse_subcategory", response.meta['maincategory_name'])
        subcategory_links = response.css(
            'div.navi.group > ul > li > a::attr(href)').getall()
        subcategory_names = response.css(
            'div.navi.group > ul > li > a::text').getall()
        for index, subcategory_link in enumerate(subcategory_links):
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{subcategory_link}', callback=self.parse_items, meta={'maincategory_name': response.meta['maincategory_name'], 'subcategory_name': subcategory_names[index]})

    def parse_items(self, response):
        print("parse_items", response.meta['maincategory_name'])

        best_items = response.css('div.best-list')
        for index, item in enumerate(best_items[1].css('li')):
            ranking = index + 1
            title = item.css('a.itemname::text').get()
            ori_price = item.css('div.o-price::text').get()
            dis_price = item.css('div.s-price strong span span::text').get()
            discount_percent = item.css('div.s-price em::text').get()

            if ori_price == None:
                ori_price = dis_price
            ori_price = ori_price.replace(',', '').replace('원', '')
            dis_price = dis_price.replace(',', '').replace('원', '')
            if discount_percent == None:
                discount_percent = 0
            else:
                discount_percent = discount_percent.replace('%', '')

            print(ranking, title, ori_price, dis_price, discount_percent)

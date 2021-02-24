# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql


class EcommercePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  passwd='killerqueen3525',  # git에 push 하지 말 것
                                  db='scrapy_ecommerce',
                                  charset='utf8')

        self.cursor = self.db.cursor()

    def create_table(self):
        create_table = """
                        CREATE TABLE IF NOT EXISTS gmarket_best(
                        main_category_name TEXT,
                        sub_category_name TEXT,
                        ranking INT,
                        title TEXT,
                        ori_price INT,
                        dis_price INT,
                        discount_percent INT ,
                        primary_key INT NOT NULL,
                        PRIMARY KEY(primary_key)
                        );
        """
        self.cursor.execute(create_table)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute(
            f"""
                INSERT INTO gmarket_best VALUES (
                    '{item['main_category_name']}',
                    '{item['sub_category_name']}',
                    '{item['ranking']}',
                    '{item['title']}',
                    '{item['ori_price']}',
                    '{item['dis_price']}',
                    '{item['discount_percent']}',
                    '{item['primary_key']}'
                )
            """
        )
        self.db.commit()

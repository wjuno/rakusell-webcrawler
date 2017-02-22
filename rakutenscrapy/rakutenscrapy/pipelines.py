# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import ProductDetailRecord


class RakutenscrapyPipeline(object):
    def process_item(self, item, spider):



        # product = ProductDetailRecord(
        #     p_id = item['p_id'],
        #     merchant=item['merchant'],
        #     product_name=item['product_name'],
        #     product_img= item['product_img'],
        #     product_url= item['product_url'],
        #     brand = item['brand'],
        #     sub_category = item['sub_category'],
        #     main_category = item['main_category'])
        # product.save()

    	product = ProductDetailRecord(
            product_price=item['product_price'],
            product_url=item['product_url'],
            category= item['category'],
            condition= item['condition'],
            avg_rating = item['avg_rating'],
            review = item['review'],
            description = item['description'])
        product_id = product.save()

        return item

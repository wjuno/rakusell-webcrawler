# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from models import ProductDetailRecord




class AmazonPipeline(object):

	def process_item(self, item, spider):
            
            product = ProductDetailRecord(
            title=item['title'],
            category=item['category'],
            availability= item['availability'],
            original_price= item['original_price'],
            sale_price= item['sale_price'],
            product_url= item['product_url'][:-3],
            product_desc= item['product_desc'],
            avg_ratings=item['avg_ratings'])
            product_id = product.save()

            return item

    # def process_item(self, item, spider):
    #     return item


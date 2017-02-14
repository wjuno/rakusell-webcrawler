# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RakutenscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_price = scrapy.Field()
    product_url = scrapy.Field() 
    category = scrapy.Field()
    condition = scrapy.Field()
    avg_rating = scrapy.Field()
    review = scrapy.Field()
    description = scrapy.Field()


    

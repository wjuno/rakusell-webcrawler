# coding: utf-8
# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from rakutenscrapy.items import RakutenscrapyItem

import bs4
import string
from scrapy import Request
from scrapy.selector import HtmlXPathSelector



class RakutenSpider(scrapy.Spider):
    name = 'rakutenDetails'
    allowed_domains = ['http://www.rakuten.com']


    start_urls = []
    

    with open("product-url.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]




    # def start_requests(self):
    #     index = 1
    #     while True:
    #         yield Request(self.start_urls.format(page=index))
    #         index +=1


    def parse(self, response):

        # list of categories
        XPATH_OUTER_DIV = '//*[@id="product-content"]/div[2]/ul/li/a'
        lis = response.xpath(XPATH_OUTER_DIV)
        cat_list = []
        count = 0

        # list of reviews
        XPATH_OUTER_REVIEW = '//*[@id="customer-review-items"]/article/p[@class="dotdotdot"]'
        reviews = response.xpath(XPATH_OUTER_REVIEW)
        review_list = []
        reviews_count = 0


        XPATH_PRODUCT_PRICE ='//*[@id="buy-box"]/span/div[1]/div[1]/span[1]/text()'
        XPATH_CATEGORY = '//*[@id="product-content"]/div[2]/ul//li/a/text()'
        XPATH_AVG_RATING = '//*[@id="customer-review-content"]/div[1]/strong/text()'
        XPATH_CONDITION = '//*[@id="buy-box"]/span/div[3]/div[1]/strong/text()'
        XPATH_REVIEW = '//*[@id="customer-review-items"]/article/p[@class="dotdotdot"]/text()[1]'
        XPATH_DESC = '//*[@id="product-overview"]/div[@itemprop="description"]/text()[1]'



        for li in lis:
            RAW_CATEGORY = li.xpath(XPATH_CATEGORY).extract()[count]
            CATEGORY = ' '.join(''.join(RAW_CATEGORY).encode('utf-8').split()) if RAW_CATEGORY else None
            cat_list.append(CATEGORY)
            count += 1        
        CATEGORY = ' '.join(' >> '.join(cat_list).encode('utf-8').split()) if cat_list else None

        for r in reviews:
            RAW_REVIEW = li.xpath(XPATH_REVIEW).extract()[reviews_count]
            REVIEW = ' '.join(''.join(RAW_REVIEW).encode('utf-8').split()) if RAW_REVIEW else None
            review_list.append(REVIEW)
            reviews_count += 1        
        REVIEW = ' '.join('>>>>'.join(review_list).encode('utf-8').split()) if review_list else 'no reviews yet'

                 

        RAW_PRODUCT_PRICE = response.xpath(XPATH_PRODUCT_PRICE).extract()
        RAW_AVG_RATING = response.xpath(XPATH_AVG_RATING).extract()
        RAW_CONDITION = response.xpath(XPATH_CONDITION).extract()
        RAW_DESC = response.xpath(XPATH_DESC).extract()

        PRODUCT_PRICE = ' '.join(''.join(RAW_PRODUCT_PRICE).encode('utf-8').split()) if RAW_PRODUCT_PRICE else None
        AVG_RATING = ' '.join(''.join(RAW_AVG_RATING).encode('utf-8').split()) if RAW_AVG_RATING else 'no ratings yet'
        CONDITION = ' '.join(''.join(RAW_CONDITION).encode('utf-8').split()) if RAW_CONDITION else None
        DESC = ' '.join(''.join(RAW_DESC).encode('utf-8').split()) if RAW_DESC else None


        PRODUCT_URL = response.url.strip()

        items = RakutenscrapyItem()
        items['product_price'] = PRODUCT_PRICE
        items['product_url'] = PRODUCT_URL
        items['category'] = CATEGORY
        items['condition'] = CONDITION
        items['avg_rating'] = AVG_RATING
        items['review'] = REVIEW
        items['description'] = DESC


        yield items

           

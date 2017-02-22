# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class AmazonProductSpider(scrapy.Spider):
  name = "AmazonDeals"
  allowed_domains = ["amazon.com"]
  start_urls = []
  
  #Use working product URL below
  for url in open("urls.txt"):
    start_urls.append(url)
 
  def parse(self, response):
    items = AmazonItem()
    
    editorial_reviews = response.xpath('//div[@id="productDescription"]//text()').extract()
  
    items['editorial_reviews'] = ''.join(editorial_reviews).strip()
    yield items

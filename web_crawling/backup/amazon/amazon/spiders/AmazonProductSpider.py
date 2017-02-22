# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from amazon.items import AmazonItem
from scrapy.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
   
import bs4
import string
from scrapy import Request
from scrapy.selector import HtmlXPathSelector




class AmazonProductSpider(scrapy.Spider):
  name = "AmazonProductsDetails"
  allowed_domains = ["amazon.com"]
  start_urls = []
  rules=(Rule(SgmlLinkExtractor(allow=("https://amazon.com/",)),  callback='parse_item', follow=True))
  



  def __init__(self):
    
    for line in open('uncomplete.txt', 'r').readlines():
        self.allowed_domains.append(line)
        self.start_urls.append('%s' % line)


  # # Use working product URL below
  # for url in open("urls.txt"):
  #   start_urls.append(url.strip())
 


 
  def parse(self, response):
  

    XPATH_TITLE = '//span[contains(@id,"productTitle") or contains(@id,"title")]//text()'
    # XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
    XPATH_SALE_PRICE = '//span[@id="priceblock_ourprice"]//text()'
    XPATH_ORIGINAL_PRICE = '//span[@id="priceblock_ourprice"]//text()'
    XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
    XPATH_AVAILABILITY = '//div[@id="availability"]//text()'

    
    XPATH_AVG_RATINGS = '//div[@id="averageCustomerReviews"]//span[@class="a-icon-alt"]//text()'
    XPATH_DESC = '//div[@id="productDescription"]//text()'
    XPATH_DESC2 = '//div[@id="productDescription"]/div/div//text()[1]'
    XPATH_DESC3 = '//div[@id="productDescription"]/p//text()[1]'
    XPATH_DESC4 = ''
    RAW_DESC4 =''

    
    RAW_DESC4 = ''
    DESC4 = ''

    i = 2
    while (i < 11):
        XPATH_DESC4 = '//div[@id="feature-bullets"]/ul/li['+ str(i) +']//text()'
        RAW_DESC4 = response.xpath(XPATH_DESC4).extract()
        TEMP = str(''.join(RAW_DESC4).encode('utf-8').strip() if RAW_DESC4 else None) 
        if TEMP == 'None':
            break
        DESC4 += str(''.join(RAW_DESC4).encode('utf-8').strip() if RAW_DESC4 else None) 
        DESC4 += str(',')
        i += 1

    RAW_TITLE = response.xpath(XPATH_TITLE).extract()
    RAW_SALE_PRICE = response.xpath(XPATH_SALE_PRICE).extract()
    RAW_CATEGORY = response.xpath(XPATH_CATEGORY).extract()
    RAW_ORIGINAL_PRICE = response.xpath(XPATH_ORIGINAL_PRICE).extract()
    RAW_AVAILABILITY = response.xpath(XPATH_AVAILABILITY).extract()

    RAW_DESC = response.xpath(XPATH_DESC).extract()
    RAW_DESC2 = response.xpath(XPATH_DESC2).extract()
    RAW_DESC3 = response.xpath(XPATH_DESC3).extract()
    RAW_AVG_RATINGS = response.xpath(XPATH_AVG_RATINGS).extract()

    TITLE = ' '.join(''.join(RAW_TITLE).encode('utf-8').split()) if RAW_TITLE else None
    SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).encode('utf-8').split()).strip() if RAW_SALE_PRICE else None
    CATEGORY = ' > '.join([i.encode('utf-8').strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
    ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).encode('utf-8').strip() if RAW_ORIGINAL_PRICE else None
    AVAILABILITY = ''.join(RAW_AVAILABILITY).encode('utf-8').strip() if RAW_AVAILABILITY else None
    DESC = ''.join(RAW_DESC).encode('utf-8').strip() if RAW_DESC else None
    DESC2 = ''.join(RAW_DESC2).encode('utf-8').strip() if RAW_DESC2 else None
    DESC3 = ''.join(RAW_DESC3).encode('utf-8').strip() if RAW_DESC3 else None
    # DESC4 = ''.join(RAW_DESC4).strip() if RAW_DESC4 else None
    AVG_RATINGS = ''.join(RAW_AVG_RATINGS).encode('utf-8').strip() if RAW_AVG_RATINGS else "There are no customer reviews yet."


    if not ORIGINAL_PRICE:
        ORIGINAL_PRICE = SALE_PRICE

    DESC_ARR = [DESC,DESC2,DESC3,DESC4]
    # print('Total String is ====> ' + str(DESC_ARR))
    if DESC_ARR:
        DESC = ' || '.join(filter(None,DESC_ARR))
    

    if all(x is None for x in DESC_ARR) :
        DESC = 'no description'
        
    # print('Total String is ====> ' + DESC)

    # print TITLE
    
    URL = response.url.strip()

    if not TITLE and not CATEGORY and not AVAILABILITY and not ORIGINAL_PRICE and not SALE_PRICE and DESC == '':
        print("====================== APPENDING FAIL URL =========================")
        errorURL=[]
        with open("errorURL.txt", "a") as myfile:
            myfile.write(URL+'\n')





    



    items = AmazonItem()
    items['title'] = TITLE
    items['category'] = CATEGORY
    items['availability'] = AVAILABILITY
    items['original_price'] = ORIGINAL_PRICE
    items['sale_price'] = SALE_PRICE
    items['product_url'] = URL
    items['product_desc'] = DESC
    items['avg_ratings'] = AVG_RATINGS
      
    return items











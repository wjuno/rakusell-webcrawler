# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from amazonlah.items import AmazonItem
    
import bs4
from scrapy import Request
import string


  

class AmazonProductSpider(scrapy.Spider):
  name = "AmazonProducts"
  allowed_domains = ["amazon.com"]
  start_urls = []



  def __init__(self):
        for line in open('urls.txt', 'r').readlines():
            self.allowed_domains.append(line)
            self.start_urls.append('%s' % line)

  # # Use working product URL below
  # for url in open("urls.txt"):
  #   start_urls.append(url.strip())
 


 
  def parse(self, response):
    count = 1
    count += 1
    print("######################## Count ###################### " + str(count))
    #TODO AVG_RATING 
    XPATH_TITLE = '//h1[@id="title"]//text()'
    # XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
    # XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
    # XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
    # XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
    # XPATH_DESC = '//div[@id="productDescription"]//text()'
    # XPATH_DESC2 = '//div[@id="productDescription"]/div/div//text()[1]'
    # XPATH_DESC3 = '//div[@id="productDescription"]/p//text()[1]'
    # XPATH_DESC4 = ''
    # RAW_DESC4 =''

    
    # RAW_DESC4 = ''
    # DESC4 = ''

    # i = 2
    # while (i < 11):
    #     XPATH_DESC4 = '//div[@id="feature-bullets"]/ul/li['+ str(i) +']//text()'
    #     RAW_DESC4 = response.xpath(XPATH_DESC4).extract() 
    #     TEMP = str(''.join(RAW_DESC4).strip() if RAW_DESC4 else None) 
    #     if TEMP == 'None':
    #         break
    #     DESC4 += str(''.join(RAW_DESC4).strip() if RAW_DESC4 else None) 
    #     DESC4 += str(',')
    #     i += 1
        



    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # XPATH_AVG_RATINGS = '//span[@class="arp-rating-out-of-text"]/text()[1]'


    RAW_TITLE = response.xpath(XPATH_TITLE).extract()
    # RAW_SALE_PRICE = response.xpath(XPATH_SALE_PRICE).extract()
    # RAW_CATEGORY = response.xpath(XPATH_CATEGORY).extract()
    # RAW_ORIGINAL_PRICE = response.xpath(XPATH_ORIGINAL_PRICE).extract()
    # RAW_AVAILABILITY = response.xpath(XPATH_AVAILABILITY).extract()
    # RAW_DESC = response.xpath(XPATH_DESC).extract()
    # RAW_DESC2 = response.xpath(XPATH_DESC2).extract()
    # RAW_DESC3 = response.xpath(XPATH_DESC3).extract()
    # # RAW_DESC4 = response.xpath(XPATH_DESC4).extract()
    # RAW_AVG_RATINGS = response.xpath(XPATH_AVG_RATINGS).extract()


    TITLE = ' '.join(''.join(RAW_TITLE).split()) if RAW_TITLE else None
    # SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
    # CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
    # ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
    # AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
    # DESC = ''.join(RAW_DESC).strip() if RAW_DESC else None
    # DESC2 = ''.join(RAW_DESC2).strip() if RAW_DESC2 else None
    # DESC3 = ''.join(RAW_DESC3).strip() if RAW_DESC3 else None
    # # DESC4 = ''.join(RAW_DESC4).strip() if RAW_DESC4 else None
    # AVG_RATINGS = ''.join(RAW_AVG_RATINGS).strip() if RAW_AVG_RATINGS else None

    
    print("TITLE : " + str(TITLE) )
    # print("SALE_PRICE : " + str(SALE_PRICE) )
    # print("CATEGORY : " + str(CATEGORY) )
    # print("AVAILABILITY : " + str(AVAILABILITY) )
    # print("ORIGINAL_PRICE : " + str(ORIGINAL_PRICE) )

    # if not ORIGINAL_PRICE:
    #   ORIGINAL_PRICE = SALE_PRICE


    # if not AVG_RATINGS:
    #   AVG_RATINGS = "There are no customer reviews yet."



    # DESC_ARR = [DESC,DESC2,DESC3,DESC4]
    # print('Total String is ====> ' + str(DESC_ARR))
    # if DESC_ARR:
    #     DESC = ' || '.join(filter(None,DESC_ARR))
    

    # if all(x is None for x in DESC_ARR) :
    #     DESC = 'no description'
        
    # print('Total String is ====> ' + DESC)

    # # title = response.xpath('//h1[@id="title"]/span/text()').extract()
    # if(response.xpath('//div[@id="productDescription"]//text()').extract()):
    #   product_desc = response.xpath('//div[@id="productDescription"]//text()').extract()

    # if(response.xpath('//div[@id="productDescription"]/div/div/text()[1]').extract()):
    #   product_desc = response.xpath('//div[@id="productDescription"]/div/div/text()[1]').extract()


    
    # if product_desc == "Product Description":
    #   product_desc = "nill"
    #   print('pass!')

   
    # avg_ratings = "test"
    # price = "test"
    URL = response.url.strip()

    



    items = AmazonItem()
    items['title'] = TITLE
    # items['category'] = CATEGORY
    # items['availability'] = AVAILABILITY
    # items['original_price'] = ORIGINAL_PRICE
    # items['sale_price'] = SALE_PRICE
    items['product_url'] = URL
    # items['product_desc'] = DESC
    # items['avg_ratings'] = AVG_RATINGS
      
    return items











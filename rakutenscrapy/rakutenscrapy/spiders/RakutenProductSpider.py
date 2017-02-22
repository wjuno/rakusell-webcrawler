# coding: utf-8
# -*- coding: utf-8 -*-
import scrapy
import urllib2  
from rakutenscrapy.items import RakutenscrapyItem

import bs4
import string
from scrapy import Request
from scrapy.selector import HtmlXPathSelector
from random import randint



class RakutenSpider(scrapy.Spider):
    name = 'rakuten'
    allowed_domains = ['http://www.rakuten.com']

    #```````````````````````````` CELL PHONE ```````````````````````````#
    # Apple - http://www.rakuten.com/loc/apple-cell-phones/85207.html?page={page}
    # Samsung - http://www.rakuten.com/loc/Samsung-Phones/87100.html?page={page}
    # HTC - http://www.rakuten.com/loc/HTC-Phones/87101.html?page={page}
    # LG - http://www.rakuten.com/loc/LG-Phones/87102.html
    # Motorola - http://www.rakuten.com/loc/Motorola-Phones/87103.html
    # Nokia - http://www.rakuten.com/loc/Nokia-Phones/87104.html
    # Sony - http://www.rakuten.com/loc/Sony-Phones/87105.html

     ######### Cell Phone Accessories ###########
     # Charger - http://www.rakuten.com/loc/chargers-cell-phone/85220.html?page={page}
     # CELL PHONE BATTERIES & ADAPTERS - http://www.rakuten.com/loc/Cell-Phone-Batteries-Adapters/85221.html?page={page}
     # Car Cradle Mounts - http://www.rakuten.com/loc/Car-Cradle-Mounts-cell-phone/85223.html?page={page}
     # BLUETOOTH CAR KITS/TUNERS - http://www.rakuten.com/loc/Bluetooth-Car-Kits-Tuners/85224.html?page={page}
     # CAR CHARGERS - http://www.rakuten.com/loc/Car-Chargers-cell-phones/85225.html?page={page}


     ############ HEADSETS #################
     # BlueTooth- http://www.rakuten.com/loc/Headsets-cell-phones/85226.html

     ############ Cases & Covers ##############
     # Hard Cases - http://www.rakuten.com/loc/Hard-Case-cell-phones/85229.html?page={page}
     # Soft Cases - http://www.rakuten.com/loc/Soft-Cases-cell-phones/85230.html?page={page}
     # PROTECTIVE CASES - http://www.rakuten.com/loc/Protective-Cases-cell-phones/85231.html?page={page}
     # Screen protector - http://www.rakuten.com/loc/Screen-Protector-cell-phone/85222.html?page={page}

     ############### Refurbished Preowned Cell Phones ################
     # Android - http://www.rakuten.com/loc/Android-refurbished-preowned-cell-phones/85235.html
     # Apple - http://www.rakuten.com/loc/Apple-refurbished-preowned-cell-phones/85236.html?page={page}



     #```````````````````````````` Cameras & Camcorders ```````````````````````````#
     # DSLR Cameras > Professional DSLR CAMERAS - http://www.rakuten.com/loc/Professional-DSLR-Camera/85291.html?page={page}
     # DSLR Camera > BODY & LENS KITS - http://www.rakuten.com/loc/Body-Lens-Kits/85292.html?page={page}

    start_urls = 'http://www.rakuten.com/loc/bluetooth-headphones/85310.html?page={page}'
  
    def start_requests(self):
        index = 1
        while True:
            yield Request(self.start_urls.format(page=index))
            index +=1


    def parse(self, response):

        XPATH_OUTER_DIV = '//div[@class="FabContainer product-lister"]'
        divs = response.xpath(XPATH_OUTER_DIV)
        
        # RMB TO CHANGE !!!!!!!!!!!!!!!!!!!!!!!
        brand = ''
        sub_category = 'Bluetooth Headphones'
        main_category = 'Headphones'


        XPATH_MERCHANT = '//div[@class="FabContainer product-lister"]//div[@class="merchant_name"]//text()'
        XPATH_PRODUCT_NAME ='//div[@class="FabContainer product-lister"]//div[@class="product_name"]//text()'
        XPATH_IMG = '//div[@class="FabContainer product-lister"]//div[@class="pl-image-box"]/img/@src'
        XPATH_PRODUCT_URL = '//div[@class="FabContainer product-lister"]/a/@href'


        count = 0
        for div in divs:

         
            RAW_MERCHANT = div.xpath(XPATH_MERCHANT).extract()[count]
            RAW_PRODUCT_NAME = div.xpath(XPATH_PRODUCT_NAME).extract()[count]
            RAW_PRODUCT_IMG = div.xpath(XPATH_IMG).extract()[count]
            RAW_PRODUCT_URL = div.xpath(XPATH_PRODUCT_URL).extract()[count]


            MERCHANT = ' '.join(''.join(RAW_MERCHANT).encode('utf-8').split()) if RAW_MERCHANT else None
            PRODUCT_NAME = ' '.join(''.join(RAW_PRODUCT_NAME).encode('utf-8').split()) if RAW_PRODUCT_NAME else None
            PRODUCT_IMG = ' '.join(''.join(RAW_PRODUCT_IMG).encode('utf-8').split()) if RAW_PRODUCT_IMG else None
            PRODUCT_URL = ' '.join(''.join(RAW_PRODUCT_URL).encode('utf-8').split()) if RAW_PRODUCT_URL else None

            # p_url = PRODUCT_URL
            # p_url = p_url.split('.html')
            # p_url = p_url[0].split('/')

            # p_id = p_url[-1]



            items = RakutenscrapyItem()
            items['p_id'] = randint(11099,1000000)
            items['merchant'] = MERCHANT
            items['product_name'] = PRODUCT_NAME
            items['product_img'] = PRODUCT_IMG
            items['product_url'] = PRODUCT_URL
            items['brand'] = brand
            items['sub_category'] = sub_category
            items['main_category'] = main_category

            count += 1
            yield items

           

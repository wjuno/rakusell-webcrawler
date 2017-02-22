from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError
from time import sleep
from models import ProductDetailRecord
import time
start_time = time.time()

# title = response.xpath('//h1[@id="title"]/span/text()').extract()

    


def AmzonParser(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'}
    page = requests.get(url,headers=headers)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            # TODO //h1[@id="title"]/span//text()
            # id="productTitle"
            #XPATH_TITLE = '//h1[@id="title"]/span//text()'
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
                RAW_DESC4 = doc.xpath(XPATH_DESC4)
                TEMP = str(''.join(RAW_DESC4).encode('utf-8').strip() if RAW_DESC4 else None) 
                if TEMP == 'None':
                    break
                DESC4 += str(''.join(RAW_DESC4).encode('utf-8').strip() if RAW_DESC4 else None) 
                DESC4 += str(',')
                i += 1
 
            RAW_TITLE = doc.xpath(XPATH_TITLE)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAW_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)

            RAW_DESC = doc.xpath(XPATH_DESC)
            RAW_DESC2 = doc.xpath(XPATH_DESC2)
            RAW_DESC3 = doc.xpath(XPATH_DESC3)
            RAW_AVG_RATINGS = doc.xpath(XPATH_AVG_RATINGS)
 
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

            print TITLE

            if page.status_code!=200:
                raise ValueError('captha')
                return None
            data = {
                    'TITLE':TITLE,
                    'SALE_PRICE':SALE_PRICE,
                    'CATEGORY':CATEGORY,
                    'ORIGINAL_PRICE':ORIGINAL_PRICE,
                    'AVAILABILITY':AVAILABILITY,
                    'URL':url,
                    'DESC':DESC,
                    'AVG_RATINGS':AVG_RATINGS,
                    }
 
            return data
        except Exception as e:
            print e
            extracted_data = []
            data = {
                    'URL':url,
                    }
            extracted_data.append(data)
            f=open('errorUrl.json','a')
            json.dump(extracted_data,f,indent=4)
            return None
 
def ReadAsin():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))

    AsinList = []

    for url in open("uncomplete.txt"):
        AsinList.append(url.strip())

    extracted_data = []
    size = len(AsinList)
    count = 0
    for i in AsinList:
        url = "https://www.amazon.com/"+i
        # print "Processing: "+url
        count += 1
        if i:
            print("================["+str(count) + " of " + str(size)+"]===================")
            item = AmzonParser(url)
            if item:
                product = ProductDetailRecord(
                title= item['TITLE'],
                category= item['CATEGORY'],
                availability= item['AVAILABILITY'],
                original_price= item['ORIGINAL_PRICE'],
                sale_price= item['SALE_PRICE'],
                product_url= item['URL'],
                product_desc= item['DESC'],
                avg_ratings= item['AVG_RATINGS'])
                product_id = product.save()

            
        sleep(5)
    
    # print("TITLE =================> " + item['TITLE'])
    # print("SALE_PRICE =================> " + item['SALE_PRICE'])
    # print("CATEGORY =================> " + item['CATEGORY'])
    # print("ORIGINAL_PRICE =================> " + item['ORIGINAL_PRICE'])
    # print("AVAILABILITY =================> " + item['AVAILABILITY'])
    # print("URL =================> " + item['URL'])
    # print("DESC =================> " + item['DESC'])
    # print("AVG_RATINGS =================> " + item['AVG_RATINGS'])


    # f=open('data.json','w')
    # json.dump(extracted_data,f,indent=4)
 
if __name__ == "__main__":
    ReadAsin()
    print("--- %s seconds ---" % (time.time() - start_time))
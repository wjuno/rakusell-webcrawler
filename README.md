# Crawl the Rakuten Electronic Products and Details (Scrapy) 

* **Cell Phones Categories**
	* Unlocked Cell Phones
	* Cell Phone Accessories
	* Headsets
	* Cases & Cover
	* Refurbished & Preowned Cell Phones
	* Phone & Phone Systems

* **Cameras & Camcorders Categories**
	* DSLR Cameras


* **Go to the rakutenscrapy/rakutenscrapy/spiders folder**
	* Issue this command will use Scrapy to crawl : 
		* scrapy crawl rakuten -o itemsDesc.json
			* this will also generate itemsDesc.json
		* scrapy crawl rakuten 
			* will not generate itemDesc.json
		* products_details table in postgres will be populated with the crawled data and also generate 
		the itemDesc.json file.
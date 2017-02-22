import psycopg2

import settings

conn = psycopg2.connect(database=settings.database,password=settings.password,host=settings.host,user=settings.user)
cur = conn.cursor()



class ProductDetailRecord(object):
    """docstring for ProductRecord""" 
    def __init__(self,p_id, merchant, product_name, product_img,product_url,brand,sub_category,main_category):
        super(ProductDetailRecord, self).__init__()
        self.p_id = p_id
        self.merchant = merchant
        self.product_name = product_name
        self.product_img = product_img
        self.product_url = product_url
        self.brand = brand
        self.sub_category = sub_category
        self.main_category = main_category

    def save(self):
        cur.execute("INSERT INTO products (id , merchant, product_name, product_img, product_url, brand, sub_category, main_category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
            self.p_id,
            self.merchant,
            self.product_name,
            self.product_img,
            self.product_url,
            self.brand,
            self.sub_category,
            self.main_category,
        ))

        # cur.execute("UPDATE electronic_products SET brand=%s WHERE product_url=%s RETURNING id", (
        #     self.product_url,
        #     self.brand,
        # ))
        conn.commit()
        return cur.fetchone()[0]





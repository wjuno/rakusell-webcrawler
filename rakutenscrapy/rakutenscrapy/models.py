import psycopg2

import settings

conn = psycopg2.connect(database=settings.database,password=settings.password,host=settings.host,user=settings.user)
cur = conn.cursor()



class ProductDetailRecord(object):
    """docstring for ProductRecord""" 
    def __init__(self, product_price, product_url, category,condition,avg_rating,review,description):
        super(ProductDetailRecord, self).__init__()
        self.product_price = product_price
        self.product_url = product_url
        self.category = category
        self.condition = condition
        self.avg_rating = avg_rating
        self.review = review
        self.description = description

    def save(self):
        cur.execute("INSERT INTO electronic_products_details (product_price, product_url, category, condition, avg_rating, review, description) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id", (
            self.product_price,
            self.product_url,
            self.category,
            self.condition,
            self.avg_rating,
            self.review,
            self.description,
        ))
        # cur.execute("UPDATE electronic_products SET brand=%s WHERE product_url=%s RETURNING id", (
        #     self.product_url,
        #     self.brand,
        # ))
        conn.commit()
        return cur.fetchone()[0]


if __name__ == '__main__':

    # setup tables
    cur.execute("DROP TABLE IF EXISTS electronic_products_details")
    cur.execute("""CREATE TABLE electronic_products_details (
        id          serial PRIMARY KEY,
        product_price       text,
        product_url    text,
        category text,
        condition text,
        avg_rating text,
        review text,
        description text
    );""")
    conn.commit()



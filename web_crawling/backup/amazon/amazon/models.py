import psycopg2

import settings

conn = psycopg2.connect(database=settings.database,password=settings.password,host=settings.host,user=settings.user)
cur = conn.cursor()


class ProductDetailRecord(object):
    """docstring for ProductRecord""" 
    def __init__(self, title, category, availability,original_price,sale_price,product_url,product_desc,avg_ratings):
        super(ProductDetailRecord, self).__init__()
        self.title = title
        self.category = category
        self.availability = availability
        self.original_price = original_price
        self.sale_price = sale_price
        self.product_url = product_url
        self.product_desc = product_desc
        self.avg_ratings = avg_ratings

    def save(self):
        # cur.execute("INSERT INTO products_details (title, category, availability,original_price,sale_price,product_url,product_desc,avg_ratings) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", (
        #     self.title,
        #     self.category,
        #     self.availability,
        #     self.original_price,
        #     self.sale_price,
        #     self.product_url,
        #     self.product_desc,
        #     self.avg_ratings,
        # ))
        cur.execute("UPDATE products_details SET title=%s, category=%s, availability=%s, original_price=%s ,sale_price=%s ,product_desc=%s ,avg_ratings=%s WHERE product_url=%s RETURNING id", (
            self.title,
            self.category,
            self.availability,
            self.original_price,
            self.sale_price,
            self.product_desc,
            self.avg_ratings,
            self.product_url,
        ))
        conn.commit()
        return cur.fetchone()[0]


if __name__ == '__main__':

    # setup tables
    cur.execute("DROP TABLE IF EXISTS products_details")
    cur.execute("""CREATE TABLE products_details (
        id          serial PRIMARY KEY,
        title       varchar(2056),
        category    varchar(2056),
        availability varchar(2056),
        original_price varchar(128),
        sale_price varchar(128),
        product_url varchar(2056),
        product_desc text,
        avg_ratings varchar(128)
    );""")
    conn.commit()



import mysql.connector
from datetime import date

class SaletrackerProductManager:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to the database.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def insert_product(self, product_dict):
        try:
            cursor = self.connection.cursor()

            # Check if identical record exists for today's date
            today_date = date.today()
            query = ("SELECT * FROM product WHERE "
                     "product_url = %(url)s AND "
                     "DATE(created_at) = DATE(%(created_at)s)"
                    )
            
            product_dict['created_at'] = today_date
            cursor.execute(query, product_dict)
            existing_product = cursor.fetchone()

            if not existing_product:
                # Insert if the identical record for today's date doesn't exist
                insert_query = ("INSERT INTO product "
                                "(product_name, product_url, product_image, product_price, shop_id, product_type_id, created_at) "
                                "VALUES (%(name)s, %(url)s, %(image)s, %(price)s, %(shop_id)s, %(product_type_id)s, %(created_at)s)")
                cursor.execute(insert_query, product_dict)
                self.connection.commit()
                print("Product inserted successfully.")
            else:
                print("Identical record for today's date already exists. Not inserted.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            cursor.close()


saletracker_db  = SaletrackerProductManager('localhost', 'root', '', 'saletracker') 

product_dict = {
    "name":"test",
    "url":"https://www.incredible.co.za/samsung-98-inch-qled-4k-98q80c-freestyle",
    "image":'test',
    "price":'test',
    "shop_id":8,
    "product_type_id":None
}    

saletracker_db.insert_product(product_dict) 
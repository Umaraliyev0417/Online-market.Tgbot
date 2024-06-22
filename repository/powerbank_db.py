import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

class Postgres_powerbank:

    def __init__(self):
        self.data_base = psycopg2.connect(
                        host=os.getenv("HOST"),
                        user=os.getenv("USER"),
                        database=os.getenv("DATABASE"),
                        password=os.getenv("PASSWORD")
                        )
        # Data base ga ulanish
        self.cursor = self.data_base.cursor()

    def create_table(self):
        """Create table"""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS powerbank (
                product_id SERIAL PRIMARY KEY,
                brand_name VARCHAR(255),
                product_image VARCHAR(255),
                product_price VARCHAR(255),
                configurations TEXT UNIQUE,
                product_url VARCHAR(255)
            )
        """)

    def insert_into(self, *args):
        self.create_table()
        """Insert data"""
        self.cursor.execute(f"""
            INSERT INTO powerbank (brand_name, product_image, product_price, configurations, product_url) 
            VALUES 
            (%s, %s, %s, %s, %s) ON CONFLICT(configurations) DO NOTHING
        """, args)
        return self.data_base.commit()

    def select_data(self):
        """select data"""
        self.cursor.execute("""
            SELECT *
            FROM powerbank
        """)
        return self.cursor.fetchall()




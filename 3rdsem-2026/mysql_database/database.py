import pymysql

class Database:
    def __init__(self, host, port, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def insert(self, query, params):
        try:
            # query = "INSERT INTO orders (item_name, item_price, item_quantity) VALUES (%s, %s, %s)"
            # params = (item.name, item.price, item.quantity)
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def update(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()
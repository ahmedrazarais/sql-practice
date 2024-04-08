# write a query to make database name inventory in which make table store 
# containg three columns product id (integer) , productname=string  , quantity = Float



# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Creation:
    def __init__(self):
        try:
            # MAKING A CONNECTION WITH MYSQL
            self.connection=mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD
               
            )
            # MAKE A POINTER FOR EXECUTING QUERY
            self.cursor=self.connection.cursor()
            
            

            print("Connection created successfull")
        # IF CONNECTION NOT MADE SUCCESSFULLY
        except mysql.connector.Error as e:
            print(f"Error in connection {e}")
    

    # making a mehtod to make update
    def Creating_database(self):
        try:
            database='inventory'
            query=f"CREATE DATABASE IF NOT EXISTS {database}"
            self.cursor.execute(query)
            self.connection.commit()
            print("Database created successfullyy..")
            return database
        except mysql.connector.Error as e:
            print(f"Error in deletion {e}")
    
    def creating_table(self):
        database=self.Creating_database()
        if database:
            self.cursor.execute(f"USE {database}")
            # MAKING TABLE IN THAT DATABASE
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS store (
                                product_id INT NOT NULL,
                                product_name VARCHAR (20),
                                quantity FLOAT )""")
            self.connection.commit()
            print("Table created successfully")
    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")

# MAKING INSTANCE OF CLASS

execution=Creation()
execution.creating_table()
execution.close_connection()
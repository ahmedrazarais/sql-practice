# Question:

# Write a Python script that interacts with a MySQL database to perform the following operations:

# Connect to a MySQL database using credentials provided in a config.py file.
# Create a new table named 'products' with the following columns:
# ID (integer, primary key)
# Name (varchar)
# Price (decimal)
# Insert three sample records into the 'products' table.
# Retrieve and print the list of all products from the 'products' table.
# Ensure to handle any potential errors gracefully and securely.
# Close the database connection after completing the operations.




# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Products:
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

    # MEHTOD TO CLOSE CONNECTION
    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")


    # MEHTOD TO CREATE DATABASE
    def create_database(self):
        try:
            query="CREATE DATABASE IF NOT EXISTS store"
            self.cursor.execute(query)
            print("Database Created Successfully.")
            return "store"
        except mysql.connector.Error as e:
            print(f"Error in database creation {e}")

    # MEHTOD TO CREATE TABLE IN DATABASE
    def create_table(self):
        # USING THE DATABASE THAT WE CREATED 
        dataset=self.create_database()
        if dataset:
            try:
               self.cursor.execute(f"USE {dataset} ")
               # MAKE TABLE IN THAT DATABASE
               query="""CREATE TABLE IF NOT EXISTS products(
               ID INT PRIMARY KEY,
               NAME VARCHAR (20),
               PRICE FLOAT
               )"""
               self.cursor.execute(query)
               print("Table created successfully")
               
            
            except mysql.connector.Error as e:
                print(f"Getting error in table creation {e}")
    
    # INSERT SAMPLE DATA IN TABLE
    def insert_data(self,data):
        try:
            query="INSERT INTO products (ID,NAME,PRICE) VALUES(%s,%s,%s)"
            self.cursor.executemany(query,data)
            print("Data added successfully")
        
        except mysql.connector.Error as e:
           print(f"Getting error in inserting data {e}")
    

        




    # MEHTOD TO RETRIEVE LIST FROM TABLE 
    def get_product_list(self):
        try:
            query="SELECT * FROM products"
            self.cursor.execute(query)
            data=self.cursor.fetchall()
            return data
        except mysql.connector.Error as e :
            print(f"GEetting error in retreiving list {e}")
            return []

    # MEHTOD TO PRINT DATA
    def display_data(self):
        data=self.get_product_list()
        if data:
            print("ID\t\tNAMES\t\tPRICE\n")
            for id,name,price in data:
                print(f"{id}\t{name}\t{price}")

# MAKING INSTANCE OF CLASS
sample_data=[(1,"chips",11.2),(2,"lays",19)]
product=Products()
# product.create_table()
# product.insert_data(sample_data)
# product.get_product_list()
# product.display_data()
product.close_connection()
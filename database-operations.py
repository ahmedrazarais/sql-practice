# Create a Python script that connects to a MySQL database and performs the following operations:

# Delete the entire table named 'customers'.
# Delete only the contents (rows) of the table named 'orders' where id=123.
# Update the 'status' column of the 'orders' table for the row where id=456, setting it to 'completed'.
# Make sure to handle any potential errors gracefully and securely. After completing the operations, close the database connection.


# Create a Python script that connects to a MySQL database and performs the following operations:

# Delete the entire table named 'customers'.
# Delete only the contents (rows) of the table named 'orders' where id=123.
# Make sure to handle any potential errors gracefully and securely. After completing the operations, close the database connection.




# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Analysis:
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
    
    
    # WRITTING QUERY FOR DELETING ENTIRE TABLE
    def write_query_for_deleting_table(self):
        try:
            query="DROP TABLE IF EXISTS customers"
            self.cursor.execute(query)
            self.connection.commit()
            print("Entire Table deleted From database")
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    

    # WRITTING QUERY FOR DELETING CONTENTS OF TABLE
    def write_query_for_deleting_table_row(self):
        try:
            source_id=("123",)
            query="DELETE FROM orders WHERE id=%s"
            self.cursor.execute(query,source_id)
            self.connection.commit()
            print("Table contents deleted From database")
        except mysql.connector.Error as e:
            print(f"Error:{e}")


    # MAKE A MEHTOD TO UPDATE IN COLUMN status
    def update(self, order_id, new_status):
        try:
            query="UPDATE orders SET status=%s WHERE id =%s"
            self.cursor.execute(query,(order_id,new_status))
            self.connection.commit()
            print("Update done successfully..\n")
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    


    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")


analysis = Analysis()

analysis.close_connection()
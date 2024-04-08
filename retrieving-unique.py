# Retrieve only the unique values from a column name professions in a table




# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Getting_unique:
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
    def get_unique_values(self):
        try:
            # Assuming the table name is 'employees' and  to retrieve unique values from the 'column_name' column
            column_name = 'professions'  # ASSUMING COLUMN NAME IS professions
            query = f"SELECT DISTINCT {column_name} FROM employees"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            print(rows)
        except mysql.connector.Error as e:
            print(f"Error in execution: {e}")
        
    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")



    

# MAKE INSTANCE OF CLASS
executor=Getting_unique()
# CALL HERE MEHTOD
executor.close_connection()
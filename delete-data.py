# Assume database  in which table name contents in table two columns name and subject
# sample data:
# name     subject
# raza     Maths
# ahmed    science
# ali      english
# jack     commerce

# write a query to delete that row from table where name is ahmed 

# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Deletion:
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
    def delete_process(self):
        try:
            source_name="ahmed"
            # ASSUMING THAT IN DATABASE contents TABLE ALREADY EXISTS
            query="DELETE FROM contents WHERE name=%s"
            self.cursor.execute(query,source_name)
            print("Row deleted successfully")

        except mysql.connector.Error as e:
            print(f"Error in deletion {e}")
        
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
executor=Deletion()
executor.close_connection()
# NOW CALL MEHTOD WHAT NEEDED








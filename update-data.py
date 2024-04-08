# Assume database name peoples in which table name details in tab;le two columns name and occupation
# sample data:
# name     occupation
# raza     CEO
# ahmed    Programmer
# ali      Scientist
# jack     Agent

# write a query to update occupation of person name ali to CA

# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Updation:
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
    def update_process(self):
        try:
            update_occuppation="CA"
            name="ali"
            # ASSUMING IN DATABSE DETAILS NAME TABLE ALREADY EXISTS
            query="UPDATE details SET occupation=%s WHERE name =%s"
            self.cursor.execute(query,(update_occuppation,name))
            self.connection.commit()
            print("Update make successfully.")
        except mysql.connector.Error as e:
            print(f"Error in connection {e}")
        
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
executor=Updation()
executor.close_connection()
# NOW CALL MEHTOD WHAT NEEDED








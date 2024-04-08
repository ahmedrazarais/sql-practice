# ASSUME HAVING Database in which two tables exist name table_a and table_b  delete the eniter table_a   and delete only contents on table_b



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
            query="DROP TABLE IF EXISTS table_a"
            self.cursor.execute(query)
            self.connection.commit()
            print("Entire Table deleted From database")
        except mysql.connector.Error as e:
            print(f"Error:{e}")
    

    # WRITTING QUERY FOR DELETING CONTENTS OF TABLE
    def write_query_for_deleting_table_contents(self):
        try:
            query="TRUNCATE table_b "
            self.cursor.execute(query)
            self.connection.commit()
            print("Table contents deleted From database")
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
analysis.write_query_for_deleting_table_contents()
analysis.write_query_for_deleting_table()
analysis.close_connection()
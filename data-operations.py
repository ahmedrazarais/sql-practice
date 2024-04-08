# Create a Python script that interacts with a MySQL database to perform the following operations:

# Connect to a MySQL database using credentials provided in a config.py file.
# Retrieve the list of all students from a table named 'students' in the database.
# Print the list of students along with their IDs and names.
# Ensure to handle potential errors gracefully and securely, and close the database connection after completing the operations.


# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Students:
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

    # MEHTOD TO RETRIEVE LIST FROM TABLE 
    def get_students_list(self):
        try:
            query="SELECT * FROM students"
            self.cursor.execute(query)
            data=self.cursor.fetchall()
            return data
        except mysql.connector.Error as e :
            print(f"GEetting error in retreiving list {e}")
            return []

    # MEHTOD TO PRINT DATA
    def display_data(self):
        data=self.get_students_list()
        if data:
            print("ID\t\tNAMES\n")
            for id,name in data:
                print(f"{id}\t{name}")

# MAKING INSTANCE OF CLASS

student=Students()
# student.display_data()
student.close_connection()
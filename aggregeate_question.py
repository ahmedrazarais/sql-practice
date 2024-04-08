# Write a SQL query to retrieve the highest salary from the employees table.









# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Salary:
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
    def Highest_salary(self):
        try:
            # Assuming the table name is 'details' and  to print name of employe who have highest pay in salary column

            query="SELECT MAX (salary) FROM details"
            self.cursor.execute(query)
            highest_pay=self.cursor.fetchone()[0]
            print(f"Employee with highest pay is {highest_pay}$")

          
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
executor=Salary()
# CALL HERE MEHTOD
executor.close_connection()


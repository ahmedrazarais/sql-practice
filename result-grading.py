# Suppose you have a database table named students with the following columns:

# student_id (unique identifier for each student, integer)
# student_name (name of the student, string)
# department (department in which the student is enrolled, string)
# age (age of the student, integer)
# gpa (grade point average of the student, float)
# Write a SQL query to find the top 3 departments with the highest average GPA among students enrolled in each department. Display the results sorted by the average GPA in descending order.

# Your query should return the following columns:

# department (department in which the students are enrolled)
# average_gpa (average GPA of students in that department)
# Implement this SQL query in your code, execute it, and print out the results. You can follow a similar structure to the previous code snippet provided. Make sure to replace the necessary parts such as database connection details and configuration.



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
    
    
    # WRITTING QUERY
    def write_query(self):
        # FOR GETTING AVERAGE SALARAY  
        try:
            query=  """SELECT department,
                   AVG(gpa) AS average_gpa
            FROM students
            GROUP BY department
            ORDER BY average_gpa DESC
            LIMIT 3"""
            self.cursor.execute(query)
            rows=self.cursor.fetchall()
            for row in rows:
                department,average_gpa=row
                print(f"Department: {department}, Average GPA: {average_gpa}")

        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")



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
# analysis.write_query()
analysis.close_connection()
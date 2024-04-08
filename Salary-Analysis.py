# Suppose you have a database table named employees with the following columns:

# employee_id (unique identifier for each employee, integer)
# first_name (first name of the employee, string)
# last_name (last name of the employee, string)
# department (department in which the employee works, string)
# salary (salary of the employee, integer)
# hire_date (date when the employee was hired, date)
# Write a SQL query to find the average salary of employees in each department, along with the total number of employees in that department. Display the results sorted by the average salary in descending order.

# Your query should return the following columns:

# department (name of the department)
# average_salary (average salary of employees in that department)
# total_employees (total number of employees in that department)



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
            query = """
                SELECT department, 
                       AVG(salary) AS average_salary,
                       COUNT(*) AS total_employees
                FROM employees
                GROUP BY department
                ORDER BY average_salary DESC
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for row in results:
                department, average_salary, total_employees = row
                print(f"Department: {department}, Average Salary: {average_salary}, Total Employees: {total_employees}")
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
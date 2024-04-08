# Consider a database schema with two tables: employees and departments.

# The employees table has the following columns:

# employee_id (Primary Key)
# employee_name
# department_id (Foreign Key referencing departments table)
# salary
# The departments table has the following columns:

# department_id (Primary Key)
# department_name
# location
# Write an SQL query to find the average salary of employees in each department.


query="""SELECT departments.department_name, AVG(employees.salary) AS average_salary
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id
GROUP BY departments.department_name;
"""
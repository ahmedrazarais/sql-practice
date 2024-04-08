# Consider two tables: employees and departments.

# The employees table has columns: employee_id, name, department_id, and salary.

# The departments table has columns: department_id and department_name.

# Write an SQL query to retrieve the names of employees along with their department names and salaries.

query="""SELECT e.name, d.department_name, e.salary 
FROM employees e 
JOIN departments d ON e.department_id = d.department_id;
"""
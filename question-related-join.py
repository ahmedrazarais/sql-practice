# Consider a table named students with the following columns: student_id, name, age, and gender.

# Write an SQL query to retrieve the names of all female students who are under the age of 25.

query="""SELECT name 
FROM students 
WHERE gender = 'female' AND age < 25
"""


# Consider a table named orders with the following columns: order_id, customer_id, order_date, and total_amount.

# Write an SQL query to retrieve the total amount of orders placed by each customer, along with their respective customer IDs, ordered by the total amount in descending order.

query="""SELECT customer_id, SUM(total_amount) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC; """
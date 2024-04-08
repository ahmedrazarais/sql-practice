# Consider a table named orders with the following columns: order_id, customer_id, order_date, and total_amount.

# Write an SQL query to retrieve the total number of orders placed by each customer, ordered by the total number of orders in descending order.

query="""SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;
"""
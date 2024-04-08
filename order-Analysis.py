# Suppose you have a database table named orders with the following columns:

# order_id (unique identifier for each order, integer)
# customer_id (identifier for the customer who placed the order, integer)
# order_date (date when the order was placed, date)
# total_amount (total amount of the order, integer)
# Write a SQL query to find the total number of orders placed by each customer, along with the total amount spent by each customer. Display the results sorted by the total amount spent in descending order.

# Your query should return the following columns:

# customer_id (identifier for the customer)
# total_orders (total number of orders placed by the customer)
# total_amount_spent (total amount spent by the customer)


# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

class Analysis:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD
            )
            self.cursor = self.connection.cursor()
            print("Connection created successfully")
        except mysql.connector.Error as e:
            print(f"Error in connection {e}")
    
    def write_query(self):
        try:
            query = """
                SELECT customer_id,
                       COUNT(order_id) AS total_orders,
                       SUM(total_amount) AS total_amount_spent
                FROM orders
                GROUP BY customer_id
                ORDER BY total_amount_spent DESC
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            for row in results:
                customer_id, total_orders, total_amount_spent = row
                print(f"Customer ID: {customer_id}, Total Orders: {total_orders}, Total Amount Spent: {total_amount_spent}")
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
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

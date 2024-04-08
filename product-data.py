# Consider a table named products with the following columns: product_id, product_name, category, and price.

# Write an SQL query to retrieve the names of products and their prices for products that belong to the 'Electronics' category and have a price greater than $500.

def write_query():
    query="""SELECT product_name, price 
    FROM products 
    WHERE category = 'Electronics' AND price > 500;
    """

write_query()
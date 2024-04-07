# Task for you is taht make a class insertion in which make table name students having 3 columns id proimary key name and age after that add sample data in taht table
#sample_data = [
#     (1, 'Raza', 20),
#     (2, 'Ahmed', 22),
#     (3, 'Ali', 21)
# ] DONT HANDLE THAT CASE WHEN DATA Alraedy enter

## Setting up Database Configuration

# 1. Create a file named `config.py` in the root directory of the project.
# 2. Inside `config.py`, define the following variables with your MySQL database connection details:


# DB_HOST = 'your_database_host'
# DB_USER = 'your_database_username'
# DB_PASSWORD = 'your_database_password'



import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

class Insertion:
    def __init__(self):
        try:
            # Establish connection to MySQL database
            self.conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
            )
            self.database = "college"
            print("Connected to MySQL database successfully!")
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def create_database(self):
        try:
            # Create 'college' database if it doesn't exist
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Database '{self.database}' created successfully!")
        except mysql.connector.Error as e:
            print(f"Error creating database: {e}")

    def close_connection(self):
        # Close database connection
        try:
            if self.conn.is_connected():
                self.cursor.close()
                self.conn.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")

    def create_table(self):
        try:
            # Switch to 'college' database
            self.cursor.execute(f"USE {self.database}")
            # Create 'students' table if it doesn't exist
            query = """CREATE TABLE IF NOT EXISTS students 
                       (id INT NOT NULL PRIMARY KEY,
                       name VARCHAR(50),
                       age INT)"""
            self.cursor.execute(query)
            self.conn.commit()
            print("Table 'students' created successfully.")
        except mysql.connector.Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self, data):
        try:
            # Insert data into 'students' table
            query = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
            self.cursor.executemany(query, data)
            self.conn.commit()
            print("Sample data inserted successfully.")
        except mysql.connector.Error as e:
            print(f"Error inserting data: {e}")

# Example data with unique primary key values
sample_data = [
    (1, 'Raza', 20),
    (2, 'Ahmed', 22),
    (3, 'Ali', 21)
]

# Create an instance of Insertion class
table = Insertion()
table.create_database()  # Create the database
table.create_table()     # Create the 'students' table
table.insert_data(sample_data)  # Insert sample data into the table
table.close_connection()  # Close the database connection

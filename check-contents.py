# task for you to add sample data and then show that data for users sample data is name subject and marks
# make databse naem university and table name 
# importing mysql connector  and from config file database name password

import mysql.connector
from config import DB_HOST,DB_PASSWORD,DB_USER

class Display:
    def __init__(self):
      try:
        # making database connection
        self.connection=mysql.connector.connect(
            host=DB_HOST,
            password=DB_PASSWORD,
            user=DB_USER  )
        
        self.database = "university"
        print("Connected to MySQL database successfully!")
        self.cursor = self.connection.cursor()
        # Select the database
        self.cursor.execute(f"USE {self.database}")

      except mysql.connector.Error as e:
         print(f"Error connecting to MySQL database: {e}")
        
    
    # mehtod to craet database
    def create_database(self):
       try:
          self.cursor.execute("CREATE DATABASE IF NOT EXISTS university")
          print("Databse Created Successfully")
       except mysql.connector.Error as e:
          print(f"Getting Error in creating Database {e}")


    # mehtod to close database connection
    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")


    # mehtod to create table

    def creating_table(self):
       try:
          self.cursor.execute("""CREATE TABLE IF NOT EXISTS result 
                              (name VARCHAR (20),
                              marks INT NOT NULL,
                              subject VARCHAR(25))
                                    """)
          self.connection.commit()
          print("Table created successfully.")

       except mysql.connector.Error as e:
          print(f"Error creating table as {e}")
    

    # mehtod to insert data

    def insert_data(self, data):
        try:
            query = "INSERT INTO result (name, marks, subject) VALUES (%s, %s, %s)"
            self.cursor.executemany(query, data)
            self.connection.commit()
            print("Data entered successfully.")
        except mysql.connector.Error as e:
            print(f"Error inserting data: {e}")
       
    # to show all data

    def display_data(self):
       try:
          self.cursor.execute("SELECT * FROM result")
          # Fetch all rows from the result set
          rows = self.cursor.fetchall()
        # Display each row
          for row in rows:
            print(row)
        
       except mysql.connector.Error as e:
          print(f"Error in display data as {e}")
       

sample_data = [
    ('Raza', 20,"Maths"),
    ('Ahmed', 22,"Biology"),
    ('Ali', 21,"Physics")
]
# making instance of class
query=Display()
query.create_database()
query.creating_table()
query.insert_data(sample_data)
query.display_data()
query.close_connection()

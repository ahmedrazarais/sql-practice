# Create a Python script that interacts with a MySQL database to implement user authentication. Your script should perform the following operations:

# Connect to a MySQL database using credentials provided in a config.py file.
# Prompt the user to enter their username and password.
# Verify the user's credentials against the data stored in a 'users' table in the database.
# If the username and password match a record in the 'users' table, print a success message and grant access. Otherwise, print an error message indicating that the credentials are invalid.
# check username in username column and password in password column
# Make sure to handle any potential errors gracefully and securely.
# After completing the authentication process, close the database connection.



# firt import sql connector abd password username from config.py file
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD

# making a class
class Authentication:
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

    # MEHTOD TO CLOSE CONNECTION
    def close_connection(self):
        # Close database connection
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("Connection to MySQL database closed.")
        except mysql.connector.Error as e:
            print(f"Error closing connection: {e}")
 

    # mehtod to take username and password input
    def prompt_username_password(self):
        username=input("Enter username (enter 0 to back):")
        if username=="0":
            return
        password=input("Enter password (enter 0 to back)")
        if password=="0":
            return
        return username,password
    
    
    # MEHTOD TO FETCH DATA FROM TABLE users
    def getting_data_from_table(self):
        try:
            query = "SELECT username, password FROM users"
            self.cursor.execute(query)
            return self.cursor.fetchall()
         
        except mysql.connector.Error as e:
            print(f"Error fetching user data: {e}")
            return []
    
    # Checking creadentials of users
    def check_credentials(self):
        data=self.getting_data_from_table()
        while True:
            username,password=self.prompt_username_password()
            if username:
                for user,pswd in data:
                    if user==username:
                        if pswd==password:
                            print("Login successfull\n")
                            return
                        else:
                            print("Invalid password")
                    else:
                        print("Invalid username")

# making instance of class
user=Authentication()
# user.prompt_username_password()
user.close_connection()

            

        












# auth.py
import mysql.connector
from mysql.connector import Error
import hashlib
import os
from dotenv import load_dotenv
load_dotenv()

# Now the environment variables will be loaded from the .env file


# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

# User login function
def is_authenticated(username, password):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and user["password"] == hash_password(password):
            return True
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
    return False

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

# Function to insert a user
def insert_user(username, password):
    hashed_password = hash_password(password)
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, hashed_password))
        connection.commit()
        print("User inserted successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

# Example usage
insert_user("DrRizwan", "Rizwan10")

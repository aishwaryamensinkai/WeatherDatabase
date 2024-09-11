import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    try:
        # Establish a database connection
        print("🔌 Connecting to the database...")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if conn.is_connected():
            print("✅ Successfully connected to the database!")
        return conn

    except mysql.connector.Error as err:
        # Detailed error message with proper logging
        print(f"❌ Error: Unable to connect to the database. Reason: {err}")
        raise  # Reraise the error to indicate a critical issue

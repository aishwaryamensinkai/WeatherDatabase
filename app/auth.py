import bcrypt
import mysql.connector
from config.db import get_db_connection

# Register a new user with proper error handling
def register(username, password):
    if not username or not password:
        print("⚠️  Error: Username and password cannot be empty.")
        return

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the username already exists
        print(f"🔍 Checking if username '{username}' is available...")
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            print("⚠️  Error: Username already taken. Please choose a different username.")
            return

        # Hash the password and store the user
        print(f"🔐 Registering new user: {username}...")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("✅ User registered successfully!")
    
    except mysql.connector.Error as err:
        print(f"❌ Database error during registration: {err}")
    
    except Exception as e:
        print(f"❌ An unexpected error occurred during registration: {e}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Log in an existing user with error handling
def login(username, password):
    if not username or not password:
        print("⚠️  Error: Username and password cannot be empty.")
        return None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        print(f"🔍 Verifying credentials for username: {username}...")
        cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        # Check if password matches
        if result and bcrypt.checkpw(password.encode('utf-8'), result[1].encode('utf-8')):
            print("✅ Login successful!")
            return result[0]
        else:
            print("⚠️  Error: Invalid username or password.")
            return None

    except mysql.connector.Error as err:
        print(f"❌ Database error during login: {err}")
    
    except Exception as e:
        print(f"❌ An unexpected error occurred during login: {e}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Update user profile (username or password)
def update_profile(user_id, new_username=None, new_password=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if new_username:
            # Check if the new username already exists
            print(f"🔍 Checking if new username '{new_username}' is available...")
            cursor.execute("SELECT id FROM users WHERE username = %s", (new_username,))
            if cursor.fetchone():
                print("⚠️  Error: Username already exists. Choose a different username.")
                return

            cursor.execute("UPDATE users SET username = %s WHERE id = %s", (new_username, user_id))
            print(f"✅ Username updated successfully to {new_username}!")

        if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
            print("✅ Password updated successfully!")

        conn.commit()
    
    except mysql.connector.Error as err:
        print(f"❌ Database error during profile update: {err}")
    
    except Exception as e:
        print(f"❌ An unexpected error occurred during profile update: {e}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

import mysql.connector
import json
from config.db import get_db_connection

# Store search history
def store_search_history(user_id, location, weather_data):
    try:
        # Serialize the weather_data dictionary to JSON format
        weather_data_json = json.dumps(weather_data, ensure_ascii=False)

        conn = get_db_connection()
        cursor = conn.cursor()

        print(f"🗂️ Storing search history for {location}...")

        cursor.execute("""
            INSERT INTO search_history (user_id, location, weather_data, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (user_id, location, weather_data_json, weather_data['timestamp']))
        conn.commit()

        print("✅ Search history saved successfully!")
    
    except mysql.connector.Error as err:
        print(f"❌ Database error during storing history: {err}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# View search history
def view_search_history(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM search_history WHERE user_id = %s", (user_id,))
        results = cursor.fetchall()

        if results:
            print("\n📜 Search History:")
            for row in results:
                try:
                    # Deserialize the JSON weather data
                    weather_data = json.loads(row[3])
                    print(f"🔹 ID: {row[0]} - Location: {row[2]} - Time: {row[4]}")
                    print(f"🌤️  Weather: Description: {weather_data['description']}, Temp: {weather_data['temperature']}°C, Humidity: {weather_data['humidity']}%, Wind Speed: {weather_data['wind_speed']} m/s")
                    print("-" * 40)
                except json.JSONDecodeError as e:
                    print(f"❌ Error decoding weather data for entry {row[0]}: {e}")
        else:
            print("🔍 No search history found.")
    
    except mysql.connector.Error as err:
        print(f"❌ Database error during fetching history: {err}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

# Delete specific entry from search history
def delete_search_history(user_id, entry_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        print(f"🗑️ Attempting to delete entry {entry_id}...")

        cursor.execute("DELETE FROM search_history WHERE id = %s AND user_id = %s", (entry_id, user_id))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Entry {entry_id} deleted successfully!")
        else:
            print(f"⚠️ Entry {entry_id} not found.")
    
    except mysql.connector.Error as err:
        print(f"❌ Database error during deletion: {err}")
    
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

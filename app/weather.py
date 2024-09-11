import requests
import os
from config.db import get_db_connection

def get_weather(location):
    API_KEY = os.getenv("API_KEY")
    try:
        print(f"🌍 Fetching current weather for {location}...")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the response is successful
        if data["cod"] == 200:
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f"✅ Current weather in {location}: {description}, {temp}°C")
            return data
        else:
            print(f"❌ Error: Location '{location}' not found. Please try again.")
            return None
    
    except Exception as e:
        print(f"⚠️ An error occurred while fetching the weather data: {e}")
        return None


def get_five_day_forecast(location):
    API_KEY = os.getenv("API_KEY")
    try:
        print(f"🌍 Fetching 5-day weather forecast for {location}...")
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the response is successful
        if data["cod"] == "200":
            for forecast in data["list"]:
                date = forecast['dt_txt']
                description = forecast['weather'][0]['description']
                temp = forecast['main']['temp']
                # print(f"📅 Date: {date} - {description} - {temp}°C")
            return data
        else:
            print(f"❌ Error: Location '{location}' not found. Please try again.")
            return None
    
    except Exception as e:
        print(f"⚠️ An error occurred while fetching the 5-day forecast: {e}")
        return None

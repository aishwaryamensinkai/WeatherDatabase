from app.auth import register, login, update_profile
from app.history import view_search_history, store_search_history, delete_search_history
from app.weather import get_weather, get_five_day_forecast
from datetime import datetime

def main():
    try:
        print("========================================")
        print("🌤️  Welcome to the Weather App!  🌤️")
        print("========================================")
        
        # Input validation for yes/no response
        while True:
            choice = input("\n❓ Do you have an account? (yes/no): ").strip().lower()
            if choice in ['yes', 'no']:
                break  # Exit loop if input is valid
            else:
                print("⚠️  Invalid input. Please type 'yes' or 'no'.")

        if choice == 'no':
            username = input("👤 Choose a username: ").strip()
            password = input("🔒 Choose a password: ").strip()
            register(username, password)
            print("✅ Account created successfully!")

        # Loop until the user logs in successfully
        user_id = None
        while user_id is None:
            print("\n🔐 Please log in:")
            username = input("👤 Username: ").strip()
            password = input("🔒 Password: ").strip()
            user_id = login(username, password)
            if user_id is None:
                print("⚠️  Invalid username or password. Please try again.")

        # Once logged in, proceed with the rest of the functionality
        if user_id:
            while True:
                print("\n========================================")
                print("🌤️  Weather App Menu  🌤️")
                print("========================================")
                print(
                    "1️⃣  Search Weather\n"
                    "2️⃣  View Search History\n"
                    "3️⃣  Delete Search History Entry\n"
                    "4️⃣  Update Profile\n"
                    "5️⃣  5-day Weather Forecast\n"
                    "6️⃣  Exit"
                )
                option = input("\n🔢 Choose an option: ")

                if option == '1':
                    location = input("\n📍 Enter a location: ").strip()
                    weather = get_weather(location)
                    if weather:
                        # Extract relevant weather information
                        description = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        humidity = weather['main']['humidity']
                        wind_speed = weather['wind']['speed']

                        print(f"\n🌤️  Current weather in {location}:")
                        print(f"🌧️  Description: {description}")
                        print(f"🌡️  Temperature: {temp}°C")
                        print(f"💧 Humidity: {humidity}%")
                        print(f"💨 Wind Speed: {wind_speed} m/s")

                        # Get current timestamp for the search
                        search_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        # Store the search data in the history, including weather details and timestamp
                        store_search_history(user_id, location, {
                            'description': description,
                            'temperature': temp,
                            'humidity': humidity,
                            'wind_speed': wind_speed,
                            'timestamp': search_timestamp
                        })
                        print("✅ Search history updated!")

                elif option == '2':
                    print("\n📜 Your search history:")
                    view_search_history(user_id)

                elif option == '3':
                    entry_id = input("\n🗑️  Enter the entry ID to delete: ")
                    delete_search_history(user_id, entry_id)
                    print("✅ Search history entry deleted!")

                elif option == '4':
                    print("\n🛠️  Update Profile Options:")
                    print("1️⃣  Update Username")
                    print("2️⃣  Update Password")
                    update_choice = input("Choose an update option (1 for username, 2 for password): ").strip()

                    if update_choice == '1':
                        new_username = input("👤 Enter your new username: ").strip()
                        update_profile(user_id, new_username=new_username)
                        print("✅ Username updated!")
                    elif update_choice == '2':
                        new_password = input("🔒 Enter your new password: ").strip()
                        update_profile(user_id, new_password=new_password)
                        print("✅ Password updated!")
                    else:
                        print("⚠️  Invalid option. Please choose either 1 or 2.")

                elif option == '5':
                    location = input("\n📍 Enter a location for the 5-day forecast: ").strip()
                    forecast = get_five_day_forecast(location)
                    if forecast:
                        print(f"\n📅 5-day weather forecast for {location}:")
                        for day in forecast['list']:
                            date = day['dt_txt']
                            description = day['weather'][0]['description']
                            temp = day['main']['temp']
                            print(f"📅 Date: {date} - {description}, {temp}°C")

                elif option == '6':
                    print("\n👋 Exiting the application. Have a great day!")
                    break

                else:
                    print("⚠️  Invalid option. Please choose a valid number.")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        print("⚠️  The application will now close. Please restart.")


if __name__ == '__main__':
    main()

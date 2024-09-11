# Weather CLI Application

This is a Python-based weather application that allows users to retrieve weather information for a specified location. The app supports user authentication, stores search history in a database, and allows users to revisit previous weather searches.

## Project Structure

```bash
.
├── README.md
├── app
│   ├── auth.py         # Handles user authentication (login, registration)
│   ├── history.py      # Manages search history retrieval and display
│   └── weather.py      # Fetches and displays weather data from external API
├── config
│   └── db.py           # Database connection and setup
├── database.txt        # SQL commands for database setup
├── main.py             # Main application entry point
├── requirements.txt    # List of dependencies
```

## Features
- **User Registration & Login**: Users can register and log in using their credentials.
- **Weather Search**: Fetch current weather data for any location.
- **Search History Management**: Store and view past weather searches.

## Requirements
- Python 3.6+
- MySQL Server
- OpenWeatherMap API Key

Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```
The app uses the following dependencies:
- mysql-connector-python==8.0.31
- bcrypt==3.2.0
- requests==2.28.1
- python-dotenv==0.21.0

## Usage
Set up the database by running the commands in database.txt.
Run the application:
```bash
python main.py
```

## Environment Variables
You need to set up a .env file with the following values:
```bash
DB_HOST=<your_database_host>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_NAME=weather_app
API_KEY=<your_weather_api_key>

```

## Data Flow Diagram
A data flow diagram (DFD) visually represents how data flows through the application. It can show how the user interacts with the CLI, the flow of data through the different modules, and how the database and API are involved.

You can include a simple diagram using tools like Lucidchart, draw.io, or Mermaid.js in markdown:
```bash
graph TD;
User -->|Input Location| CLI --> WeatherAPI;
WeatherAPI --> CLI -->|Display| User;
CLI -->|Store Search History| DB;
DB --> CLI -->|Retrieve History| User;
```

## Performance Considerations
To optimize the performance of the application:
- Use caching to minimize API calls.
- Implement database indexing on frequently queried fields like user_id in the search_history table.
- Consider optimizing API response handling, e.g., by limiting the size of weather data stored.

## Known Issues
- API Limits: OpenWeatherMap API has rate limits. Be cautious of exceeding the free tier limits.
- Database Connection Timeout: Occasionally, the MySQL connection may time out. Implement retry logic or increase the connection timeout in the database settings.

## Notes
- The application uses `bcrypt` to hash passwords.
- Make sure to use a valid API key from OpenWeatherMap.

## Contributing
- Fork the repository.
- Create a new feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.

## FAQ
How do I reset my password?
You can implement a "forgot password" feature using the same bcrypt library to rehash and reset the password.

Can I run the application without MySQL?
MySQL is required for user management and history storage. However, you could modify the code to use SQLite for a simpler local setup.

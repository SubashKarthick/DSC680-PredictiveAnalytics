# Weather Forecasts
# Author: A Rabson
# 08/12/2023

# Required Libraries
import requests

# API key for OpenWeatherMap's One Call API
API_KEY_ONE_CALL = "insert your API Key here"

 
# Function to fetch latitude and longitude based on city or zip code using
# OpenWeatherMap's One Call API.
def get_lat_lon(query, query_type):
    endpoint = ""
    if query_type == 'city':
        # Splits parameter back into two entered user variables
        city, state = query.split(',')
        # Formats URL for a city, state call to the API
        endpoint = f"http://api.openweathermap.org/geo/1.0/direct?q=" \
                   f"{city},{state},US&appid={API_KEY_ONE_CALL}"
    elif query_type == 'zip':
        # Formats URL for a zip call to the API
        endpoint = f"http://api.openweathermap.org/geo/1.0/zip?zip=" \
                   f"{query},US&appid={API_KEY_ONE_CALL}"

    try:
        # Make a GET request to the One Call API using the specified URL
        response = requests.get(endpoint)
        # Raises an exception if status code indicates an error (404, 500, etc)
        response.raise_for_status()
        # Parses the response content as JSON data to store in 'data' variable
        data = response.json()
        # Checks if JSON data was successfully pulled and contains lat, lon
        if data:
            if query_type == 'city':
                # Return latitude, longitude, city name, and country for city
                return data[0]['lat'], data[0]['lon'], data[0]['name'], \
                       data[0]['country']
            elif query_type == 'zip':
                # Return latitude, longitude, city name, and country for zip
                return data['lat'], data['lon'], data['name'], data['country']
        else:
            # Notifies user no data found and returns None for all variables
            print(f"No data found for {query}. Please ensure the city or zip "
                  f"code is correct.")
            return None, None, None, None
    # Notifies user to other errors and returns None for all variables
    except requests.ConnectionError:
        print("Error: Unable to connect to the internet. Please check your "
              "connection.")
        return None, None, None, None
    except requests.Timeout:
        print("Error: The request timed out. Please try again later.")
        return None, None, None, None
    except requests.RequestException:
        print(f"Error fetching latitude and longitude for {query}. Ensure "
              f"it's a valid city/state or zip code.")
        return None, None, None, None


# Function to fetch weather data based on latitude and longitude using
# OpenWeatherMap's One Call API.
def get_weather_data_one_call(lat, lon, unit):
    # Formats URL to pull weather data excluding certain info and setting
    # desired unit of measurement
    endpoint = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}" \
               f"&lon={lon}&exclude=minutely,hourly,alerts&units={unit}&" \
               f"appid={API_KEY_ONE_CALL}"
    try:
        # Sends a GET request to the specified endpoint
        response = requests.get(endpoint)
        # Checks if response has an error status code and raises an exception
        response.raise_for_status()
        # Converts the response data from JSON format to a Python dictionary
        return response.json()
    # Notifies user to any likely errors
    except requests.ConnectionError:
        print("Error: Unable to connect to the internet. Please check your "
              "connection.")
    except requests.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


# Function to display weather data in readable format
def display_weather_one_call(data, unit):
    # Creates dictionary for symbols of unit chosen
    symbols = {
        'metric': '°C',
        'imperial': '°F',
        'standard': 'K'
    }
    # Pulls from the data current data and daily data into two dictionaries
    current_data = data['current']
    daily_data = data['daily'][0]

    # Extract required weather information
    current_temp = current_data['temp']
    feels_like = current_data['feels_like']
    low_temp = daily_data['temp']['min']
    high_temp = daily_data['temp']['max']
    pressure = current_data['pressure']
    humidity = current_data['humidity']
    description = current_data['weather'][0]['description']

    # Prints formatted output for desired fields
    print(f"Current Temperature: {current_temp}{symbols[unit]}")
    print(f"Feels Like: {feels_like}{symbols[unit]}")
    print(f"Low Temperature: {low_temp}{symbols[unit]}")
    print(f"High Temperature: {high_temp}{symbols[unit]}")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")


# Functions to validate user input
def validate_city(city):
    # Checks if city name is within a reasonable (arbitrary) range
    if 2 <= len(city) <= 50:
        return True
    return False


def validate_state(state):
    # validates user's state against a list of all states
    valid_states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    if state.upper() in valid_states:
        return True
    return False


def validate_zip(zip_code):
    # Checks that the zip is correct length and is only made up of numbers
    if len(zip_code) == 5 and zip_code.isdigit():
        return True
    return False


# Gets user input and validates it against a set of acceptable responses.
def get_user_input(prompt, valid_responses):
    # Sets the input with error handling for white spaces and capitalisation
    user_input = input(prompt).lower().strip()
    # If not a valid response, notifies user and loops until valid
    while user_input not in valid_responses:
        print("Invalid choice. Please try again.")
        user_input = input(prompt).lower().strip()
    return user_input


# Main function encapsulating the program logic
def main():
    print("Welcome to the Weather Forecast Program!")
    while True:
        # Asking the user for their preferred search method (city or zip code)
        query_type = get_user_input(
            "\nWould you like to search by city or zip code? (city/zip): ",
            ["city", "zip"])

        if query_type == "city":
            # Asks user for city with error handling
            city = input("Enter the city name: ").strip().lower()
            while not validate_city(city):
                print("Invalid city name. Please enter a valid city name.")
                city = input("Enter the city name: ").strip().lower()
            # Asks user for city's state, capitalising and validating
            state = input("Enter the state abbreviation "
                          "(e.g., NY for New York): ").strip()
            while not validate_state(state):
                print("Invalid input. Please enter a valid state abbreviation.")
                state = input("Enter the state abbreviation "
                              "(e.g., NY for New York): ").strip()
            # Sets query as city, state to use in API call
            query = f"{city},{state}"
        else:
            # Asks user for zip code with error handling
            zip_code = input("Enter the zip code: ").strip()
            while not validate_zip(zip_code):
                print("Invalid zip code. "
                      "Please enter a valid 5-digit zip code.")
                zip_code = input("Enter the zip code: ").strip()
            # Sets query as zip to use in API call
            query = zip_code

        # Fetching latitude, longitude, city name and country
        lat, lon, name, country = get_lat_lon(query, query_type)

        # If latitude and longitude were successfully fetched
        if lat and lon:
            # Asks user which unit to display the temperature in
            unit = get_user_input(
                "\nChoose temperature unit:\nC - Celsius\nF - Fahrenheit\nK - "
                "Kelvin\nYour choice (c/f/k): ",
                ['c', 'f', 'k']).lower()
            units_map = {
                'c': 'metric',
                'f': 'imperial',
                'k': 'standard'
            }

            weather_data = get_weather_data_one_call(lat, lon, units_map[unit])
            # If successfully fetched the data, calls function to display
            # in a readable format
            if weather_data:
                print(f"\nWeather for {name}, {country}:")
                display_weather_one_call(weather_data, units_map[unit])

            # Asking the user if they want to continue or exit the program
            choice = get_user_input(
                "\nWhat would you like to do next?\n1 - Search for another "
                "location\n2 - Exit program\nYour choice (1/2): ",
                ['1', '2'])
            if choice == '2':
                break
        else:
            print(
                "Unable to fetch weather data for the provided location. "
                "Please try again.")


# Executes the main function
if __name__ == "__main__":
    main()

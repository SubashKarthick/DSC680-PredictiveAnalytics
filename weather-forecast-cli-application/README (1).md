# Weather Forecast CLI (Python)

A robust, user-friendly command-line tool to retrieve real-time weather conditions for any U.S. location using the OpenWeatherMap API. Developed as part of the MSc Data Science program.

---

## Overview

This application provides accurate and up-to-date weather information by leveraging OpenWeatherMap’s One Call API.  
Users can search by city/state or zip code, select their preferred temperature unit (Celsius, Fahrenheit, Kelvin), and receive detailed current weather metrics—all directly in the terminal.

---

## Key Features

- **Flexible Location Search**  
  Retrieve weather data by entering either a U.S. city and state abbreviation or a 5-digit zip code.

- **Customizable Units**  
  Choose from Celsius, Fahrenheit, or Kelvin for temperature display.

- **Comprehensive Weather Metrics**  
  Displays current temperature, “feels like” temperature, daily minimum/maximum, atmospheric pressure, humidity, and sky condition descriptions.

- **Interactive & Robust Input Validation**  
  Ensures only valid cities, states, and zip codes are accepted, reducing user error.

- **Error Handling**  
  Handles connectivity, timeout, and invalid input issues gracefully, with clear messaging.

---

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/)
- `requests` Python package  
  (Install with: `pip install requests`)

### Setup & Usage

1. **Clone or download** this project folder.
2. Obtain a free [OpenWeatherMap API key](https://openweathermap.org/api) and enter it into the code if required.
3. Run the program from the terminal:
   ```bash
   python weatherprojectmain.py

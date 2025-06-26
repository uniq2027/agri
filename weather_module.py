# def get_weather_info(location):
#     # This can later be replaced with real API data
#     dummy_weather = {
#         "Chennai": {"temp": "34°C", "rain": "Low", "advice": "Water crops early morning"},
#         "Delhi": {"temp": "38°C", "rain": "None", "advice": "Avoid sowing new seeds"},
#         "Mumbai": {"temp": "29°C", "rain": "High", "advice": "Good for rice cultivation"},
#         "Hyderabad": {"temp": "32°C", "rain": "Moderate", "advice": "Time for sowing pulses"},
#     }

#     return dummy_weather.get(location, {"temp": "N/A", "rain": "N/A", "advice": "Weather data not found"})






#____________________connect with API____________________

import requests

API_KEY = "ce6e5deec3f60f529f9148e090d7a5ff"  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_info(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            return {
                "temp": "N/A",
                "rain": "N/A",
                "advice": "Location not found or API limit exceeded."
            }

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        advice = generate_agri_advice(temp, weather_desc)

        return {
            "temp": f"{temp}°C",
            "rain": weather_desc.title(),
            "advice": advice
        }

    except Exception as e:
        return {
            "temp": "N/A",
            "rain": "N/A",
            "advice": f"Error fetching weather: {str(e)}"
        }

def generate_agri_advice(temp, weather):
    if "rain" in weather.lower():
        return "Rain expected — great for sowing rice or sugarcane."
    elif float(temp) > 35:
        return "Very hot — irrigate crops regularly and avoid sowing new seeds."
    elif float(temp) < 20:
        return "Cool temperature — suitable for crops like wheat or peas."
    else:
        return "Good temperature for most crops — proceed with usual practices."






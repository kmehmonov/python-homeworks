import requests
from datetime import datetime

from apikeys import weather_api

my_api = weather_api
weather_url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exc}&units={units}&appid={api_id}"
coordinate_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_id}"

def get_coordinates(city_name: str, country_code: str = ''):
    """
    Get lat and lon from city name
    Args:
        city_name: str
        country_code: str
             ISO 3166 country codes (optional)
    Returns:
        A dictionary containing geolocation data
    """
    try:
        url = coordinate_url.format(
            city_name=city_name,
            state_code='',
            country_code=country_code,
            limit=1,
            api_id=my_api
        )
        res = requests.get(url)
        res.raise_for_status()  # Raise an HTTPError for bad responses
        geo_data = res.json()
        if not geo_data:
            raise ValueError(f"Could not find location data for {city_name}.")
        return geo_data[0]
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        raise

def get_weather(city_name: str, stat='current') -> None:
    """ 
    Get weather data for a specified city.
    
    Args:
        city_name: str
            The name of the city.
        stat: str
            Type of weather data to fetch: 'current', 'minutely', 'hourly', or 'daily'.
    
    Returns:
        weather dict
            The weather data for the specified city.
    """
    try:
        exclude = {
            "current": True,
            "minutely": True,
            "hourly": True,
            "daily": True,
            "alerts": True
        }
        if stat:
            exclude[stat.lower()] = False
        exclude_str = ",".join(item for item in exclude.keys() if exclude[item])

        # Get lat and lon
        geo_data: dict = get_coordinates(city_name)

        url = weather_url.format(
            lat=geo_data["lat"],
            lon=geo_data["lon"],
            exc=exclude_str,
            units='metric',
            api_id=my_api
        )

        weather = requests.get(url)
        weather.raise_for_status()  # Check if the request was successful
        weather_data = weather.json()

        # Handle different types of weather data
        if stat == "current":
            print_current_weather(weather_data)
        elif stat == "daily":
            print_daily_weather(weather_data)
        elif stat == "hourly":
            print_hourly_weather(weather_data)
        else:
            print("Currently, only 'current', 'daily', and 'hourly' weather are supported.")

        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error processing data: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def print_current_weather(data: dict) -> None:
    """
    print current weather
    """
    current = data["current"]
    time = datetime.fromtimestamp(current["dt"])
    temp = current["temp"]
    feels_like = current["feels_like"]
    pressure = current["pressure"]
    humidity = current["humidity"]
    wind_speed = current["wind_speed"]

    print(f"""
    {"-"*10} Today: {time} {"-"*10}
    temp = {temp} \u00b0C
    feels_like = {feels_like} \u00b0C
    pressure = {pressure} Pa
    humidity = {humidity} %
    wind_speed = {wind_speed} m/s
""")

def print_hourly_weather(data: dict) -> None:
    """
    print hourly weather
    """
    hourlies = data["hourly"]
    for hourly in hourlies:
        time = datetime.fromtimestamp(hourly["dt"])
        temp = hourly["temp"]
        pressure = hourly["pressure"]
        humidity = hourly["humidity"]
        wind_speed = hourly["wind_speed"]

        print(f"""
        {"-"*10} Today: {time.strftime("%Y-%m-%d")} {"-"*10}
        Time: {time.strftime("%H-%M-%S")}
        temp = {temp} \u00b0C
        pressure = {pressure} Pa
        humidity = {humidity} %
        wind_speed = {wind_speed} m/s
""")

def print_daily_weather(data: dict) -> None:
    """
    print daily weather
    """
    dailies = data["daily"]
    for daily in dailies:
        time = datetime.fromtimestamp(daily["dt"])
        temp = daily["temp"]
        pressure = daily["pressure"]
        humidity = daily["humidity"]
        wind_speed = daily["wind_speed"]

        print(f"""
        {"-"*10} Date: {time.strftime("%Y-%m-%d")} {"-"*10}
        temp:
            morning = {temp["morn"]} \u00b0C
            evening = {temp["eve"]} \u00b0C
            night = {temp["night"]} \u00b0C
            day = {temp["day"]} \u00b0C
            min = {temp["min"]} \u00b0C
            max = {temp["max"]} \u00b0C
        pressure = {pressure} Pa
        humidity = {humidity} %
        wind_speed = {wind_speed} m/s
""")
    



if __name__ == "__main__":

    get_weather(city_name="Tashkent", stat="current")

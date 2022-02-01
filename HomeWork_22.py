import requests

def get_weather():

    city = input()
    key = '9c4e929252e352abf06d3ee895e1a477'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)

    weather = result.json()

    print(f'''{str(weather["name"])}:
Temperature: {weather["main"]["temp"]}C
Feels like: {weather["main"]["feels_like"]}C
Pressure: {weather["main"]["pressure"]}mm
Humidity: {weather["main"]["humidity"]}%
Wind: {weather["wind"]["speed"]}m/s
''')

get_weather()


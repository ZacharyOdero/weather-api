#this is a simple API to display the weather conditions around the world.
import requests


API_KEY = '219eaf2a551bb39b05da1d675fff18fe'
BASE_URL = " https://api.openweathermap.org/data/2.5/weather" #url of the website from which the data is obtained

city = input('Enter city: ') #query parameter for the request url
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url) #data is stored in response variable.

if response.status_code == 200: #runs succeeding code if the operation is successful. This is indicated when the status code is 200.
    data = response.json() #converts the data into a json file
    #one can choose the data to be displayed per search
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    wind_speed = data['wind']['speed']
    longitude = data['coord']['lon']
    latitude = data['coord']['lat']
    #displaying the selected data
    print("Weather: ", weather)
    print(f'Temperature: {temperature} degree celsius')
    print(f'Wind speed: {wind_speed} m/s')
    print(f'Longitude: {longitude}')
    print(f'Latitude: {latitude}')

else:
    print("An error has occurred.")


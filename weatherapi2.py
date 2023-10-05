import requests

def getweather():
    ui = input("Enter a city name or zip code: ")
    
    apk = 'a96ba83c385ad73a6c8965b437658d84'

    burl = 'https://api.openweathermap.org/data/2.5/weather?'

    url = f'{burl}q={ui}&appid={apk}'
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {ui}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("Failed to retrieve weather data.")
        exit()

if __name__ == "__main__":
    getweather()

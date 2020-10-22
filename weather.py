import requests
import os






# temp = data['main']['temp']

# print(f'The current temperature is {temp} F')



def get_city():
    print('Please enter in a city in this format:')
    print('Format: \'city,country code\' ')
    city = input('Enter: ')

    return city


def get_data(city):

    key = os.environ.get('WEATHER_KEY')
    
    query = {'q' : {city}, 'units': 'imperial', 'appID' : key}
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()

    return data

def parse_data(data):
    forecasts = data['list']

    for x, forecast in enumerate(forecasts):

        if (x % 8) == 0:   # 8 forecasts in a day
            day = x/8 + 1     
            print(f'Day {day:.0f}')
            
        times = forecast['dt_txt']
        temp = forecast['main']['temp']
        desc = forecast['weather'][0]['description']  # there's a list in the weather attribute
        wind = forecast['wind']['speed']
        print(f'Date: {times} | Temp: {temp} F  | Wind: {wind} MPH {desc}')


def main():

    city = get_city()
    data = get_data(city)
    parse_data(data)







if __name__ == "__main__":
    main()



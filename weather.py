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
    # day1
    print('Day 1')
    for x in range (-1,7):
        day1times = data['list'][x]['dt_txt']
        day1temp = data['list'][x]['main']['temp']
        # day1desc = data['list'][x]['weather']['main']
        day1wind = data['list'][x]['wind']['speed']

        print(f'Date: {day1times} | Temp: {day1temp} F  | Wind: {day1wind} MPH')
    print('')
    print('Day 2')
    for x in range (7,15):
            day2times = data['list'][x]['dt_txt']
            day2temp = data['list'][x]['main']['temp']
            # day1desc = data['list'][x]['weather']['main']
            day2wind = data['list'][x]['wind']['speed']

            print(f'Date: {day2times} | Temp: {day2temp} F  | Wind: {day2wind} MPH')
    print('')
    print('Day 3')
    for x in range (15,23):
            day3times = data['list'][x]['dt_txt']
            day3temp = data['list'][x]['main']['temp']
            # day1desc = data['list'][x]['weather']['main']
            day3wind = data['list'][x]['wind']['speed']

            print(f'Date: {day3times} | Temp: {day3temp} F  | Wind: {day3wind} MPH')
    print('')
    print('Day 4')
    for x in range (23,31):
            day4times = data['list'][x]['dt_txt']
            day4temp = data['list'][x]['main']['temp']
            # day1desc = data['list'][x]['weather']['main']
            day4wind = data['list'][x]['wind']['speed']

            print(f'Date: {day4times} | Temp: {day4temp} F  | Wind: {day4wind} MPH')
    print('')
    print('Day 5')
    for x in range (31,39):
            day5times = data['list'][x]['dt_txt']
            day5temp = data['list'][x]['main']['temp']
            # day1desc = data['list'][x]['weather']['main']
            day5wind = data['list'][x]['wind']['speed']

            print(f'Date: {day5times} | Temp: {day5temp} F  | Wind: {day5wind} MPH')        
def main():

    city = get_city()
    data = get_data(city)
    parse_data(data)







if __name__ == "__main__":
    main()



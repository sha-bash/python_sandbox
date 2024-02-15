import requests
import time

def find_uk_city(coordinates: list) -> str:
    
    URL = 'https://geocode.maps.co/reverse?'

    UK_CITIES = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    
    for lat, lon in coordinates:
        params = {'lat': lat, 'lon': lon}
        result = requests.get(URL, params=params).json()
        time.sleep(15)
        if result['address']['city'] in UK_CITIES:
            return result['address']['city']
    return 'no_city'


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
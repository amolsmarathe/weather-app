import requests
import requests_cache

FLUSH_PERIOD = 10 * 60  # 10 minutes in seconds
requests_cache.install_cache(expire_after=FLUSH_PERIOD)


def get_ip():
    base_url_ip = 'https://api.ipify.org'
    return requests.get(base_url_ip).text


def get_geo(ip):
    response_geo = requests.get(f'http://ip-api.com/json/{ip}', headers={'User-Agent': 'amol_weather_app'}).json()
    geo_info = ('lat', 'lon', 'city', 'country')
    return {info: response_geo[info] for info in geo_info}


def get_weather(lat, lon):
    base_url_weather = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
    response_weather = requests.get(base_url_weather, params={'lat':lat, 'lon':lon}).json()
    return response_weather['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']

def convert_to_fr(temp_C):
    return 9 / 5 * temp_C + 32

def greet(ip):    # we pass ip address instead of using get_ip()
    # ip = get_ip()    # we directly pass ip
    geo_info = get_geo(ip)
    temp = get_weather(geo_info['lat'], geo_info['lon'])
    return f'It is {temp} degree celsius right now at your location: {geo_info["city"]}, {geo_info["country"]}'


if __name__ == '__main__':
    import sys
    
    print(greet(sys.argv[1]))    # WHAT IS THE REASON FOR THIS sys.argv[1]?? WHAT ARE WE PASSING TO greet() HERE???

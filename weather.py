"""source:
   https://code.google.com/p/python-weather-api/wiki/Examples#Weather.com
"""

import pywapi
import DHT

def get_weather():
    home_hum, home_temp = DHT.readDHTvalues()

    weather = pywapi.get_weather_from_weather_com('BS3:4:UK')
    out_feel = weather['current_conditions']['feels_like']
    out_conditions = weather['current_conditions']['text'].lower()

    weather_dict = {
        'home_hum' : home_hum,
        'home_temp' : home_temp,
        'out_conditions' : out_conditions,
        'out_feel' : out_feel
        }

    return weather_dict
    
def main():
    weather = get_weather()
    print "Home: {0:0.1f} C and {1:0.1f}%".format(weather['home_temp'], weather['home_hum'])
    print "It's %s and feels %d outside" %(weather['out_conditions'], int(weather['out_feel']))

if __name__ == '__main__':
    main()

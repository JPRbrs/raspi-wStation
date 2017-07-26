#!/usr/bin/env python2.7

"""
source:
https://code.google.com/p/python-weather-api/wiki/Examples#Weather.com
"""

import pywapi
# TODO add address to secrets


def get_weather():
    """
    Returns a dict with two keys: out_feel and out_conditions
    """
    retval = {}

    weather = pywapi.get_weather_from_weather_com('BS16:4:UK')

    retval['out_feel'] = weather['current_conditions']['feels_like']
    retval['out_conditions'] = weather['current_conditions']['text'].lower()

    return retval


def main():
    weather = get_weather()

    print "{} and feels {} outside".format(
        str(weather['out_conditions']),
        str(weather['out_feel'])
    )


if __name__ == '__main__':
    main()

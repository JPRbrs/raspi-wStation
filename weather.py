#!/usr/bin/env python2.7

"""
source:
https://code.google.com/p/python-weather-api/wiki/Examples#Weather.com
"""

from datetime import (
    datetime,
    timedelta,
)

import pywapi

from secrets import post_code


def get_weather():
    """
    Returns a dict with the weather info to stored in the database
    """
    weather = pywapi.get_weather_from_weather_com(post_code)
    curr_cond = weather['current_conditions']

    ret_dict = {
        'date': datetime.now().strftime('%A %d %B'),
        'feels_like': int(curr_cond['feels_like']),
        'out_temperature': int(curr_cond['temperature']),
        'out_humidity': int(curr_cond['humidity']),
        'uv_index': int(curr_cond['uv']['index']),
        'wind_direction': curr_cond['wind']['text'],
        'wind_speed': int(curr_cond['wind']['speed']),
        'out_conditions': curr_cond['text'].lower(),
    }

    return ret_dict


def get_forecast(days_from_today):
    """
    Returns tomorrows weather conditions a numbers of days after today
    equal to the passed parameter
    """
    if days_from_today not in (1, 2, 3):
        raise ValueError('Days_From_Today must be 1, 2 or 3')

    weather = pywapi.get_weather_from_weather_com('BS16:4:UK')
    forecast = weather['forecasts'][days_from_today]

    ret_dict = {
        'date': (datetime.now() + timedelta(days=1)).strftime('%A %d %B'),
        'high': forecast['high'],
        'low': forecast['low'],
        'sunrise': forecast['sunrise'],
        'sunset': forecast['sunset'],
        'day_text': forecast['day']['text'],
        'day_humidity': forecast['day']['humidity'],
        'day_precip': forecast['day']['chance_precip'],
        'day_wind': forecast['day']['wind']['gust'],
        'night_text': forecast['night']['text'],
        'night_humidity': forecast['night']['humidity'],
        'night_precip': forecast['night']['chance_precip'],
        'night_wind': forecast['night']['wind']['gust']
    }
    return ret_dict

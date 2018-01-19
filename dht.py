#!/usr/bin/env python2.7
"""
Requests the DHT data (temperature and humidity) and returns a dictionary with those values
plus a timestamp to be stored in the database
"""
from Adafruit_DHT import read_retry, DHT22
import time

sensor = DHT22
pin = 11

def get_temp_and_hum():
    h,t = read_retry(sensor, pin)
    return round(t,1) ,round(h,1)

def requestData():
# Returns a dictionary with all the data corresponding to a db entry (an Instant)
    h,t = read_retry(sensor, pin)
    current_time = time.strftime("%d.%m.%Y.%H.%M").split('.')

    values = {}
    values['temp'], values['hum'] = get_temp_and_hum()
    values['day'] = current_time[0]
    values['month'] = current_time[1]
    values['year'] = current_time[2]
    values['hour'] = current_time[3]
    values['minute'] = current_time[4]

    return values

if __name__ == "__main__":
    print requestData()
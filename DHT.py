#!/usr/bin/python

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22
pin = 11

def readDHTvalues():
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    return (humidity, temperature)

def requestData():
# Returns a dictionary with all the data corresponding to a db enrty (an Instant)
	import sqlite3 as lite
	import sys
	import re
	
	months = {
		'Jan' : 1,
		'Feb' : 2,
		'Mar' : 3,
		'Apr' : 4,
		'May' : 5,
		'Jun' : 6,
		'Jul' : 7,
		'Aug' : 8,
		'Sep' : 9,
		'Oct' : 10,
		'Nov' : 11,
		'Dec' : 12
	}

	h,t =readDHTvalues()
	line = 'T={0:0.1f}, H={1:0.1f}'.format(t, h)
	line = line +time.strftime(", %d-%b-%Y, %H.%M.%S")

        # temp, hum, day, month, year, hour, minute
	pattern = "T=(\d+\.\d),\ H=(\d+.\d),\ (\d+)-(\w{3})-(\d{4}),\ (\d+).(\d+).\d+"
	result = re.search(pattern, line)

	values = {}
        values['temp'] = result.group(1)
        values['hum'] = result.group(2)
        values['day'] = result.group(3)
        values['month'] = months[result.group(4)]
        values['year'] = result.group(5)
        values['hour'] = result.group(6)
        values['minute'] = result.group(7)

        return values

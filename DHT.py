#!/usr/bin/python

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT22
pin = 11

def main():
    h,t =readDHTvalues()
    line = 'T={0:0.1f}, H={1:0.1f}'.format(t, h)
    line = line +time.strftime(", %d-%b-%Y, %H.%M.%S")
    print line
    
def readDHTvalues():
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    return (humidity, temperature)

if __name__ == '__main__':
    main()

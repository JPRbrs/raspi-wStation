"""
Requests temperature and humidity from DHT sensor

"""
try:
    from Adafruit_DHT import (
        read_retry,
        DHT22
    )
    sensor = DHT22
    pin = 11

except ImportError:
    print('Not running on the pi, some features won\'t be available')


def get_hum_and_temp():
    h, t = read_retry(sensor, pin)
    return round(h, 1), round(t, 1)

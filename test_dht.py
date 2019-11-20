from Adafruit_DHT import (
        read_retry,
        DHT22
)

sensor = DHT22
pin = 11
humidity, temperature = read_retry(sensor, pin)
print("{0:0.1f} C and {1:0.1f}%".format(temperature, humidity))

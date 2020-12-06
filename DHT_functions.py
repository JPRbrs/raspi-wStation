from Adafruit_DHT import read_retry, DHT22

SENSOR = DHT22
PIN = 11
TEMPLATE = '{0}{{component="{1}"}} {2}'


def get_conditions_for_lcd():
    humidity, temperature = read_retry(SENSOR, PIN)
    return str(int(temperature)) + "C and " + str(int(humidity)) + "%"


def get_conditions_for_node_exporter():
    humidity, temperature = read_retry(SENSOR, PIN)
    temp_metric = TEMPLATE.format("pantalones", "temperature", temperature)
    hum_metric = TEMPLATE.format("pantalones", "humidity", humidity)

    print(temp_metric + "\n" + hum_metric)

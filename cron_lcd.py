#!/usr/bin/python
from datetime import datetime
from dht import requestData
import weather
from lcd import LCD
from time import sleep


def main():
    home_conditions = requestData()
    time = datetime.now().strftime('%H:%M')
    weather_dict = weather.get_weather()
    line1 = "{0:0.1f} C and {1:0.1f}%".format(
        home_conditions['temp'],
        home_conditions['hum']
    )
    line2 = time + " Feels %d" % (
        int(weather_dict['out_feel'])
    )
    try:
        lcd = LCD()
        sleep(0.5)
        lcd.send_text(line1, 1)
        lcd.send_text(line2, 2)
    except Exception, e:
        print e
        lcd._clean_up()
        quit()
    except KeyboardInterrupt:
        print 'User interrupted'
        lcd._clean_up()
        quit()

if __name__ == '__main__':
    main()

#!/usr/bin/python

import DHT
import time
import weather
import commands
import RPi.GPIO as GPIO
from LCD_library import LCD

def main():
    GPIO.setwarnings(False)
    lcd=LCD()
    while(True):
        try:
            weather_dict = weather.get_weather()
            line1 = "{0:0.1f} C and {1:0.1f}%".format(weather_dict['home_temp'], weather_dict['home_hum'])
            line2 = "Outside feels %d" % (int(weather_dict['out_feel']))
            line3 = weather_dict['out_conditions'][:16]
        
            lcd.sendText(1, line1)
            lcd.sendText(2, line2)
            time.sleep(10)
            lcd.sendText(1, line1)
            lcd.sendText(2, line3)
            time.sleep(10)
        except Exception,e:
            print e
            lcd._cleanUp()
            quit()
        except KeyboardInterrupt:
            print 'User interrupted'
            lcd._cleanUp()
            print "clean"
            quit()

if __name__ == '__main__':
    main()

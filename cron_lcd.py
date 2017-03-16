#!/usr/bin/env python2.7
"""
script to feed the LCD from a cronjob
"""
from datetime import datetime
import commands
import DHT
import weather
import LCD as LCD

def main():
    lcd=LCD.LCD()
    lcd.blight(1)
    try:
        home_conditions = DHT.requestData()
        time = datetime.now().strftime('%H:%M')
        weather_dict = weather.get_weather()


        line1 = "{0:0.1f} C and {1:0.1f}%".format(
            home_conditions['temp'],
            home_conditions['hum']
        )

        line2 = time + " Feels %d" % (
            int(weather_dict['out_feel'])
        )

        lcd.sendText(1, line1)
        lcd.sendText(2, line2)
    except Exception,e:
        print e
        lcd._cleanUp()
        quit()
    except KeyboardInterrupt:
        print 'User interrupted'
        lcd._cleanUp()
        quit()

if __name__ == '__main__':
    main()


"""OTHER EXAMPLES
    lcd.blight(True)
    coreTemp = commands.getoutput('vcgencmd measure_temp')
    coreTemp = commands.getoutput('vcgencmd measure_temp')
    gpuMem = commands.getoutput('vcgencmd get_mem gpu')
    roomHumid, roomTemp = DHT.readDHTvalues()

    text = "dancing text    "
    lcd.sendText(1,text)
    lcd.move(5, text)
    time.sleep(2)
"""

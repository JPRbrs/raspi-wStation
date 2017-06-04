#!/usr/bin/python
"""
script to feed the LCD from a cronjob
"""
from datetime import datetime
import DHT
import weather
from lcd import LCD


def main():
    lcd = LCD()
    lcd.blight(1)
    try:
        home_conditions = DHT.requestData()
        time = datetime.now().strftime('%H:%M')
        weather_dict = weather.get_weather()
        import pdb; pdb.set_trace()
        line1 = "{0:0.1f} C and {1:0.1f}%".format(
            home_conditions['temp'],
            home_conditions['hum']
        )

        line2 = time + " Feels %d" % (
            int(weather_dict['out_feel'])
        )
        
        lcd.sendText(line1, 1)
        lcd.sendText(line2, 2)
    except Exception, e:
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

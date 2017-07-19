#!/usr/bin/python
from datetime import datetime
import DHT
import weather
from lcd import LCD
from time import sleep
from buses import get_next_bus
from secrets import portcullis


def main():
    home_conditions = DHT.requestData()
    time = datetime.now().strftime('%H:%M')
    weather_dict = weather.get_weather()
    buses = get_next_bus(portcullis, 2)
    line1 = "{0:0.1f} C and {1:0.1f}%".format(
        home_conditions['temp'],
        home_conditions['hum']
    )
    line2 = time + " Feels %d" % (
        int(weather_dict['out_feel'])
    )
    line3 = '{}: {}'.format(buses[0][0], buses[0][1])
    line4 = '{}: {}'.format(buses[1][0], buses[1][1])

    try:
        lcd = LCD()
        sleep(0.5)
        lcd.send_text(line1, 1)
        lcd.send_text(line2, 2)
        sleep(15)
        lcd.send_text(time, 1)
        lcd.send_text(line3, 2)
        sleep(15)
        lcd.send_text(line1, 1)
        lcd.send_text(line2, 2)
        sleep(15)
        lcd.send_text(time, 1)
        lcd.send_text(line4, 2)
        sleep(15)
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

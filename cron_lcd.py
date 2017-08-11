#!/usr/bin/python
from datetime import datetime
import DHT
import weather
from lcd import LCD
from time import sleep
from buses import get_next_bus
from secrets import portcullis


def get_time():
    return datetime.now().strftime("%H:%M")


def check_time_within_range(start_hour, end_hour):
    return (
        int(datetime.now().strftime("%H")) >= start_hour and
        int(datetime.now().strftime("%H")) <= end_hour
    )


def check_line_length(line):
    def func_wrapper():
        """ Check line is no longer than 16 chars
        """
        print line
        print type(line)
        if len(line >= 16):
            return False
        return line
    return func_wrapper


# @check_line_lenght
def get_home_conditions():
    """
    Returns a line ready for the LCD with
    home conditions
    """
    home_conditions = DHT.requestData()
    return "{0:0.1f} C and {1:0.1f}%".format(
        home_conditions["temp"],
        home_conditions["hum"]
    )


# @check_line_lenght
def get_weather():
    """
    Returns a line ready for the LCD with
    outside weather conditions
    """
    weather_dict = weather.get_weather()
    return "It feels {}".format(weather_dict['out_feel'])


# @check_line_lenght
def get_buses():
    """
    Returns a line ready fro the LCD with
    the following two buses
    """
    buses = get_next_bus(portcullis, 2)
    return "{}: {}  {}: {}".format(
        buses[0][0],
        buses[0][1],
        buses[1][0],
        buses[1][1]
    )


def main():
    try:
        lcd = LCD()
        lcd.send_text(get_home_conditions(), 1)
        lcd.send_text(get_weather(), 2)
        # sleep(30)
        # lcd.send_text(get_buses(), 2)
        # sleep(30)
    except Exception, e:
        print e
        lcd._clean_up()
        quit()
    except KeyboardInterrupt:
        print "User interrupted"
        lcd._clean_up()
        quit()


if __name__ == "__main__":
    main()


"""OTHER EXAMPLES
    lcd.blight(True)
    coreTemp = commands.getoutput("vcgencmd measure_temp")
    coreTemp = commands.getoutput("vcgencmd measure_temp")
    gpuMem = commands.getoutput("vcgencmd get_mem gpu")
    roomHumid, roomTemp = DHT.readDHTvalues()

    text = "dancing text    "
    lcd.sendText(1,text)
    lcd.move(5, text)
    time.sleep(2)
"""

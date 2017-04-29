from LCD import LCD
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2) or (sys.argv[1] not in ('0', '1')):
        print "Usage: sudo python LCD command where:"
        print "command = 1  on"
        print "command = 0 off"
        quit()

    lcd = LCD()
    if sys.argv[1] == '0':
        lcd._cleanUp()
    else:
        lcd.blight(1)

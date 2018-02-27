#!/usr/bin/python
from lcd import LCD


def main():
    try:
        lcd = LCD()
        lcd.blight(0)
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

from lcd import LCD
import sys


def enable_backlight():
    lcd.blight(1)


def disable_backlight():
    lcd._cleanUp()


def display_text():
    if sys.argv[2]:
        lcd.sendText(sys.argv[2])
    else:
        print "Error: text required"
        quit()


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "Usage: sudo python lcd_service [on/off] [display text]"
        quit()

    actions = {
        'on':   enable_backlight,
        'off':  disable_backlight,
        'text': display_text,
    }
    
    if sys.argv[1] not in actions.keys():
        print "Available options: on, off, text"
        quit()

    lcd = LCD()
    actions[sys.argv[1]]()

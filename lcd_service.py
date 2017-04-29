from lcd import LCD
import sys


def enable_backlight():
    lcd.blight(1)


def disable_backlight():
    lcd._cleanUp()


def display_message():
    if not sys.argv[2]:
        print "Error: text required"
        quit()
    message = sys.argv[2]
    message_length = len(str(sys.argv[2]))
    print ("printing {}...".format(sys.argv[2]))

    enable_backlight()

    if message_length > 0 and message_length < 16:
        lcd.sendText(message)
    elif message_length > 16 and message_length < 31:
        lcd.sendText(message[0:15], 1)
        lcd.sendText(message[15:len(message)], 2)
    else:
        print("message too long, consider texting her")
        quit()


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print "Usage: sudo python lcd_service [on/off] [display text]"
        quit()

    actions = {
        'on':   enable_backlight,
        'off':  disable_backlight,
        'text': display_message,
    }

    if sys.argv[1] not in actions.keys():
        print "Available options: on, off, text"
        quit()

    lcd = LCD()
    actions[sys.argv[1]]()

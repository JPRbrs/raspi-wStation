#!/usr/bin/python
#
# HD44780 LCD Test Script for
# Raspberry Pi
#
# Author : Matt Hawkins
# Site   : http://www.raspberrypi-spy.co.uk
#
# Date   : 03/08/2012
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

# Code was modified to use it as a library

import time
import RPi.GPIO as GPIO

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
LED_ON = 15

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

# LCD RAM address for the 2 lines
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005


class LCD:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)        # Use BCM GPIO numbers
        GPIO.setup(LCD_E, GPIO.OUT)   # E
        GPIO.setup(LCD_RS, GPIO.OUT)  # RS
        GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
        GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
        GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
        GPIO.setup(LCD_D7, GPIO.OUT)  # DB7
        GPIO.setup(LED_ON, GPIO.OUT)  # Backlight enable

        # Initialise display
        self._lcd_byte(0x33, LCD_CMD)
        self._lcd_byte(0x32, LCD_CMD)
        self._lcd_byte(0x28, LCD_CMD)
        self._lcd_byte(0x0C, LCD_CMD)
        self._lcd_byte(0x06, LCD_CMD)
        self._lcd_byte(0x01, LCD_CMD)
        self.blight(0)

    def _cleanUp(self):
        GPIO.cleanup()

    def _lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = data
        # mode = True  for character
        #        False for command

        GPIO.output(LCD_RS, mode)  # RS

        # High bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits & 0x10 == 0x10:
            GPIO.output(LCD_D4, True)
        if bits & 0x20 == 0x20:
            GPIO.output(LCD_D5, True)
        if bits & 0x40 == 0x40:
            GPIO.output(LCD_D6, True)
        if bits & 0x80 == 0x80:
            GPIO.output(LCD_D7, True)

        # Toggle 'Enable' pin
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, True)
        time.sleep(E_PULSE)
        GPIO.output(LCD_E, False)
        time.sleep(E_DELAY)

        # Low bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits & 0x01 == 0x01:
            GPIO.output(LCD_D4, True)
        if bits & 0x02 == 0x02:
            GPIO.output(LCD_D5, True)
        if bits & 0x04 == 0x04:
            GPIO.output(LCD_D6, True)
        if bits & 0x08 == 0x08:
            GPIO.output(LCD_D7, True)

        # Toggle 'Enable' pin
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, True)
        time.sleep(E_PULSE)
        GPIO.output(LCD_E, False)
        time.sleep(E_DELAY)

    def _displace(self, text):
        # takes a 16 char string and formats it to show it in movement
        if len(text) > 16:
            print ('String cannot be longer than 16 characters')
            return

        ret = []
        text = list(text)

        for x in range(1, 16):
            ret.append(text[x])
        ret.append(text[0])
        ret = ''.join(ret)
        return ret

    def _lcd_string(self, message, style):
        # Send string to display
        if style == 1:
            message = message.ljust(LCD_WIDTH, " ")
        elif style == 2:
            message = message.center(LCD_WIDTH, " ")
        elif style == 3:
            message = message.rjust(LCD_WIDTH, " ")

        for i in range(LCD_WIDTH):
            self._lcd_byte(ord(message[i]), LCD_CHR)

    def sendText(self, text, row=1, justification=2):
        # ROW: send 'text' to row number 1 or 2
        # Justification: left(1), center(2), (3)right
        if (len(text) > 16):
            print "Text not valid. Longer than 16 characters"
            text = 'ERR:line too long'
        rows = {
            1: LCD_LINE_1,
            2: LCD_LINE_2
        }
        self._lcd_byte(rows[row], LCD_CMD)
        self._lcd_string(text, justification)

    def blight(self, state):
        # Toggle backlight on (state = true) or of (state=false)
        GPIO.output(LED_ON, state)

    def move(self, seconds, text):
        for x in range(seconds*2):
            self.sendText(text, 1)
            time.sleep(0.5)
            text = self._displace(text)

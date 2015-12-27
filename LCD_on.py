#!/usr/bin/python

import RPi.GPIO as GPIO
from LCD_library import LCD

def main():
    lcd = LCD()
    lcd.blight(1)	

if __name__ == '__main__':
    main()

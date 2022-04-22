import drivers
from time import sleep
from datetime import datetime

display = drivers.Lcd()

def clearLcd():
    display.lcd_clear()

def printtoLcd(message):
    clearLcd()
    print("Displaying " + message)
    display.lcd_display_string(message, 1)
    display.lcd_display_string("Recycled: ", 2)
    display.lcd_display_string("Cans| 0 Bottles| 0 ", 3)
    display.lcd_display_string("Sauce it Up", 4)
    


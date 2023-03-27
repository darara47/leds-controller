from machine import Pin, PWM
from time import sleep

ledR = PWM(Pin(19))
ledG = PWM(Pin(18))
ledB = PWM(Pin(20))
ledR.freq(1000)
ledG.freq(1000)
ledB.freq(1000)

def setLeds(color, brightness=1):
    red = color[0]
    green = color[1]
    blue = color[2]
    error = False
    
    if (red > 255 or red < 0):
        print('Red is out of range! red = ' + str(red))
        error = True
    if (green > 255 or green < 0):
        print('Green is out of range! green = ' + str(green))
        error = True
    if (blue > 255 or blue < 0):
        print('Blue is out of range! blue = ' + str(blue))
        error = True
    if (brightness > 1 or brightness < 0):
        print('Brightness is out of range! brightness = ' + str(brightness))
        error = True
    
#     print('red = ' + str(red) + '\ngreen = ' + str(green) + '\nblue = ' + str(blue))
    if (error == False):
        # max value is 65535
        ledR.duty_u16(red * 257 * brightness)
        ledG.duty_u16(green * 257 * brightness)
        ledB.duty_u16(blue * 257 * brightness)

def twoColorsFilling(mainColor, newColor, filling):
    red = round(mainColor[0] + (newColor[0] - mainColor[0]) * filling);
    green = round(mainColor[1] + (newColor[1] - mainColor[1]) * filling);
    blue = round(mainColor[2] + (newColor[2] - mainColor[2]) * filling);
    setLeds((red, green, blue))

    

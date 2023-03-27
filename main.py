from neopixel import Neopixel
from colors import colors
from ledsBed import setLeds
from microphone import microphone
import animations
import random


numpix = 300
strip = Neopixel(numpix, 0, 28, "GRB")

type = 'calm'
# type = 'party'

if (type == 'calm'):
    timesleep = 0.06
    breaktime = 0.1
    partLength = 50
    _colors = colors['allBasic']
    continuation = False
    continuousColorIndex = 0
    withBed = True
       
    while(True):
        animationsType = random.randint(0, 4)
#         print(animationsType)
        animationsType = 6
        if (animationsType == 0):
            continuousColorIndex = animations.frontalHit(strip, numpix, 70, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 1):
            continuousColorIndex = animations.backalHit(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 2):
            continuousColorIndex = animations.randomCompletion(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 3):
            continuousColorIndex = animations.allFilling(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 4):
            continuousColorIndex = animations.musicDetection(strip, numpix, 100, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 5):
            continuousColorIndex = animations.musicDetectionSyn(strip, numpix, 80, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 6):
            continuousColorIndex = animations.musicDetectionSyn2(strip, numpix, 80, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 7):
            continuousColorIndex = animations.musicDetectionSyn3(strip, numpix, 80, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 8):
            continuousColorIndex = animations.musicDetectionSyn(strip, numpix, 80, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)

elif(type == 'party'):
    timesleep = 0.004
    breaktime = 0
    partLength = 50
    _colors = colors['allBasic']
    continuation = False
    continuousColorIndex = None
    withBed = True
       
    while(True):
        animationsType = random.randint(0, 3)
        if (animationsType == 0):
            animations.frontalHit(strip, numpix, 70, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 1):
            animations.backalHit(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 2):
            animations.randomCompletion(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)
        if (animationsType == 3):
            animations.allFilling(strip, numpix, 50, timesleep, breaktime, partLength, _colors, continuation, continuousColorIndex, withBed)


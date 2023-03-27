import utime
import machine
import math
import random
import ledsBed

random.seed()

def __getRandomColorsIndexes(newColorIndex, colors, continuousType):
    if (continuousType == False):
        newColorIndex = random.randint(0, len(colors) - 1)
        
    mainColorIndex = newColorIndex
    
    if (len(colors) >= 4):
        indexesDifference = abs(mainColorIndex - newColorIndex)
        while (indexesDifference <= 1 or indexesDifference >= len(colors) - 1):
            newColorIndex = random.randint(0, len(colors) - 1)
            indexesDifference = abs(mainColorIndex - newColorIndex)
    else:
        while mainColorIndex == newColorIndex:
            newColorIndex = random.randint(0, len(colors) - 1)
    
    return mainColorIndex, newColorIndex

def rainbow(strip, numpix, brightness, timesleep, colors, continuation):
    colorsNumber = len(colors)
    step = round(numpix / colorsNumber)
    current_pixel = 0
    strip.brightness(brightness)

    for i in range(colorsNumber):
        strip.set_pixel_line_gradient(current_pixel, min(current_pixel + step, 299), colors[i], colors[(i + 1) % colorsNumber])
        current_pixel += step
        
    strip.show()

    while continuation:
        strip.rotate_right(1)
        utime.sleep(timesleep)
        strip.show()

def frontalHit(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        newColorIndex = random.randint(0, len(colors) - 1)
        if (continuousColorIndex is not None):
            newColorIndex = continuousColorIndex
        
        loop = True
        while loop:
            mainColorIndex, newColorIndex = __getRandomColorsIndexes(newColorIndex, colors, continuousColorIndex != None)
            
            strip.set_all(colors[mainColorIndex], brightness)
            strip.show()
            
            movingIndexRange = round(partLength / 2) + 1
            for movingIndex in range(movingIndexRange):
                for repeatability in range(math.ceil(numpix / partLength) + 1):
                    index1 = repeatability * partLength - movingIndex
                    index2 = repeatability * partLength + movingIndex
                    if (index1 >= 0 and index1 < numpix):
                        strip.set_pixel(index1, colors[newColorIndex], brightness)
                    if (index2 >= 0 and index2 < numpix):
                        strip.set_pixel(index2, colors[newColorIndex], brightness)
                        
                strip.show()
                if (withBed):
                    ledsBed.twoColorsFilling(colors[mainColorIndex], colors[newColorIndex], movingIndex / movingIndexRange)
                
                utime.sleep(timesleep)
            if (breaktime > 0):
                utime.sleep(breaktime)
            
            loop = continuation
        return newColorIndex

def backalHit(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        newColorIndex = random.randint(0, len(colors) - 1)
        if (continuousColorIndex is not None):
            newColorIndex = continuousColorIndex
        
        loop = True
        while loop:
            mainColorIndex, newColorIndex = __getRandomColorsIndexes(newColorIndex, colors, continuousColorIndex != None)
            
            strip.set_all(colors[mainColorIndex], brightness)
            strip.show()
            
            movingIndexRange = partLength
            for movingIndex in range(movingIndexRange):
                for repeatability in range(math.ceil(numpix / partLength)):
                    index = repeatability * partLength + movingIndex
                    if (index < numpix):
                        strip.set_pixel(index, colors[newColorIndex], brightness)
                        
                strip.show()
                if (withBed):
                    ledsBed.twoColorsFilling(colors[mainColorIndex], colors[newColorIndex], movingIndex / movingIndexRange)
                
                utime.sleep(timesleep)
            if (breaktime > 0):
                utime.sleep(breaktime)
            
            loop = continuation
        return newColorIndex

def randomCompletion(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        newColorIndex = random.randint(0, len(colors) - 1)
        if (continuousColorIndex is not None):
            newColorIndex = continuousColorIndex
        
        loop = True
        while loop:
            mainColorIndex, newColorIndex = __getRandomColorsIndexes(newColorIndex, colors, continuousColorIndex != None)
            
            strip.set_all(colors[mainColorIndex], brightness)
            strip.show()
            
            for i in range(numpix):
                pixelIndex = random.randint(0, numpix - 1)
                while(strip.pixelsValue[pixelIndex] != tuple([round(color * (brightness / 100)) for color in colors[mainColorIndex]])):
                    pixelIndex = random.randint(0, numpix - 1)
                
                strip.set_pixel(pixelIndex, colors[newColorIndex], brightness)
                
                if (i % math.ceil(numpix / partLength) == 0 or i == numpix - 1):
                    strip.show()
                    if (withBed):
                        ledsBed.twoColorsFilling(colors[mainColorIndex], colors[newColorIndex], (i + 1) / numpix)
                    
                    utime.sleep(timesleep)
            if (breaktime > 0):
                utime.sleep(breaktime)
            
            loop = continuation
        return newColorIndex

def allFilling(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        newColorIndex = random.randint(0, len(colors) - 1)
        if (continuousColorIndex is not None):
            newColorIndex = continuousColorIndex
        
        loop = True
        while loop:
            mainColorIndex, newColorIndex = __getRandomColorsIndexes(newColorIndex, colors, continuousColorIndex != None)
            
            strip.set_all(colors[mainColorIndex], brightness)
            strip.show()
            
            movingIndexRange = partLength
            for movingIndex in range(movingIndexRange):
                filling = movingIndex / movingIndexRange
                red = round(colors[mainColorIndex][0] + (colors[newColorIndex][0] - colors[mainColorIndex][0]) * filling);
                green = round(colors[mainColorIndex][1] + (colors[newColorIndex][1] - colors[mainColorIndex][1]) * filling);
                blue = round(colors[mainColorIndex][2] + (colors[newColorIndex][2] - colors[mainColorIndex][2]) * filling);
                
                strip.set_all((red, green, blue), brightness)
                strip.show()
                if (withBed):
                    ledsBed.twoColorsFilling(colors[mainColorIndex], colors[newColorIndex], filling)
                
                utime.sleep(timesleep)
            if (breaktime > 0):
                utime.sleep(breaktime)
            
            loop = continuation
        return newColorIndex

def musicDetection(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        
        mic = machine.ADC(26)
        potentiometer = machine.ADC(27)
        iteration = 0
        avgMicValue = 0
        maxValue = 0
        limit = 0
        isActiveTrigger = 0
        triggerTime = 0
        
        pixels = [[0, 0, 0, brightness] for i in range(numpix)]

        mainColorIndex = 3
        newColorIndex = 1
        
        for index in range(numpix):
            pixels[index] = colors[mainColorIndex]
            strip.set_pixel(index, colors[mainColorIndex], brightness)
        
        strip.show()
        
        loop = True
        while loop:
            micValue = mic.read_u16()
            potentiometerValue = potentiometer.read_u16()
            limit = round(potentiometerValue / 4) + 1000
            avgMicValue = (avgMicValue * iteration + micValue) / (iteration + 1)
            
            if (abs(avgMicValue - micValue) > limit):
                if (triggerTime == 0):
                    isActiveTrigger = 10
                    triggerTime = iteration
#                     print("TRIGGER: ", limit)
            
            if (triggerTime != 0 and iteration - triggerTime > 200):
                triggerTime = 0
            
            
            if (iteration % 10 == 0):
                for index in range(numpix / 2 - 1):
                    if (pixels[index] != pixels[index + 1]):
                        pixels[index] = pixels[index + 1]
                        strip.set_pixel(index, pixels[index + 1], brightness)
                    if (pixels[numpix - 1 - index] != pixels[numpix - 1 - index - 1]):
                        pixels[numpix - 1 - index] = pixels[numpix - 1 - index - 1]
                        strip.set_pixel(numpix - 1 - index, pixels[numpix - 1 - index - 1], brightness)
                if (isActiveTrigger > 0):
                    if (pixels[round(numpix / 2) - 1] != colors[newColorIndex]):
                        pixels[round(numpix / 2) - 1] = colors[newColorIndex]
                        strip.set_pixel(round(numpix / 2) - 1, colors[newColorIndex], brightness)
                    if (pixels[round(numpix / 2)] != colors[newColorIndex]):
                        pixels[round(numpix / 2)] = colors[newColorIndex]
                        strip.set_pixel(round(numpix / 2), colors[newColorIndex], brightness)
                    isActiveTrigger = isActiveTrigger - 1
                else:
                    if (pixels[round(numpix / 2) - 1] != colors[mainColorIndex]):
                        pixels[round(numpix / 2) - 1] = colors[mainColorIndex]
                        strip.set_pixel(round(numpix / 2) - 1, colors[mainColorIndex], brightness)
                    if (pixels[round(numpix / 2)] != colors[mainColorIndex]):
                        pixels[round(numpix / 2)] = colors[mainColorIndex]
                        strip.set_pixel(round(numpix / 2), colors[mainColorIndex], brightness)
                
                strip.show()
            
#                 if (i % 1000 == 0):
#                     print('avgMicValue: ', avgMicValue)
            
#             print(iteration)
            iteration = iteration + 1

def musicDetectionSyn(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        
        mic = machine.ADC(26)
        potentiometer = machine.ADC(27)
        iteration = 0
        avgMicValue = 0
        maxValue = 0
        limit = 0
        isActiveTrigger = 0
        triggerTime = 0
        synValue = 0

        mainColorIndex = 3
        newColorIndex = 1
        
        pixels = [mainColorIndex] * round(numpix / 2 + 1)
        
        ledsBed.setLeds(colors[mainColorIndex], 1)
        for index in range(numpix):
            strip.set_pixel(index, colors[mainColorIndex], brightness)
        
        strip.show()
        
        loop = True
        while loop:
            micValue = mic.read_u16()
            potentiometerValue = potentiometer.read_u16()
            limit = round(potentiometerValue / 60)
            avgMicValue = (avgMicValue * iteration + micValue) / (iteration + 1)
            
            if (micValue > maxValue):
                maxValue = micValue
            
            if (abs(avgMicValue - micValue) > limit):
                synValue = abs(avgMicValue - micValue) - limit
            else:
                synValue = 0
            
            synRange = numpix / 2
            synWidth = synValue / maxValue * synRange
            
            for index in range(synRange):
                if (index < synWidth):
                    if (pixels[index] != newColorIndex):
                        pixels[index] = newColorIndex
                        strip.set_pixel(index, colors[newColorIndex], brightness)
                        strip.set_pixel(numpix - 1 - index, colors[newColorIndex], brightness)
                        strip.set_pixel(round(numpix / 2) + index, colors[newColorIndex], brightness)
                        strip.set_pixel(round(numpix / 2) - 1 - index, colors[newColorIndex], brightness)
                elif (pixels[index + 1] == mainColorIndex):
                    if (pixels[index] != mainColorIndex):
                        pixels[index] = mainColorIndex
                        strip.set_pixel(index, colors[mainColorIndex], brightness)
                        strip.set_pixel(numpix - 1 - index, colors[mainColorIndex], brightness)
                        strip.set_pixel(round(numpix / 2) + index, colors[mainColorIndex], brightness)
                        strip.set_pixel(round(numpix / 2) - 1 - index, colors[mainColorIndex], brightness)

            if (pixels[0] != mainColorIndex):
                strip.show()
            
            iteration = iteration + 1

def musicDetectionSyn2(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        
        mic = machine.ADC(26)
        potentiometer = machine.ADC(27)
        iteration = 0
        avgMicValue = 0
        maxValue = 0
        limit = 0
        isActiveTrigger = 0
        triggerTime = 0
        synValue = 0
        synWidth = 0
        prevSynWidth = 0
        brightnessBackground = 10

        mainColorIndex = 4
        newColorIndex = 2
        
        pixels = [mainColorIndex] * round(numpix / 2 + 1)
        
        ledsBed.setLeds(colors[mainColorIndex], 1)
        strip.set_all(colors[mainColorIndex], brightnessBackground)
        strip.show()
        
        loop = True
        while loop:
            micValue = mic.read_u16()
            potentiometerValue = potentiometer.read_u16()
            limit = round(potentiometerValue / 60)
            avgMicValue = (avgMicValue * iteration + micValue) / (iteration + 1)
            
            if (micValue > maxValue):
                maxValue = micValue
            
            if (abs(avgMicValue - micValue) > limit):
                synValue = abs(avgMicValue - micValue) - limit
            else:
                synValue = 0
            
            synRange = numpix / 4
            prevSynWidth = synWidth
            synWidth = synValue / maxValue * synRange * 1.9
            if (synWidth - prevSynWidth < -1):
                synWidth = prevSynWidth - 1
            
#             synRange = numpix / 2
#             synWidth = synValue / maxValue * synRange
            
            for index in range(synRange):
                if (index < synWidth):
                    if (pixels[index] != newColorIndex):
                        pixels[index] = newColorIndex
                        strip.set_pixel(round(numpix * 3 / 4) + index, colors[newColorIndex], brightness)
                        strip.set_pixel(round(numpix * 3 / 4) - 1 - index, colors[newColorIndex], brightness)
                        strip.set_pixel(round(numpix / 4) + index, colors[newColorIndex], brightness)
                        strip.set_pixel(round(numpix / 4) - 1 - index, colors[newColorIndex], brightness)
                elif (pixels[index] != mainColorIndex):
                    pixels[index] = mainColorIndex
                    strip.set_pixel(round(numpix * 3 / 4) + index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix * 3 / 4) - 1 - index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix / 4) + index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix / 4) - 1 - index, colors[mainColorIndex], brightnessBackground)

            if (pixels[0] != mainColorIndex):
                strip.show()
            
            iteration = iteration + 1
            
def musicDetectionSyn3(strip, numpix, brightness, timesleep, breaktime, partLength, colors, continuation, continuousColorIndex = None, withBed = True):
    
    if (len(colors) <= 1):
        print('Not enough colors')
    else:
        
        mic = machine.ADC(26)
        potentiometer = machine.ADC(27)
        iteration = 0
        avgMicValue = 0
        maxValue = 0
        limit = 0
        isActiveTrigger = 0
        triggerTime = 0
        synValue = 0
        synWidth = 0
        prevSynWidth = 0
        brightnessBackground = 10

        mainColorIndex = 4
        newColorIndex = 1
        
        pixels = [mainColorIndex] * round(numpix / 2 + 1)
        
        ledsBed.setLeds(colors[mainColorIndex], 1)
        strip.set_all(colors[mainColorIndex], brightnessBackground)
        strip.show()
        
        loop = True
        while loop:
            micValue = mic.read_u16()
            potentiometerValue = potentiometer.read_u16()
            limit = round(potentiometerValue / 60)
            avgMicValue = (avgMicValue * iteration + micValue) / (iteration + 1)
            
            if (micValue > maxValue):
                maxValue = micValue
            
            if (abs(avgMicValue - micValue) > limit):
                synValue = abs(avgMicValue - micValue) - limit
            else:
                synValue = 0
            
            synRange = numpix / 4
            prevSynWidth = synWidth
            synWidth = synValue / maxValue * synRange * 1.9
            if (synWidth - prevSynWidth < -1):
                synWidth = prevSynWidth - 1
            
            for index in range(synRange):
                if (index < synWidth):
                    pixels[index] = newColorIndex
                    strip.set_pixel(round(numpix * 3 / 4) + index, (255, round(200 * (1 - index / synWidth)), 0), brightness)
                    strip.set_pixel(round(numpix * 3 / 4) - 1 - index, (255, round(200 * (1 - index / synWidth)), 0), brightness)
                    strip.set_pixel(round(numpix / 4) + index, (255, round(200 * (1 - index / synWidth)), 0), brightness)
                    strip.set_pixel(round(numpix / 4) - 1 - index, (255, round(200 * (1 - index / synWidth)), 0), brightness)
                elif (pixels[index] != mainColorIndex):
                    pixels[index] = mainColorIndex
                    strip.set_pixel(round(numpix * 3 / 4) + index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix * 3 / 4) - 1 - index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix / 4) + index, colors[mainColorIndex], brightnessBackground)
                    strip.set_pixel(round(numpix / 4) - 1 - index, colors[mainColorIndex], brightnessBackground)

            if (pixels[0] != mainColorIndex):
                strip.show()
            
            iteration = iteration + 1
            
import machine
import utime

def microphone(queue):

    mic = machine.ADC(26)
    potentiometer = machine.ADC(27)
    microphoneTrigger = 0

    i = 0
    avgMicValue = 0
    maxValue = 0
    limit = 0
    activeTrigger = 0

    print("START", microphoneTrigger)
    microphoneTrigger = 123
    print("START", microphoneTrigger)
    
    while True:
        micValue = mic.read_u16()
        potentiometerValue = potentiometer.read_u16()
        limit = round(potentiometerValue / 20)
    #     print("micValue: ",micValue)

        avgMicValue = (avgMicValue * i + micValue) / (i + 1)

    #     if (micValue > maxValue):
    #         maxValue = micValue
    #         print("maxValue: ", maxValue)
        
        if (abs(avgMicValue - micValue) > limit):
    #         print("limit: ", limit)
            if (activeTrigger == 0):
                activeTrigger = i
                microphoneTrigger = i
                print("microphoneTrigger: ", microphoneTrigger)
                queue.put(microphoneTrigger)
        
        if (activeTrigger != 0 and i - activeTrigger > 200):
            activeTrigger = 0
        
        
    #     if (i % 1000 == 0):
    #         print('avgMicValue: ', avgMicValue)
        
        i = i + 1
        queue.put(None)
        utime.sleep(0.001)

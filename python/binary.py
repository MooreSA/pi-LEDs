import RPi.GPIO as GPIO
import time
ledPins = [11 , 3, 13, 15, 16, 18, 12, 5, 24, 22]
def setup():
    GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT) # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led

def clearLEDS():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)

def displayLED(binary):
    clearLEDS()
    for index, bit in enumerate(binary):
        if bit == 1:
            GPIO.output(ledPins[-index], GPIO.LOW)
        

def loop():
    maxLength = 2 ** len(ledPins)
    num_bits = len(ledPins)
    for number in range(maxLength):
        binary = [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]
        displayLED(binary)
        time.sleep(0.1)
    destroy()
            

def destroy():
    GPIO.cleanup() # Release all GPIO

if __name__ == '__main__': # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()

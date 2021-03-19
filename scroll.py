import RPi.GPIO as GPIO
import time
ledPins = [11 , 3, 13, 15, 16, 18, 12, 5, 24, 22]
def setup():
    GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT) # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led

def loop():
    while True:
        for pin in ledPins: 
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.1)
            

def destroy():
    GPIO.cleanup() # Release all GPIO

if __name__ == '__main__': # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()

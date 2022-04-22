import RPi.GPIO as GPIO
import time
import motortest
import lcdTest

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 22
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElasped = StopTime - StartTime
    distance = (TimeElasped * 34300 ) / 2

    return distance

if __name__ == '__main__':
    
    try:
        dist = distance()
        while(dist >= 30):
            lcdTest.printtoLcd("Searching.....")
            dist = distance()
            motortest.goForward(0.5)
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)
        motortest.turnRight()
        time.sleep(0.1)
        motortest.stop()
        time.sleep(0.1)
        motortest.turnLeft()
        time.sleep(0.1)
        while(dist <= 60):
            lcdTest.printtoLcd("Returning...")
            dist = distance()
            motortest.goBackward(0.5) 
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)
        lcdTest.printtoLcd("Stop...")
        motortest.stop()
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        lcdTest.printtoLcd("Stop")
        motortest.stop()
        GPIO.cleanup()

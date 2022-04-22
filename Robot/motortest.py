#Simple program to test functionality of motors
#Author Dalton Kinney Group 17
import time
import board
from adafruit_motorkit import MotorKit
#Kit to initialize connection to the board
kit = MotorKit(i2c = board.I2C())
def main():
    goForward()
    goBackward()
    turnLeft()
    turnRight()

def stop():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
#Go Forward
def goForward(speed):
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
#Go Backward
def goBackward(speed):
    kit.motor1.throttle = -speed
    kit.motor2.throttle = -speed
#Turn 90 degrees left
def turnRight():
    kit.motor1.throttle = -0.5
    kit.motor2.throttle = 0.5
    time.sleep(0.9)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
#turn 90 degrees right
def turnLeft():
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.5
    time.sleep(.9)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
#Turn 180 degrees
def turnAround():
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = -0.5
    time.sleep(2)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
#Turn 360 degrees
def spinAround():
    turnAround()
    turnAround()

if __name__ == "__main__":
    main()

"""Simple test for using adafruit_motorkit with a DC motor"""
import time
from adafruit_motorkit import MotorKit
 
kit = MotorKit()
 
kit.motor1.throttle = 1.0           ## set left wheel speed
kit.motor2.throttle = 1.0           ## set right wheel speed
time.sleep(5)
kit.motor1.throttle = 0             ## left wheel stop
kit.motor2.throttle = 0             ## right wheel stop
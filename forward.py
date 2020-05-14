"""Simple test for using adafruit_motorkit with a DC motor"""
import time
from adafruit_motorkit import MotorKit                  
 
kit = MotorKit()                                ## wheel1 =right    ,wheel 2 = left
 
kit.motor1.throttle = 0.5           ## set wheel1 speed
kit.motor2.throttle = 0.5         ## set  wheel2  speed
time.sleep(0.2)
kit.motor1.throttle = 0             ## wheel 1  stop
kit.motor2.throttle = 0             ## wheel 2  stop
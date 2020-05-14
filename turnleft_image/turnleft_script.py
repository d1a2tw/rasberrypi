import os 
import time
from adafruit_motorkit import MotorKit

folder_name="5_14_turnleft"     ## image saved name     =>        "  date +action type"
times=100                                             ## number of image
kit = MotorKit()                                    ## wheel1 =right    ,wheel 2 = left




for i in range (times):
    kit.motor1.throttle = 0.5              ## set wheel1 speed
    kit.motor2.throttle = 0           ## set  wheel 2 speed
    time.sleep(0.2)
    kit.motor1.throttle = 0             ##  wheel1  stop
    kit.motor2.throttle = 0             ##  wheel 2stop
    a="raspistill -o  "
    b=folder_name
    c=str(i)                    # the ith photo
    d=".jpg"
    command=a+b+c+d
    os.system(command)

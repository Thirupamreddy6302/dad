#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()




>>>>>>>>>>>>>>>>>>>>>>>>>>

Measured Distance = 549.5 cm
Measured Distance = 3401.5 cm
Measured Distance = 3401.1 cm
Measured Distance = 3369.6 cm
Measured Distance = 3385.2 cm
Measured Distance = 3355.4 cm
Measured Distance = 3363.0 cm
Measured Distance = 3367.6 cm
Measured Distance = 3373.0 cm
Measured Distance = 3399.7 cm
Measured Distance = 3375.9 cm
Measured Distance = 3406.6 cm
Measured Distance = 3417.5 cm
Measured Distance = 3386.5 cm
Measured Distance = 3385.8 cm
Measured Distance = 3357.1 cm
Measured Distance = 3389.8 cm
Measured Distance = 3356.1 cm
Measured Distance = 3358.6 cm
Measured Distance = 3355.7 cm
Measured Distance = 3387.8 cm
Measured Distance = 3393.5 cm
Measured Distance = 3392.1 cm
Measured Distance = 3370.0 cm
Measured Distance = 3375.8 cm
Measured Distance = 3372.2 cm
Measured Distance = 3389.8 cm
Measured Distance = 3439.7 cm
Measured Distance = 2806.0 cm
Measured Distance = 87.1 cm
Measured Distance = 7.7 cm
Measured Distance = 3389.1 cm



               

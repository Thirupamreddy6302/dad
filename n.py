import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pirPin= 8
GPIO.setup(pirPin, GPIO.IN)
counter=1
time.sleep(4)

while True:
    if GPIO.input(pirPin):
        print("Motion Detected")
        time.sleep(1)
        counter=counter+1
        import os
        os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/Desktop/1.jpg")
        print("pic taken")
    else:
        print("testing")
        
Motion Detected
pic taken
Motion Detected
pic taken
Motion Detected
pic taken
Motion Detected
pic taken
Motion Detected
pic taken
Motion Detected
pic taken
Motion Detected
pic taken

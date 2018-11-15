from gpiozero import DistanceSensor
from time import sleep

sensor=DistanceSensor(echo=18,trigger=17)
while True:
    print("distance: ",sensor.distance * 100)
    sleep(1)



>>>>>>>>>>>>>>>>>
distance:  100.0
distance:  55.01255321502685
distance:  54.382388591766365
distance:  100.0
distance:  100.0
distance:  53.32052028179169
distance:  100.0
distance:  100.0
distance:  100.0
distance:  100.0
distance:  100.0
distance:  100.0
distance:  100.0distance:  0.0
distance:  0.0
distance:  0.0
distance:  0.0

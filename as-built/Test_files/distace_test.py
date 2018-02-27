from gpiozero import LED, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
import time
from signal import pause

remote_factory = PiGPIOFactory(host='172.20.10.11')

led = LED(26)
sensor = DistanceSensor(18, 17, max_distance=1, threshold_distance=0.2)

def init():

    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    led.on()
    time.sleep(1)
    led.off()

#init()
#while True:
#    distance = sensor.distance * 100
#    print("Distance : %.1f" % distance)
#    time.sleep(1)


sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()

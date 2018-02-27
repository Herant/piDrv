from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

remote_factory = PiGPIOFactory(host='192.168.1.130')
led_1 = LED(5, 6)  # local pin
led_2 = LED(13, 19, pin_factory=remote_factory)  # remote pin

while True:
    led_2.off()
    sleep(1)
    led_1.off()
    sleep(1)

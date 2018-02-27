from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory
import csv
import time
import cv2

turn_speed = 0.6
drive_speed = 0.2
remote_factory = PiGPIOFactory(host='192.168.1.130')
motor_1 = Motor(forward=19, backward=13)
motor_2 = Motor(forward=6, backward=5)
drive_forward = motor_1.forward
drive_backward = motor_1.backward
turn_left = motor_2.forward
turn_right = motor_2.backward

turn_left(0)
turn_right(0)
drive_forward(0)

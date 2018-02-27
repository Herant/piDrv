from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory
import csv
import time

turn_speed = 0.5
drive_speed = 0.15
remote_factory = PiGPIOFactory(host='192.168.1.130')
# 19 = FORWARD, 13 = BACKWARD
motor_1 = Motor(forward=19, backward=13)
# 6 = LEFT, 5 = RIGHT
motor_2 = Motor(forward=6, backward=5)
drive_forward = motor_1.forward
drive_backward = motor_1.backward
turn_left = motor_2.forward
turn_right = motor_2.backward

dlp = 0
ulp = 0
urp = 0
drp = 0

pv = 0
sp = 0

def drive():
    global pv,sp

    with open('plot_database.txt','r') as csvfile:
        cords = csv.reader(csvfile, delimiter=',')

        for x in cords:
            sp = float(x[0])
            pv = float(x[1])

    if pv > 320:
        print('Turn LEFT!!!')
        drive_forward(0.1)
        turn_right(0)
        turn_left(turn_speed)
        drive_forward(0.2)
        time.sleep(0.1)
    elif pv < 320:
        print('Turn RIGHT!!!')
        drive_forward(0.1)
        turn_left(0)
        turn_right(turn_speed)
        drive_forward(0.2)
        time.sleep(0.2)

while True:
    drive()

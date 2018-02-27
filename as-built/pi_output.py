from gpiozero import Motor, LED, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
import csv
import time
import numpy as np

turn_speed = 0.7
drive_speed = 0.25
remote_factory = PiGPIOFactory(host='172.20.10.11')
motor_1 = Motor(forward=19, backward=13)
motor_2 = Motor(forward=6, backward=5)

led = LED(26)
sensor = DistanceSensor(echo=18, trigger=17)

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
left_top_line = 0
right_top_line = 0

new_speed = 0.0
state = True

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

def speed():

    global new_speed, state

    while state:

        for speed in np.arange(0.1,0.5,1):
            if new_speed < 0.5:
                new_speed += speed
                print(new_speed)
                return new_speed
            elif new_speed == 0.5:
                new_speed = 0.0

def drive():
    global pv,sp,left_top_line,right_top_line

    with open('plot_database.txt','r') as csvfile:
        cords = csv.reader(csvfile, delimiter=',')

        for x in cords:
            sp = float(x[0])
            pv = float(x[1])

    with open('lines_database.txt','r') as csvfile:
        cords = csv.reader(csvfile, delimiter=',')

        for x in cords:
            left_top_line = float(x[1])
            right_top_line = float(x[2])


    if (pv > 280 or pv < 360):

        #print("PV:", pv, "Left TOP:", left_top_line, "Right Top:", right_top_line)

        drive_forward(speed())
        turn_right(0)
        turn_left(0)
        print("FORWARD")

        if (left_top_line > 320 and right_top_line > 320):
            turn_left(turn_speed)
            turn_right(0)
            drive_forward(speed())

        elif (left_top_line < 320 and right_top_line < 320):
            turn_left(0)
            turn_right(turn_speed)
            drive_forward(speed())

        if pv > 360:
            #drive_backward(0)
            drive_forward(speed())
            turn_right(0)
            turn_left(turn_speed)
            print("TURNING LEFT")


        elif pv < 280:
            #drive_backward(0)
            drive_forward(speed())
            turn_left(0)
            turn_right(turn_speed)
            print("TURNING RIGHT")


init()
while True:
    drive()

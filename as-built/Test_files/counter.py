import numpy as np

new_speed = 0
state = True

def speed():

    global new_speed, state

    while state:

        for speed in np.arange(0.1,0.4,1):
            if new_speed < 0.4:
                new_speed += speed
                print(new_speed)
                return new_speed
            elif new_speed == 0.4:
                new_speed = 0.0


while True:
    speed()

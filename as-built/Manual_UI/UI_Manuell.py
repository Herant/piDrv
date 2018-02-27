from tkinter import *
import sys
from time import sleep
from gpiozero import Motor
#from gpiozero.pins.pigpio import PiGPIOFactory

#remote_factory = PiGPIOFactory(host=)
turn_speed = 0.5
drive_speed = 0.15
#remote_factory = PiGPIOFactory(host=)
# 19 = FORWARD, 13 = BACKWARD
motor_1 = Motor(forward=19, backward=13)
# 6 = LEFT, 5 = RIGHT
motor_2 = Motor(forward=6, backward=5)

drive_forward = motor_1.forward
drive_backward = motor_1.backward
turn_left = motor_2.forward
turn_right = motor_2.backward




class RcApp(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.left = Button(self, text='LEFT')
        self.right = Button(self, text='Right')
        self.forward = Button(self, text='Forward')
        self.reverse = Button(self, text='Reverse')

        self.bind('<ButtonPress>', self.callback)
        self.bind('<ButtonRelease>', self.callback)

        self.left.grid(column=0,row=1)
        self.right.grid(column=2,row=1)
        self.forward.grid(column=1,row=0)
        self.reverse.grid(column=1,row=2)

        self.type = None

    def callback(self, event):
        print(event.type)
        self.type = event.type
        if self.type == '4':
            if event.widget == self.left:
                self.after(200, self.move_left)
            if event.widget == self.right:
                self.after(200, self.move_right)
            if event.widget == self.forward:
                self.after(200, self.move_forward)
            if event.widget == self.reverse:
                self.after(200, self.move_reverse)
            
        

    def move_left(self):
        if self.type == '4':
            
            turn_left(0.3)
            sleep(2)
            motor_2.stop()
            self.after(200, self.move_left)
            print('moving left!')
                
                

    def move_right(self):
        if self.type == '4':
            print('moving right!')
            turn_right(0.3)
            self.after(200, self.move_right)

    def move_forward(self):
        if self.type == '4':
            print('moving forward!')
            drive_forward(0.5)
            self.after(200, self.move_forward)

    def move_reverse(self):
        if self.type == '4':
            print('moving backward!')
            drive_backward(0.5)
            self.after(200, self.move_reverse)

    


root = RcApp()
root.mainloop()

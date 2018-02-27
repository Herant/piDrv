import cv2
import time
import numpy as np

up_y = 0
ball_y = 0
new_sp = 0

plot_sp = 0
plot_pv = 0

# PID CONTROLLER SETTINGS
h=1.35     # 1.35
Ti=0.15    # 0.15
Td=1       # 1
Kp=0.0934  # 0.0934

def pid_controller(img, y, yc, h=1, Ti=1, Td=1, Kp=1, u0=0, e0=0):

    text = 0

    global new_sp
    #  y  .. Measured Process Value
    #  yc .. Setpoint
    #  h  .. Sampling Time
    #  Kp .. Controller Gain Constant
    #  Ti .. Controller Integration Constant
    #  Td .. Controller Derivation Constant
    #  u0 .. Initial state of the integrator
    #  e0 .. Initial error

    # Step variable
    k = 0
    # Initialization
    ui_prev = u0
    e_prev = e0

    if y != yc:
        # Error between the desired and actual output
        e = yc - y
        # Integration Input
        ui = ui_prev + 1.0/Ti * h*e
        # Derivation Input
        ud = 1.0/Td * (e - e_prev)/float(h)
        # Adjust previous values
        e_prev = e
        ui_prev = ui
        # Calculate input for the system
        u = Kp * (e + ui + ud)

        k += 1

        new_sp = int(u)

        text = int(new_sp)
        ball_txt = ('output: {0}'.format(text))
        cv2.putText(img,ball_txt,(470,100),fontFace=4,color=[18,153,255],thickness=1,fontScale=0.8)


def simulator(img, down_left_point, up_left_point, up_right_point, down_right_point):

    lower_center_point_1 = ((down_right_point[0]-down_left_point[0])/2)+down_left_point[0]
    lower_center_point_2 = (down_right_point[1]+down_left_point[1])/2
    low_y = int(lower_center_point_1)
    low_x = int(lower_center_point_2)

    upper_center_point_1 = ((up_right_point[0]-up_left_point[0])/2)+up_left_point[0]
    upper_center_point_2 = ((up_right_point[1]+up_left_point[1])/2)
    half_center_point = ((lower_center_point_2 - upper_center_point_2) / 2) + upper_center_point_2

    global up_y         # SETPOINT
    global ball_y       # FEEDBACK
    global plot_sp, plot_pv

    up_y = int(upper_center_point_1)
    up_x = int(upper_center_point_2)
    midd_x = int(half_center_point)

    cv2.line(img, (320,0),(320,360), [0, 255, 0], 1)
    cv2.line(img, (0,180),(640,180), [0, 255, 0], 1)

    # SP & SV DEBUGGER:

    #if up_y > 0:

        #if new_sp == up_y:
            #print('KEEP FORWARD')

        #elif new_sp > up_y:           #ball_y > up_y
            #print('TURN LEFT')
        #    ball_y -= 1            MANUAL CONTROL

        #elif new_sp < up_y:         #ball_y < up_y
            #print('TURN RIGHT')
        #    ball_y += 1            MANUAL CONTROL

    pid_controller(img, ball_y, up_y, h, Ti, Td, Kp, u0=0, e0=0)  # h=1.35, Ti=0.15, Td=1, Kp=0.0935 - Ok Settings

    cv2.circle(img, (new_sp,midd_x), radius=15, color=[0, 255, 0], thickness=-1)

    ball_txt = ('setpoint: {0}'.format(up_y))
    cv2.putText(img,ball_txt,(450,70),fontFace=4,color=[18,153,255],thickness=1,fontScale=0.8)

    ball_txt = ('error: {0}'.format(up_y - new_sp))
    cv2.putText(img,ball_txt,(491,130),fontFace=4,color=[31, 23, 176],thickness=1,fontScale=0.8)

    # STORING PV AND SP IN A FILE FOR USE IN OTHER PROGRAMS

    plot_sp = up_y
    plot_pv = new_sp
    plot_list = (plot_sp, plot_pv)

    np.savetxt('plot_database.txt', np.array(plot_list), fmt='%.2f', newline=',')

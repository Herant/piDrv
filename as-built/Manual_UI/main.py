# arp -a for ip-adresses
# ACTIVATING REMOTE GPIOS ON PI
# sudo pigpiod
# run code GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.1.130 python3 test.py
# STREAMING piCAMERA to local
# cd /usr/src/mjpg-streamer/mjpg-streamer-experimental
'''
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 360 -fps 20 -ex night"
'''

import numpy as np
import cv2
import mss
from image_processing import process_image
import time

sct = mss.mss()

def img_proccessor():

    while True:

        last_time = time.time()
                        #20/0   65/5 190
        monitor = {'top': 190, 'left': 0, 'width': 640, 'height': 360}
        original_img = np.array(sct.grab(monitor))
        #resized_img = cv2.resize(original_img, (640, 360))
        try:
            fps_calc = 1.0 / (time.time()-last_time)
        except:
            pass
        #print(fps_calc)
        fps = ('fps: {0}'.format(int(fps_calc)))

        new_img = cv2.putText(process_image(original_img),fps,(522,40),fontFace=4,color=[18,153,255],thickness=1,fontScale=0.8) #Color = BGR

        cv2.imshow('Processed', new_img)

        # FPS Monitor
        #print('fps: {0}'.format(1 / (time.time()-last_time)))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

img_proccessor()

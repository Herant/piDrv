import numpy as np
import cv2
import mss
import time
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from image_processing import process_image
from threading import Thread

cv2.ocl.setUseOpenCL(False)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

timer = [0]
sp = [0]
pv = [0]

count_timer = 0

sct = mss.mss()

def animate(i):

    global timer, count_timer, sp, pv

    with open('plot_database.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            count_timer += 1
            sp.append(row[0])
            pv.append(row[1])
            timer.append(count_timer)
            if count_timer % 300 == 0:
                timer.clear()
                sp.clear()
                pv.clear()
                count_timer = 0
                ax1.clear()

    ax1.clear()
    ax1.plot(timer, pv, label='Process Value')
    ax1.plot(timer, sp, label='Dynamic Setpoint')
    ax1.set_title('PID Controller')
    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("PID (PV)")
    plt.grid(True)
    plt.ylim(0)
    plt.xlim(0)
    plt.legend()

def img_proccessor(state):

    last_time = time.time()
                    #20/140
    monitor = {'top': 20, 'left': 0, 'width': 640, 'height': 360}
    original_img = np.array(sct.grab(monitor))
    resized_img = cv2.resize(original_img, (640, 360))

    fps_calc = 1 / (time.time()-last_time)
    fps = ('fps: {0}'.format(int(fps_calc)))

    new_img = cv2.putText(process_image(resized_img),fps,(522,40),fontFace=4,color=[18,153,255],thickness=1,fontScale=0.8) #Color = BGR

    cv2.imshow('Processed', new_img)


class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            img_proccessor(True)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()


#myClassB()
myClassA()
while True:
    pass

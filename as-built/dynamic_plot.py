import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

timer = [0]
sp = [0]
pv = [0]

count_timer = 0

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
    ax1.autoscale(enable=True, axis='both', tight=None)
    plt.grid(True)
    plt.ylim(0)
    plt.xlim(0)
    plt.legend()

def plot_go():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

plot_go()

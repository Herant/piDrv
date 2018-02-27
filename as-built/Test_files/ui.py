# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import tkinter as tk
import csv
import main
from matplotlib import style
from tkinter import ttk
from threading import Thread


LARGE_FONT= ("Verdana", 12)

f = Figure(figsize=(5,5), dpi=100)
ax1 = f.add_subplot(111)

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
    ax1.set_ylabel("PID (DYNAMIC SP & PROCESS VALUE)")
    plt.grid(True)
    plt.ylim(0)
    plt.xlim(0)
    plt.legend()


class piDrv(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "piDrv")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Main(container, self)

        self.frames[Main] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        video_on_button = tk.Button(self, text="Start video processing",
                            command=lambda: main.img_proccessor(True))
        video_on_button.pack()

        video_off_button = tk.Button(self, text="Stop video processing",
                            command=lambda: main.img_proccessor(False))
        video_off_button.pack()

        exit_button = tk.Button(self, text="Exit",
                            command=self.client_exit)
        exit_button.pack()

    def client_exit(self):
        exit()


app = piDrv()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()

# piDrv
selv driving raspberry pi rc car, with only video as input.

Here's some examples of this program:

https://www.youtube.com/watch?v=w9t7N6BsKLE

https://www.youtube.com/watch?v=ykFyVyn9zIk

https://www.youtube.com/watch?v=EriapUwfpHA

In order for this to work you need to install Python 3.5(other may work, but i found 3.5 to work best with the libraries).

You need following libraries:
  - Numpy (https://stackoverflow.com/questions/29499815/how-to-install-numpy-on-windows-using-pip-install)
  - Cv2 (https://pypi.python.org/pypi/opencv-python)
  - Mss (http://python-mss.readthedocs.io/installation.html)
  - Csv (https://csvkit.readthedocs.io/en/0.9.1/install.html)
  - matplotlib (https://matplotlib.org/users/installing.html)
  - gpiozero (https://gpiozero.readthedocs.io/en/stable/installing.html)

To be able to control rc car i used gpiozero to remotly control Rpi. In my case i only got gpiozero working on mac, so if you are windows user try figure out if gpiozero works on your computer.

Since when i was working on that project i didn't know how to program in OOP neither multithreading, that is why my program consists of several programs that you have to run from different consols to work simultaneously. Data that is used in between the programs is stored in plot_database.txt and lines_database.txt. I know its not the most effiecent way of doing that, but it worked.

Also, i run all of the programs on my client computer and only recieving video through streamer and sending GPIO pin commands through gpiozero. The stream that i used is this one: http://petrkout.com/electronics/low-latency-0-4-s-video-streaming-from-raspberry-pi-mjpeg-streamer-opencv/ i found this to by far the best choice since low latency.

After all of the libraries are installed, run the code by running main.py

main.py is designed to grab the defined corner of your upper left screen and process that area. With this code running you can place random driving video from youtube to see that lines are being detected.

dynamic_plot.py is optional and only used to create plotting diagram for SP and PV for the PID controller. (Time discreet PID controller that only controlled software, since no real feedback from the rc.)

And finally pi_output.py is code that starts to send commands to the rc. And gpio_cleanup.py is sometimes need to be run for resetting GPIOs. Both files need to be edited with correct ip-address of your Rpi. Also these has to be ran with command that looks something like this : GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=ip-address python3 pi_output.py
More info : https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

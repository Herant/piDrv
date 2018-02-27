#run code GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.1.130 python3 test.py
# sudo pigpiod
from gpiozero import PWMLED
from time import sleep
from pynput import keyboard

forward = PWMLED(19)
reverse = PWMLED(13)
left = PWMLED(6)
right = PWMLED(5)
led = PWMLED(26)

speed = 1
steer = 1

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

        if format(key) == 'Key.cmd':
            forward.value = speed
        elif format(key) == 'Key.alt':
            reverse.value = speed
        elif format(key) == 'Key.cmd' and format(key) == 'Key.alt_r':
            forward.value = speed
            left.value = steer
        elif format(key) == 'Key.cmd' and format(key) == 'Key.cmd_r':
            forward.value = speed
            right.value = steer
        elif format(key) == 'Key.alt' and format(key) == 'Key.alt_r':
            reverse.value = speed
            left.value = steer
        elif format(key) == 'Key.alt' and format(key) == 'Key.cmd_r':
            reverse.value = speed
            right.value = steer

        if format(key) == 'Key.alt_r':
            left.value = steer
        elif format(key) == 'Key.cmd_r':
            right.value = steer
        if format(key) == 'Key.shift':
            led.value = 1

def on_release(key):
    print('{0} released'.format(
        key))
    forward.value = 0
    reverse.value = 0
    left.value = 0
    right.value = 0
    #led.value = 0
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

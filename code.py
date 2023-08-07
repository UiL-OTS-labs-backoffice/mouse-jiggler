import time
import board
from digitalio import DigitalInOut, Direction
import usb_hid
from adafruit_hid.mouse import Mouse


led = DigitalInOut(board.LED_INVERTED)
led.direction = Direction.OUTPUT

mouse = Mouse(usb_hid.devices)


while True: 
    mouse.move(x=1)
    time.sleep(30)
    mouse.move(x=-1)
    time.sleep(30)

    

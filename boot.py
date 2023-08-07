import board
import touchio
import storage
import time

touch = touchio.TouchIn(board.A0)
wait = 10 * 1000
storage_on = False

while wait > 0:
    if touch.value:
        storage_on = True
        break
    time.sleep(0.001)
    wait -= 1

if not storage_on:
    storage.disable_usb_drive()

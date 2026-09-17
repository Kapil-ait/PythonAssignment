import winsound
import time

for i in range(10):
    winsound.Beep(800, 100)
    time.sleep(0.8)
    winsound.Beep(600, 100)
    time.sleep(0.8)
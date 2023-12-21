import pyautogui as pg
import time
from pynput import keyboard

while True:
    print(pg.position())
    x,y=pg.position()
    print(pg.pixel(x,y))
    time.sleep(1)
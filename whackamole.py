import pyautogui as pg
import time
from pynput import keyboard

# colors
"""
yes1 = 209 150 74
yes2 = 2xx
no1 = 255 0 0
no2 = 134 226 0
"""
xarray = [2316, 2451, 2578, 2701, 2836, 2316, 2451, 2578, 2701, 2836, 2316, 2451, 2578, 2701, 2836]
yarray = [297, 297, 297, 297, 297, 517, 517, 517, 517, 517, 732, 732, 732, 732, 732]

pg.click(2597, 997)
time.sleep(1)

tend = time.time()+63
while True:
    while time.time() < tend:
        for i in range(15):
            r, g, b = pg.pixel(xarray[i], yarray[i])
            if r > 200 and r != 255:
                pg.click(xarray[i], yarray[i])
    time.sleep(360)
print("exit hehehehaw")

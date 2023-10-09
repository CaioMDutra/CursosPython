import pyautogui as pg
import random
import time

pg.FAILSAFE = True

while True:
    x = random.randint(700, 900)
    y = random.randint(800, 1000)
    pg.moveTo(x, y, 0.5)
    time.sleep(2)

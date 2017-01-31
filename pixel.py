from microbit import *

x = 0
y = 0
while True:
    display.clear()
    display.set_pixel(x, y, 9)

    if button_a.was_pressed():
        x = (x+1)%5

    if button_b.was_pressed():
        y = (y+1)%5

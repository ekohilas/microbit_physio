from microbit import *
import music

numbers = [ Image("01110:01010:01010:01010:01110"), #0
            Image("00100:00100:00100:00100:00100"), #1
            Image("01110:00010:01110:01000:01110"), #2
            Image("01110:00010:01110:00010:01110"), #3
            Image("01010:01010:01110:00010:00010"), #4
            Image("01110:01000:01110:00010:01110"), #5
            Image("01110:01000:01110:01010:01110"), #6
            Image("01110:00010:00010:00010:00010"), #7
            Image("01110:01010:01110:01010:01110"), #8
            Image("01110:01010:01110:00010:00010"), #9
            Image("10111:10101:10101:10101:10111"),]#10

def timer(length=None, brightness=5):
    display.show([i*brightness for i in numbers[:length]], delay=1000, clear=True)

notes = "ABCDEFG"
octaves = list(range(1,9))

while True:
    display.show(Image(5,5).invert()*1/9)
    if button_a.was_pressed():
        for n in numbers[1:]:
            display.show(n*9)
            sleep(1000)
            timer()
            timer(6, 3)
    if button_b.was_pressed():
        display.clear()



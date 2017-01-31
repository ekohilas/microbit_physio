from microbit import *
import music

NUMBERS = [ Image("01110:01010:01010:01010:01110"), #0
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
    display.show([i*brightness for i in numbers[1:length]], delay=1000, clear=True)

def number_beep(number, duration, brightness, frequency, sound_length):
    display.show(NUMBERS[number] * brightness)#, wait=False)
    music.pitch(frequency, sound_length, wait=False)
    sleep(duration)

while True:

    display.show(Image.HAPPY*1/9)

    if button_a.was_pressed():

        # 10 sets of 10 seconds
        for set_num in range(1,11):

            for score in range(set_num):
                display.show(NUMBERS[set_num] * 9)
                music.pitch(1750, 50)
                display.clear()
                sleep(10)

            sleep(1000-(50+10)*set_num)

            for rest in range(5,0,-1):
                number_beep(rest, 1000, 3, 500, 50)

            number_beep(set_num, 1000, 9, 1500, 1000)

            for second in range(1,11):
                number_beep(second, 1000, 6, 1000, 50)

            display.clear()


            if button_b.was_pressed():
                break

        music.play(music.POWER_UP)

    if button_b.was_pressed():

        # 10 sets of 5 seconds
        for set_num in range(1,11):

            for score in range(set_num):
                display.show(NUMBERS[set_num] * 9)
                music.pitch(1750, 50)
                display.clear()
                sleep(10)

            sleep(1000-(50+10)*set_num)

            for rest in range(5,0,-1):
                number_beep(rest, 1000, 3, 500, 50)

            number_beep(set_num, 1000, 9, 1500, 1000)

            for second in range(1,6):
                number_beep(second, 1000, 6, 1000, 50)

            display.clear()

            if button_b.was_pressed():
                break

        music.play(music.POWER_UP)


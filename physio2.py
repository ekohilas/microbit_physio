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

            flash_num = set_num
            sleep_duration = 1000
            LONG_BEEP = 333
            SHORT_BEEP = 50
            PAUSE = 50


            for _ in range (set_num//5):
                set_num -= 5
                sleep_duration -= LONG_BEEP + PAUSE
                display.show(NUMBERS[flash_num] * 9)
                music.pitch(1750, LONG_BEEP)
                display.clear()
                sleep(PAUSE)

            for score in range(set_num):
                display.show(NUMBERS[flash_num] * 9)
                music.pitch(1750, SHORT_BEEP)
                display.clear()
                sleep(PAUSE)

            sleep(sleep_duration - (SHORT_BEEP + PAUSE)*set_num)

            for rest in range(5,0,-1):
                number_beep(rest, 1000, 3, 500, SHORT_BEEP)

            number_beep(flash_num, 1000, 9, 1500, 1000)

            for second in range(1,11):
                number_beep(second, 1000, 6, 1000, SHORT_BEEP)

            display.clear()

            if button_b.was_pressed():
                display.scroll("paused", wait=False)
                while not button_a.is_pressed():
                    pass
                display.clear()

        music.play(music.POWER_UP)

    if button_b.was_pressed():

        display.show(Image.ALL_CLOCKS, delay=2500, wait=False)

        for i in range(1,31):
            if not i%15:
                pitch = 900
            elif not i%2:
                pitch = 600
            else:
                pitch = 800

            music.pitch(pitch, 50)
            sleep(1000-50)

            if button_b.was_pressed():
                display.scroll("paused", wait=False)
                while not button_a.is_pressed():
                    pass
                display.clear()

        music.play(music.POWER_UP)



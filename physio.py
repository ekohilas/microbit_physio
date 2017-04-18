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

#def timer(length=None, brightness=5):
#   display.show([i*brightness for i in numbers[1:length]], delay=1000, clear=True)

def number_beep(number, duration, brightness, frequency, sound_length):
    display.show(NUMBERS[number] * brightness)#, wait=False)
    music.pitch(frequency, sound_length, wait=False)
    sleep(duration)

def number_flash(number, brightness, pitch, sound_duration, pause_duration):
    display.show(NUMBERS[number] * brightness)
    music.pitch(pitch, sound_duration)
    display.clear()
    sleep(pause_duration)

def flash_set_number(set_number):

    flash_num = set_number
    sleep_duration = 1000
    LONG_BEEP = 333
    SHORT_BEEP = 50
    PAUSE = 50

    for _ in range (set_number//5):
        set_number -= 5
        sleep_duration -= LONG_BEEP + PAUSE
        number_flash(flash_num, 9, 1750, LONG_BEEP, PAUSE)

    for _ in range(set_number):
        number_flash(flash_num, 9, 1750, SHORT_BEEP, PAUSE)

    sleep(sleep_duration - (SHORT_BEEP + PAUSE)*set_number)

def start_sets(num_sets, set_len):

    for set_num in range(1, num_sets+1):
        play_set(set_num, set_len)
    music.play(music.POWER_UP)

def play_set(set_num, set_len):

    SHORT_BEEP = 50

    # flash set number
    flash_set_number(set_num)

    # coutdown
    for rest in range(5, 0, -1):
        number_beep(rest, 1000, 3, 500, SHORT_BEEP)

    # begin set
    number_beep(set_num, 1000, 9, 1500, 1000)

    # countup
    for second in range(1, set_len+1):
        number_beep(second, 1000, 6, 1000, SHORT_BEEP)

    display.clear()

    # pause
    if button_b.was_pressed():
        display.show(Image.TARGET/9)
        while not button_a.is_pressed():
            pass
        display.clear()

def rest(seconds):
    display.show([x/9 for x in Image.ALL_CLOCKS], delay=(seconds*1000)//12, wait=False)

    for i in range(1, seconds+1):
        if i%15 == 0:
            pitch = 900
        elif i%2 == 0:
            pitch = 600
        else:
            pitch = 800

        music.pitch(pitch, 50)
        sleep(1000-50)

    music.play(music.POWER_UP)

if __name__ == "__main__":

    while True:
        display.show(Image.HAPPY/9)

        if button_a.was_pressed():
            # 10 sets of 10 seconds
            start_sets(10, 10)

        if button_b.was_pressed():
            rest(30)

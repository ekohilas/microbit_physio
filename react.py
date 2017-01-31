from microbit import *

highscore = 0
while True:
    display.show(Image.SQUARE)
    if button_b.was_pressed():
        display.show(Image.SQUARE_SMALL)
        start = running_time()
        while True:
            if button_b.was_pressed():
                end = running_time()
                score = end - start
                if score < highscore or highscore == 0:
                    highscore = score
                display.scroll("{}ms".format(score))
                break

    if button_a.was_pressed():
       display.scroll("{}ms".format(highscore))



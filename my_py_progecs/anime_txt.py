import os
import time


def animate_text(text):
    number_of_char = 1
    while True:
        print('\n')
        print(text[0:number_of_char])
        number_of_char += 1

        if number_of_char > len(text):
            number_of_char = 0

        time.sleep(0.2)
        os.system('clear')


animate_text("Hello Galio!!!")

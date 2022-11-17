# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example uses the light sensor on the Circuit Playground, located next to the picture of the
eye on the board. Once you have the library loaded, try shining a flashlight on your Circuit
Playground to watch the number of NeoPixels lit up increase, or try covering up the light sensor
to watch the number decrease.
"""

'''This is what I want to do:
# define a function that translates letters from a string into morse code
# for each . pixels 0-4 will light up for 0.5 seconds
# for each - pixels 0-9 will light up for 1.5 seconds
# 1 second between each letter
# 2 seconds between each word, with pixel[0] lighting up red

# function will run when light gets a certain level of low (below150?)
'''

import time
from adafruit_circuitplayground import cp
import neopixel

cp.pixels.auto_write = False
cp.pixels.brightness = 0.2

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def morsify(string):
    """turns letters of english alphabet into morse code according to morse code dictionary"""
    morse_word = ''
    for letter in string:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            morse_word += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            morse_word += ' '

    return morse_word

#print(morsify("shit"))

def lights(morseCode):
    """This function translates morse code to lights on the adafruit playground
    Half of pixels   = .
    All pixels       = -
    Red pixel        = new letter
    Double red pixel = new word """
    for char in morseCode:
        if char == '.':
            print(char)
            cp.pixels[0] = (115, 0, 163)
            cp.pixels[1] = (115, 0, 163)
            cp.pixels[2] = (115, 0, 163)
            cp.pixels[3] = (115, 0, 163)
            cp.pixels[4] = (115, 0, 163)
            cp.pixels.show()
            time.sleep(0.5)
            cp.pixels[0] = (0, 0, 0)
            cp.pixels[1] = (0, 0, 0)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[4] = (0, 0, 0)
            cp.pixels.show()
            time.sleep(0.5)

        elif char == "-":
            print(char)
            cp.pixels[0] = (115, 0, 163)
            cp.pixels[1] = (115, 0, 163)
            cp.pixels[2] = (115, 0, 163)
            cp.pixels[3] = (115, 0, 163)
            cp.pixels[4] = (115, 0, 163)
            cp.pixels[5] = (115, 0, 163)
            cp.pixels[6] = (115, 0, 163)
            cp.pixels[7] = (115, 0, 163)
            cp.pixels[8] = (115, 0, 163)
            cp.pixels[9] = (115, 0, 163)
            cp.pixels.show()
            time.sleep(1.5)

            cp.pixels[0] = (0, 0, 0)
            cp.pixels[1] = (0, 0, 0)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[4] = (0, 0, 0)
            cp.pixels[5] = (0, 0, 0)
            cp.pixels[6] = (0, 0, 0)
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)
            cp.pixels[9] = (0, 0, 0)
            cp.pixels.show()
            time.sleep(0.5)
        elif char == ' ':
            print(char)
            cp.pixels[0] = (255, 0, 0)
            cp.pixels.show()
            time.sleep(1)
            cp.pixels[0] = (0, 0, 0)
            cp.pixels.show()
            time.sleep(1)



'''def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range).
    Allows remapping light value to pixel position."""
    return round(value / 320 * 9)'''


while True:
    print(cp.light)

    if cp.light <= 2:
        output = morsify('resist persist')
        lights(output)
    else:
        print(cp.light)


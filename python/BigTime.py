#!/usr/bin/env python3

from art import * #For the bigtext to work
import time
import os
from datetime import datetime

print("Paste this in your browser for the font list:")
print("\x1b[1;4;34mhttps://www.ascii-art.site/FontList.html\n") #\x1b[1;4;34m used to display bold(1), underline(4), and blue(34) text
font = input("\x1b[0mFont for the clock (default font will be used if not specified): ") #\x1b[0m used to reset the style

if not font:
    font = "big" #To display the default font

def output(x): 
    os.system('clear') 
    tprint(str(x), font=font)
    time.sleep(0.09) #This number could be arbitrary
        

while True:
    hrs = datetime.now().hour
    mins = datetime.now().minute
    sec = datetime.now().second
    hrs = str(hrs)
    if int(hrs) < 10:
        hrs = "0" + hrs
    mins = str(mins)
    if int(mins) < 10:
        mins = "0" + mins
    sec = str(sec)
    if int(sec) < 10:
        sec = "0" + sec #There may be a better way using def to make this code more efficient
    output(hrs + ":" + mins + ":" + sec)

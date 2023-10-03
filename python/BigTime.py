from art import *
import time
import os
from datetime import datetime

print("Paste this in your browser for the font list: \nhttps://www.ascii-art.site/FontList.html\n")
font = input("Font for the clock (default font will be used if not specified): ")

if not font:
    font = "big"

def output(x): 
    os.system('clear')
    tprint(str(x), font=font)
    time.sleep(0.09)
        

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
        sec = "0" + sec
    output(hrs + ":" + mins + ":" + sec)

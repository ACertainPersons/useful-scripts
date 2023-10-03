from art import *
import time
import os
from datetime import datetime

hrs = datetime.now().hour
mins = datetime.now().minute
sec = datetime.now().second
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
    output(str(hrs) + ":" + str(mins) + ":" + str(sec))

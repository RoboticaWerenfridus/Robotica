ascii_art = """
                                                                                                                                                                                         
         ,--.                                                                                                                                                                            
       ,--.'|               ___      ,---,                                      .--.--.               ,---,                 ,--,         ,-.                                        ,-.  
   ,--,:  : |             ,--.'|_  ,--.' |                                     /  /    '.           ,--.' |               ,--.'|     ,--/ /|                 ,--,               ,--/ /|  
,`--.'`|  ' :             |  | :,' |  |  :                      ,---,         |  :  /`. /           |  |  :               |  | :   ,--. :/ |          .---.,--.'|         .--.,--. :/ |  
|   :  :  | |             :  : ' : :  :  :                  ,-+-. /  |        ;  |  |--`            :  :  :               :  : '   :  : ' /          /. ./||  |,        .--,`|:  : ' /   
:   |   \ | :  ,--.--.  .;__,'  /  :  |  |,--.  ,--.--.    ,--.'|'   |        |  :  ;_       ,---.  :  |  |,--.  ,--.--.  |  ' |   |  '  /        .-'-. ' |`--'_        |  |. |  '  /    
|   : '  '; | /       \ |  |   |   |  :  '   | /       \  |   |  ,"' |         \  \    `.   /     \ |  :  '   | /       \ '  | |   '  |  :       /___/ \: |,' ,'|       '--`_ '  |  :    
'   ' ;.    ;.--.  .-. |:__,'| :   |  |   /' :.--.  .-. | |   | /  | |          `----.   \ /    / ' |  |   /' :.--.  .-. ||  | :   |  |   \   .-'.. '   ' .'  | |       ,--,'||  |   \   
|   | | \   | \__\/: . .  '  : |__ '  :  | | | \__\/: . . |   | |  | |          __ \  \  |.    ' /  '  :  | | | \__\/: . .'  : |__ '  : |. \ /___/ \:     '|  | :       |  | ''  : |. \  
'   : |  ; .' ," .--.; |  |  | '.'||  |  ' | : ," .--.; | |   | |  |/          /  /`--'  /'   ; :__ |  |  ' | : ," .--.; ||  | '.'||  | ' \ \.   \  ' .\   '  : |__     :  | ||  | ' \ \ 
|   | '`--'  /  /  ,.  |  ;  :    ;|  |  :_:,'/  /  ,.  | |   | |--'          '--'.     / '   | '.'||  :  :_:,'/  /  ,.  |;  :    ;'  : |--'  \   \   ' \ ||  | '.'|  __|  : ''  : |--'  
'   : |     ;  :   .'   \ |  ,   / |  | ,'   ;  :   .'   \|   |/                `--'---'  |   :    :|  | ,'   ;  :   .'   \  ,   / ;  |,'      \   \  |--" ;  :    ;.'__/\_: |;  |,'     
;   |.'     |  ,     .-./  ---`-'  `--''     |  ,     .-./'---'                            \   \  / `--''     |  ,     .-./---`-'  '--'         \   \ |    |  ,   / |   :    :'--'       
'---'        `--`---'                         `--`---'                                      `----'             `--`---'                          '---"      ---`-'   \   \  /            
                                                                                                                                                                      `--`-'   
"""

print(ascii_art)
import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
from bluedot import BlueDot

bd = BlueDot()
 
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(6, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setwarnings(False)

init()

def forward(tf):
    gpio.output(6, True)
    gpio.output(12, True)
    time.sleep(tf)
    
def left(tf):
    gpio.output(6, False)
    gpio.output(12, True)
    time.sleep(tf)
     
def right(tf):
    gpio.output(6, True)
    gpio.output(12, False)
    time.sleep(tf)
    
def stop(tf):
    gpio.output(6, False)
    gpio.output(12, False)
    sys.exit()
    time.sleep(tf)
    
def move(pos):
    init()
    sleep_time = 0.030
    
    if pos.top:
        forward(sleep_time)
    elif pos.left:
        left(sleep_time)
    elif pos.right:
        right(sleep_time)
    elif pos.bottom:
        stop(sleep_time)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(6, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setwarnings(False)
    
def stop1():
    init()
    gpio.output(6, False)
    gpio.output(12, False)

gpio.output(6, False); gpio.output(12, False)
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop1
command = tk.Tk()
command.mainloop()

        


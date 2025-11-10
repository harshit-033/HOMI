import pyautogui as p
from time import sleep
import pyperclip
import random
from datetime import datetime
date=datetime.now()
sleep(5)


#open
def opw():
    global p
    p.moveTo(16,754,duration=0.2)
    p.click(16,754)
    p.moveTo(57,698,duration=0.2)
    p.click(57,698)
    p.typewrite("chrome",interval=0.2)
    p.press('Enter')
    sleep(3)
    p.moveTo(469,499,duration=0.2)
    sleep(1)
    p.click(469,499)
    p.click(469,499)
    sleep(5)
    while True:
        if p.pixelMatchesColor(134,141,(0, 230, 118),tolerance=2)and p.pixelMatchesColor(780,502,(18, 46, 49),tolerance=2)and p.pixelMatchesColor(687,717,(18, 138, 126),tolerance=2):
            print("whatsapp not connected")
        else:
            if p.pixelMatchesColor(931,324,(66, 203, 165),tolerance=2):
                print("whatsapp started......")
                p.moveTo(329,344,duration=0.2)
                p.click(329,344)
                break
            else:
                print("wrong tab")
    
        
                           

opw()                           
                           
                           

            


    
        
        
    
            

    

import pyautogui as p
from time import sleep

sleep(4)
pos3=p.locateOnScreen("logo.png",confidence=.7)
pos3x=pos3[0]
pos3y=pos3[1]
print(pos3x)
p.moveTo(pos3,duration=0.2)
p.click()
p.rightClick()
p.moveTo(pos3x+56,pos3y+250,duration=0.2)
p.click(pos3x+56,pos3y+259)
sleep(5)

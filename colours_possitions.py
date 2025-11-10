import pyautogui as p
from time import sleep
sleep(2)
p.press('win')
p.typewrite('whatsapp')
p.press('enter')
sleep(1)
p.press('ctrl + f')
sleep(1)
p.typewrite('Harshit Bajpayee')
p.press('down')
p.press('enter')




'''
while True:
    posxy=p.position()
    print(posxy, p.pixel(posxy[0],posxy[1]))
    sleep(1)
    if posxy[0]==0 and posxy[1]==0:
        break
'''
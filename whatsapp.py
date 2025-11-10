import pyautogui as p
from time import sleep
from datetime import datetime


dt1 = datetime(2025, 9, 12, 15, 15, 25)



while True:
    now = datetime.now()

    if now==dt1:
        sleep(2)
        p.press('win')
        p.typewrite('whatsapp')
        p.press('enter')
        sleep(1)
        p.press('ctrl + f')
        p.typewrite('Harshit Bajpayee')
        p.press('down')
        p.press('enter')
        sleep(1)
        for i in range(0,2000):
            p.typewrite('lode ho tum')
            p.press('enter')
        break
    else:
        continue








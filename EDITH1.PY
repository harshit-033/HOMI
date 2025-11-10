import pyautogui as p
import os
from time import sleep
import pyperclip
import random
from datetime import datetime
date=datetime.now()
sleep(5)


#get message
def get():
    global p
    p.moveTo(535,627, duration=.2)
    p.tripleClick()
    p.rightClick()
    p.moveTo(614,507)
    p.click()
    sg=pyperclip.paste()
    
    msg = ""


    for char in sg:


        if ord(char) >= 65 and ord(char) <= 90:
            msg += char

        elif ord(char) >= 97 and ord(char) <= 122:
            msg += char


    print(msg)
    return msg
    
#get ADMIN
def getA():
    global p
    p.moveTo(1112,626, duration=.2)
    p.tripleClick()
    p.rightClick()
    p.moveTo(1105,498)
    p.click()
    msgA=pyperclip.paste()
    return msgA
#Reply(admin)
def replyA(msgA):
    global p
    f=open("messages.txt",'a',encoding='utf-8')
    date=datetime.now()
    t=str(date)
    gret=['hi','hello','hii','hey','heya']
    ask=['how are you?','how are you??','how are you???','how r u?','how r u???''how r u??','how are you','how r u','how are u?','how are u??','how are u']
    k=['okk','k','ok','okkk','oky','okay','oka','okays','welcome','wc','welcomes']
    thk=['thank','thank you','thanks','tk','thk','thank u','thanku']
    comp=['good','nice','very good','gud','vg','very nice','excellent','wonderfull','outstanding']
    if str(msgA).lower() in gret:   
        ass="Hello Boss/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(ass,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(ass)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr. Harshit")
    elif str(msgA).lower()in ask:
        ass1="i am fine, what about u?/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(ass1,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(ass1)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower()in thk:
        ass4=":smi"
        asss4="welcome/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(ass4,interval=0.1)
        p.press('Enter')
        p.press('Enter')
        p.moveTo(637,695)
        p.click(637,695)
        p.write(asss4,interval=0.1)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(ass4)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower() in k:
        ass2=("\\")
        p.moveTo(637,695)
        p.click(637,695)
        p.write(":thu",interval=0.2)
        p.press('Enter')
        p.press('Enter')
        p.moveTo(637,695)
        p.click(637,695)
        p.write(ass2,interval=0.2)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(ass2)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower() in comp:
        ass3=("\\")
        p.moveTo(637,695)
        p.click(637,695)
        p.write(":thu",interval=0.1)
        p.press('Enter')
        p.press('Enter')
        p.moveTo(637,695)
        p.click(637,695)
        p.write(ass3,interval=0.1)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(ass3)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower()=="screenshot/":
        x=p.screenshot(imageFilename='screen.png')
        dc=os.getcwd()+'\screen.png'
        p.moveTo(520,697,duration=0.2)
        p.click(520,697)
        p.moveTo(520,630,duration=0.2)
        p.click(520,630)
        sleep(3)
        p.moveTo(440,666,duration=0.2)
        p.click(440,666)
        p.write(dc)
        sleep(1)
        p.press('Enter')
        sleep(1)
        p.press('Enter')
        sleep(1)
        p.press('Enter')
        sleep(6)
        p.moveTo(637,695)
        p.click(637,695)
        p.write('//',interval=0.1)
        p.press('Enter')
        p.press('Enter')
        p.write('//',interval=0.1)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write("screenshot")
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower()in "commands/":
        hel="*commands/*(shows all the commands),*archiveself/*(EDITH is removed from top),*archive/*(archive the below chat),*recaud/*(record audio of 20 sec),*webcam/*(takes picture through your pc webcam),*screenshot/*(takes screen shot of your pc),*closetabs/*(close all tabs other than whatsapp)"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(hel,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(hel)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr.Harshit")
    elif str(msgA).lower()in "closetabs/":
        pos3=p.locateOnScreen("logo.png",confidence=.7)
        pos3x=pos3[0]
        pos3y=pos3[1]
        if pos3 is not None:
            sleep(4)
            p.moveTo(pos3,duration=0.2)
            p.click()
            p.rightClick()
            p.moveTo(pos3x+56,pos3y+259,duration=0.2)
            p.click(pos3x+56,pos3y+259)
            p.moveTo(0,pos3y+259,duration=0.2)
            p.click(0,pos3y+259)
            sleep(1)
        exe="Done boss/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(exe,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write(exe)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr. Harshit")        
    elif str(msgA).lower()in "webcam/":
        p.moveTo(520,695,duration=0.3)
        p.click(520,695)
        sleep(1)
        p.moveTo(519,481,duration=0.3)
        p.click(519,481)
        sleep(2)
        
        p.moveTo(862,652,duration=0.3)
        p.click(862,652)
        sleep(1)
        p.press('Enter')
        sleep(1)
        p.press('Enter')
        exe="Done boss/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(exe,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write("webcam")
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr. Harshit")
        p.moveTo(637,695)
        p.click(637,695)
        p.write('//',interval=0.1)
        p.press('Enter')
        p.press('Enter')
    elif str(msgA).lower()in "recaud/":
        p.moveTo(1250,695,duration=0.5)
        p.click(1250,695)
        sleep(30)
        p.moveTo(1250,695,duration=0.5)
        p.click(1250,695)
        exe="Done boss/"
        p.moveTo(637,695)
        p.click(637,695)
        p.write(exe,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msgA)
        f.write('%\n'+"sent:-")
        f.write("Recording")
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+"Mr. Harshit")
        p.moveTo(637,695)
        p.click(637,695)
        p.write('//',interval=0.1)
        p.press('Enter')
        p.press('Enter')
    elif str(msgA).lower()in "archive/":
        p.moveTo(415,334,duration=0.2)
        p.click(415,334)
        sleep(2)
        p.moveTo(461,370,duration=0.2)
        p.click(461,370)
        p.moveTo(637,695)
        p.click(637,695)
        p.write('//',interval=0.1)
        p.press('Enter')
        p.press('Enter')
    elif str(msgA).lower()in "archiveself/":
        p.hotkey('Ctrl','Alt','Shift','E')
        p.moveTo(227,250,duration=0.2)
        p.click(227,250)
        
        
            
    f.close()        
        





#REPLY
def reply(msg):
    global p
    p.click(505,131)
    p.moveTo(1078,416,duration=.2)
    p.tripleClick(duration=.2)
    p.rightClick(duration=0.2)
    p.moveTo(1120,436)
    p.click()
    sen=pyperclip.paste()
    print(sen)
    p.click(932,133)
    f=open("messages.txt",'a',encoding='utf-8')
    t=datetime.now()
    t=str(date)
    p.moveTo(637,695)
    gret=['hi','hello','hii','hey','heya']
    ask=['how are you?','how are you??','how are you???','how r u?','how r u???''how r u??','how are you','how r u','how are u?','how are u??','how are u']
    k=['okk','k','ok','okkk','oky','okay','oka','okays','welcome','wc','welcomes']
    thk=['thank','thank you','thanks','tk','thk','thank u','thanku']
    comp=['good','nice','very good','gud','vg','very nice','excellent','wonderfull','outstanding']

    if str(msg).lower() in gret:
        rep="Hello, whats up??"
        p.click(637,695)
        p.write(rep,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(rep)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
    elif str(msg).lower()in ask:
        rep1="i am fine, what about u?"
        p.click(637,695)
        p.write(rep1,interval=0.1)
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(rep1)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
    elif str(msg).lower()in thk:
        rep4="welcome :smi"
        p.click(637,695)
        p.write(rep4,interval=0.1)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(rep4)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
    elif str(msg).lower() in k:
        rep2=("smili face")
        p.click(637,695)
        p.write(":thu",interval=0.2)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(rep2)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
    elif str(msg).lower() in comp:
        rep3=("  THANK YOU :smi")
        p.click(637,695)
        p.write(rep3,interval=0.1)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(rep3)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
        
    else:
        pos3=p.locateOnScreen("logo.png",confidence=.7)
        pos3x=pos3[0]
        pos3y=pos3[1]
        if pos3 is not None:
            sleep(4)
            p.moveTo(pos3,duration=0.2)
            p.click()
            p.rightClick()
            p.moveTo(pos3x+56,pos3y+259,duration=0.2)
            p.click(pos3x+56,pos3y+259)
            p.moveTo(0,pos3y+259,duration=0.2)
            p.click(0,pos3y+259)
        sub="Your msg will be deliverd.This is Mr.Harshit's python bot EDITH.He is curently not availaible,will message you soon.Currenty Mr.Harshit only taught me to reply the messages like *hi* , *hello* , *how are u* , *ok* and compliments like=> *good* , *nice* , etc. *Sorry for inconvinience,I am under developent*"
        sub2="EDITH(Future of the world)"
        sub3="Drop your msg you want to send!"
        p.click(637,695)
        p.write("Your msg will be deliverd.This is Mr.Harshit's python bot EDITH.He is curently not availaible,will message you soon.Currenty Mr.Harshit only taught me to reply the messages like *hi* , *hello* , *how are u* , *ok* and compliments like=> *good* , *nice* , etc. *Sorry for inconvinience,I am under developent*. ",interval=0.1)
        p.press('Enter')
        p.write("*Drop your msg you want to send!*",interval=.01)
        p.press('Enter')
        p.write("*EDITH*(Future of the world)",interval=.01)
        p.press('Enter')
        p.write(":rob",interval=.01)
        p.press('Enter')
        p.press('Enter')
        f.write('%\n'+'%\n'+"recived:-")
        f.write(msg)
        f.write('%\n'+"sent:-")
        f.write(sub + sub3 + sub2)
        f.write('%\n'+"time:-"+t)
        f.write('%\n'+"With:-"+sen)
    f.close()        
#search
def search():
    p.moveTo(526,639, duration=0.5)
    p.click(1246,638)
    while True:
        if p.pixelMatchesColor(34,232,(8, 41, 76),tolerance=2)and p.pixelMatchesColor(29,242,(214, 255, 255),tolerance=2):
            p.moveTo(34,232,duration=0.01)
            p.click(34,232)
            replyA(getA())
        elif p.pixelMatchesColor(44,255,(244, 211, 59),tolerance=2)and p.pixelMatchesColor(36,242,(254, 253, 255),tolerance=2):
            p.moveTo(34,232,duration=0.01)
            p.click(34,232)
            p.moveTo(415,262)
            sleep(1)
            p.click(415,262)
            p.moveTo(459,294)
            p.click(459,294)
        elif p.pixelMatchesColor(484,694,(53, 53, 53),tolerance=2):
            p.moveTo(1259,695,duration=0.5)
            p.click(1259,695)
            
   

        else:
            try:
                pos2=p.locateOnScreen("dot.png",confidence=.7)
                if pos2 is not None:
                    p.moveTo(pos2)
                    p.moveRel(-200,0)
                    p.click()
                    sleep(.5)
                        
            except(Exception):
                print("no new msg...")
                
            if p.pixelMatchesColor(527,636,(32, 44, 51),tolerance=2):
                reply(get())
                print("recived:-")
                
            else:
                print("no msg yet...")
                
        posxy=p.position()
        if posxy[0]==0:
            break
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
    p.moveTo(457,522,duration=0.2)
    sleep(1)
    p.click(457,522)
    p.click(457,522)
    while True:
        if p.pixelMatchesColor(472,493,(12, 191, 66),tolerance=2):
            p.moveTo(457,522,duration=0.2)
            sleep(1)
            p.click(457,522)
            p.click(457,522)
            
            if p.pixelMatchesColor(356,265,(83, 83, 83),tolerance=2)and p.pixelMatchesColor(388,266,(255, 255, 255),tolerance=2)and p.pixelMatchesColor(353,253,(255, 255, 255),tolerance=2):
                print("No internet access")
            if p.pixelMatchesColor(134,141,(0, 230, 118),tolerance=2)and p.pixelMatchesColor(780,502,(18, 46, 49),tolerance=2)and p.pixelMatchesColor(687,717,(18, 138, 126),tolerance=2):
                print("whatsapp not connected")            
            else:
                if p.pixelMatchesColor(931,324,(66, 203, 165),tolerance=2):
                    print("whatsapp started......")
                    p.moveTo(329,344,duration=0.2)
                    p.click(329,344)
                    search()
                else:
                    print("wrong tab")
        elif p.pixelMatchesColor(34,139,(196, 172, 106),tolerance=2)and p.pixelMatchesColor(34,119,(255, 253, 255),tolerance=2):
            print("whatsapp started......")
            p.moveTo(34,232,duration=0.2)
            p.click(34,232)
            search()
        else:
            print("wrong window")
            
       
        posxy=p.position()        
        if posxy[0]==0:
            break    
        sleep(1)        

#password protect
for i in (1,4):
    pswd=p.password(text=' enter your password/command word:-',title='E.D.I.T.H.')
    if pswd=="harshit.03/start":
        print("ACCESS GRANTED")
        print("EDITH STARTING")
        print("5")
        sleep(1)
        print("4")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        sleep(1)
        print("0")
        print("STARTED")
        sleep(1)
        while True:
            opw()
            posxy=p.position()        
            if posxy[0]==0:
                break 
    elif pswd=="harshit.03/end":
        print("THANKS FOR USING")
        sleep(1)
        break
    elif i==3:
        print("ACCESS DENIED")
        print("Unauthorised access")
        print("EDITH is closing")
        sleep(1)
        break
        
    else:
        print("ACCESS DENIED")
        print("Unauthorised access")

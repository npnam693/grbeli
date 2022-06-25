from pyautogui import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pyautogui
import time
import keyboard
import random
import win32api, win32con

import os

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r"C:\Users\Admin\Desktop\GreenBeli\chromedriver.exe",chrome_options=options)
url = 'https://play.greenbeli.io/'
print ("Open Chorme")
driver.get(url)


Game = 1;
print("~~~~~~~~~ Game 1 start!!! ~~~~~~~~~~")
while 1:
    if pyautogui.locateOnScreen('Login.png', confidence=0.7) == None:
        time.sleep(2)
        print("Waitting.....")
    else:
        pyautogui.rightClick(pyautogui.locateCenterOnScreen('Login.png', confidence=0.7))
        break
print("Log in GREEN")
if pyautogui.locateOnScreen('wallet.png', confidence=0.9) != None:
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('wallet.png', confidence=0.9))
    time.sleep(0.5)
    pyautogui.rightClick();
    pyautogui.write('0xa2a1727Ae4d2c9c74Fc029975bCCbeFC73a36421')
if pyautogui.locateOnScreen('pass.png', confidence=0.9) != None:
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('pass.png', confidence=0.9))
    time.sleep(0.5)
    pyautogui.rightClick();
    pyautogui.write('greenhivong')

while 1:
    if pyautogui.locateOnScreen('login1.png', confidence=0.8) != None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('login1.png', confidence=0.8))
        time.sleep(0.3)
        pyautogui.rightClick()
        print("Login in Green - DONE")
        break;
    else:
        print("Notfound Login button")

i = 0
while 1:
    if pyautogui.locateOnScreen('x.png', confidence=0.9) != None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('x.png', confidence=0.9))
        time.sleep(0.3)
        pyautogui.rightClick()
        print("click X done!!")
        break;
    else:
        print("Notfound X button")
        i = i + 1
        if (i == 15):
            break
while 1:
    if pyautogui.locateOnScreen('battle.png', confidence=0.9) != None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('battle.png', confidence=0.9))
        time.sleep(0.3)
        pyautogui.rightClick()
        print("click BATTLE done!!")
        break;
    else:
        print("Notfound Battle button")

while 1:
    if pyautogui.locateOnScreen('pve.png', confidence=0.9) != None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('pve.png', confidence=0.9))
        time.sleep(0.3)
        pyautogui.rightClick()
        print("click PVE")
        break;
    else:
        print("Notfound pve")

time.sleep(2)
round  = 1;
while (1):
    if (round<=3):
        while 1:
            if pyautogui.locateOnScreen('hint.png', confidence=0.9) == None:
                time.sleep(2)
                print("Not in choice --- Waiting....")
            else :
                break
        if pyautogui.locateOnScreen('3.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('3.png', confidence=0.9);
        elif pyautogui.locateOnScreen('4.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('4.png', confidence=0.9);
        elif pyautogui.locateOnScreen('5.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('5.png', confidence=0.9)
        elif pyautogui.locateOnScreen('6.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('6.png', confidence=0.9)
        elif pyautogui.locateOnScreen('7.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('7.png', confidence=0.9)
        elif pyautogui.locateOnScreen('8.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('8.png', confidence=0.9)
        elif pyautogui.locateOnScreen('2.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
        elif pyautogui.locateOnScreen('1.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('1.png', confidence=0.9)
        else:
            print("Not found a card.")
            continue
        pyautogui.moveTo(x,y)
        time.sleep(0.2)
        pyautogui.rightClick()
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Select.png', confidence=0.9))
        time.sleep(0.2)
        pyautogui.rightClick()
        round = round+1
        print(round)
    elif (round > 3 and round <=6):
        while 1:
            if pyautogui.locateOnScreen('hint.png', confidence=0.75) == None:
                time.sleep(2)
                print("Not in choice --- Waiting....")
            else :
                break;
        if pyautogui.locateOnScreen('9.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('9.png', confidence=0.9);
        elif pyautogui.locateOnScreen('8.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('8.png', confidence=0.9);
        elif pyautogui.locateOnScreen('7.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('7.png', confidence=0.9)
        elif pyautogui.locateOnScreen('6.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('6.png', confidence=0.9)
        elif pyautogui.locateOnScreen('5.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('5.png', confidence=0.9)
        elif pyautogui.locateOnScreen('4.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('4.png', confidence=0.9)
        elif pyautogui.locateOnScreen('3.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('3.png', confidence=0.9)
        elif pyautogui.locateOnScreen('2.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
        elif pyautogui.locateOnScreen('1.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('1.png', confidence=0.9)
        else:
            print("Not found a card.")
            continue
        pyautogui.moveTo(x,y)
        time.sleep(0.2)
        pyautogui.rightClick()
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Select.png', confidence=0.9))
        time.sleep(0.2)
        pyautogui.rightClick()
        round = round+1
        print(round)
    else:
        time.sleep(2)
        if pyautogui.locateOnScreen('hint.png', confidence=0.75) == None:
            key = 1;
            while 1:
                if pyautogui.locateOnScreen('Next.png', confidence=0.9) != None:
                    x, y = pyautogui.locateCenterOnScreen('Next.png', confidence=0.9)
                    pyautogui.moveTo(x, y)
                    time.sleep(0.3)
                    pyautogui.rightClick()
                    round = 1;
                    print("NewGame")
                    Game= Game +1    
                    # if (Game == 16):
                    #     os.system("shutdown /s /t 1")
                    print("~~~~~~~~~ Game",Game,"start!!! ~~~~~~~~~~")
                    time.sleep(10)
                    key = 0
                    break
                elif pyautogui.locateOnScreen('hint.png', confidence=0.75) == None :
                    print("Not in choice --- Waiting....")
                    time.sleep(2)
                else: break
        if (key == 0): continue
        if pyautogui.locateOnScreen('10.png', confidence=0.85) != None:
            x, y = pyautogui.locateCenterOnScreen('10.png', confidence=0.85);
        elif pyautogui.locateOnScreen('9.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('9.png', confidence=0.9);    
        elif pyautogui.locateOnScreen('8.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('8.png', confidence=0.9);
        elif pyautogui.locateOnScreen('7.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('7.png', confidence=0.9)
        elif pyautogui.locateOnScreen('6.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('6.png', confidence=0.9)
        elif pyautogui.locateOnScreen('5.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('5.png', confidence=0.9)
        elif pyautogui.locateOnScreen('4.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('4.png', confidence=0.9)
        elif pyautogui.locateOnScreen('3.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('3.png', confidence=0.9)
        elif pyautogui.locateOnScreen('2.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
        elif pyautogui.locateOnScreen('1.png', confidence=0.9) != None:
            x, y = pyautogui.locateCenterOnScreen('1.png', confidence=0.9)
        else:
            print("Not found a card.")
            continue
        pyautogui.moveTo(x,y)
        time.sleep(0.2)
        pyautogui.rightClick()
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Select.png', confidence=0.9))
        time.sleep(0.2)
        pyautogui.rightClick()
        round = round+1
        print(round)


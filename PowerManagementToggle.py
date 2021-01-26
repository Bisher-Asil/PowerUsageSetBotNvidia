import os
from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con


#This program was written in a few hours, its purpose is to set the computer's power usage.
# Disclaimer: This is an awful way to do it, even the cmds, a better way would be NViAPI but I dont want to use it
## 1200 150 , 1220 300  # To open control panel


## 776 419,  240 240 240 To scroll down

## 750 419 To click the menu

## 556 431 , 120 185 4 To Check if menu is opened

## Optimal : X same, 430
## Adaptive(Balanced): , 450
## Performance: , 470


def PowerSetting(x):
    OpenCtrlPanel()
    FindPowerSettings(x)

def ClickOnPosition(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def OpenCtrlPanel():
    ChangeinY = 140
    ChangeinX = 20
    win32api.SetCursorPos((1200,150))
    x, y = win32api.GetCursorPos()  
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(0.011)
    win32api.SetCursorPos((x+ChangeinX,y+ChangeinY))
    time.sleep(0.011)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.011)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

Found = False
Found2 = False
Found3 = False 


def FindPowerSettings(x):
    try:
        Found = False
        while(Found == False):
            if pyautogui.pixel(776,419)[0] == 240 and pyautogui.pixel(776,419)[1] == 240 and pyautogui.pixel(776,419)[2] == 240:
                Found = True
                ClickOnPosition(776,419)
                time.sleep(0.1)
                ClickOnPosition(750,419)
                try:
                    Found2 = False
                    while(Found2 == False):
                        if pyautogui.pixel(556,431)[0] == 120 and pyautogui.pixel(556,431)[1] == 185 and pyautogui.pixel(556,431)[2] == 4:
                            Found2 = True
                            if(x == 1): ClickOnPosition(750, 430)
                            elif (x == 2): ClickOnPosition(750, 450)  
                            elif (x==3): ClickOnPosition(750, 470)    
                            time.sleep(1)
                            ClickOnPosition(1919, 0)
                            time.sleep(1)
                            keyboard.press_and_release("enter")
                        else: time.sleep(0.01)
                except:
                    pass
            else: time.sleep(0.01)
    except:
        pass



On = True
while (On == True):

    e = input("Type s for Saving, b for Balanced, p for Performance, N to cancel: ")
    if(e == 's' or e == 'S'): 
        os.startfile('PowerSaver.cmd')
        PowerSetting(1)
    elif (e== 'b' or e == 'B'): 
        os.startfile('Balanced.cmd')
        PowerSetting(2)
    elif (e=='p' or e == 'P'): 
        os.startfile('Performance.cmd')
        PowerSetting(3)
    elif (e=='n' or e == 'N'): On = False
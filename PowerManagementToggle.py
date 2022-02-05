import os
import pyautogui 
import time
import keyboard
import win32api, win32con


#This program was written in a few hours, its purpose is to set the computer's power usage.
# Disclaimer: This is an awful way to do it, even the cmds, a better way would be NViAPI but I dont want to use it
## 1200 150 , 1220 300  # To open control panel

# Update: 18/12/2021, Made it more consistent so it requires no human intervention, optimized a little more

#Update : 5/2/2021, Made it check for icons repeatedly, fixed crashing 

## 776 419,  240 240 240 To scroll down

## 750 419 To click the menu

## 556 431 , 120 185 4 To Check if menu is opened

## Optimal : X same, 430
## Adaptive(Balanced): , 450
## Performance: , 470

ISenabled = True
current_step = 1  ##using this to make it loop if current step is not complete, this prevents common crashing, steps are: 1: Right click on desktop 2: find Nvidia Control Panel 3: click on Nvidia Control Panel
## 4: find scroll wheel 5: click scroll wheel to get to performace settings 6: find performace settings 7: click performance settings 8: choose correct performance setting 9: press the upper right corner to close 10: press enter to apply

def FindPowerSettings(x):
    global current_step
    while(current_step != 10 or keyboard.is_pressed('q') == False):
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
                            if  (pyautogui.locateOnScreen('OpenSetting.png', confidence = 0.85)):
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
                else: time.sleep(0.001)
        except:
            pass


def PowerSetting(x):
    OpenCtrlPanel()
    FindPowerSettings(x)

def ClickOnPosition(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def OpenCtrlPanel():
    openpanel = False
    foundpanel = False
    while(openpanel == False):
        win32api.SetCursorPos((1200,150))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.25)
        openpanel = True
    while(foundpanel ==False):
        PanelLocation = pyautogui.locateOnScreen('CtrlPnl.png', confidence = 0.85)
        if (PanelLocation[1] != 0): 
            win32api.SetCursorPos((PanelLocation[0],PanelLocation[1]))
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.011)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            foundpanel = True

while (ISenabled == True):
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

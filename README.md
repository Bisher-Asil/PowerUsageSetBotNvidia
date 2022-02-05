# PowerUsageSetBotNvidia
This bot sets your power settings, using CMDs for Windows and Pyautogui for Nvidia ControlPanel (This is a bad way, NvAPI is better)

This bot was only made with the intention to make my life easier, please do not sue me I am just simulating a user.

This is not very friendly as of yet (6/2/2021) but inshallah I'll make a GUI version

You must have a screen that is exactly 1920x1080, Or be willing to go through pyautogui.displayMousePos() and change some numbers your self.

How to set the numbers in case your screen is different:
1-Open a python IDLE, the default one works great.
2- import pyautogui, and run the command displayMousePos()
3- Go to the relevant numbers (All commented in the code) and change them

You can also take a different path by just doing some math to take the percentage of my screen to your screen, the app will scale accordingly.

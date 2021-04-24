from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32com

while keyboard.is_pressed('q') == False:
	point = pyautogui.locateOnScreen('next.png', confidence=0.7)
	if point != None:
		print("I can see it")
		pyautogui.click(pyautogui.center(point))
	else:
		n=1		
		if pyautogui.locateOnScreen('wait.png', confidence=0.7) != None:
			print("waiting")
			n=0
		err = pyautogui.locateOnScreen('error.png', confidence=0.7)

		if err != None:
			print("error")
			pyautogui.click(pyautogui.center(err))
			n=0
		if n==1:
			print("I am unable to see it")
			press('down')
			press('down')
			press('down')
			press('down')
			press('down')
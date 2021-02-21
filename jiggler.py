from time import sleep
import pyautogui, sys

print("[SUCCESS] Starting the jiggling!")

while True:
    xpos = pyautogui.position()[0]
    ypos = pyautogui.position()[1]
    pyautogui.moveTo(xpos,ypos)   
    pyautogui.moveTo(xpos + 1,ypos) 
    sleep(2)

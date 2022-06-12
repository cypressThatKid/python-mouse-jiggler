from time import sleep
import pyautogui

print("Coffee time...")

forward = True

try:
    while True:
        xpos = pyautogui.position()[0]
        ypos = pyautogui.position()[1]
        pyautogui.moveTo(xpos,ypos)
        new_pos = xpos - 1
        if forward:
            new_pos = xpos + 1
        forward = not forward
        pyautogui.moveTo(new_pos, ypos)
        sleep(30)

except KeyboardInterrupt:
    print("offee over. Get back to work, buddy.")

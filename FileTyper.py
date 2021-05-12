import pyautogui as pyg
import time as t
f = open("FILENAME", "r")
listOfLines = f.readlines()
for line in listOfLines:
    t.sleep(5)
    pyg.press("t")
    print(line.strip())
    pyg.write(line.strip())
    pyg.press("enter")
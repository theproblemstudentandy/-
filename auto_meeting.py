# -*- coding: utf-8 -*-


import webbrowser as wb
import pyautogui as py


url = str(input("Please input google meeting url:"))
wb.open(url)
py.sleep(3)
py.click()
py.sleep(2)

#ctrl+e close the webcam/ctrl+d close the microphone 
py.sleep(2)
py.hotkey('ctrl', 'e')
py.sleep(2)
py.hotkey('ctrl', 'd')
py.sleep(2)
join = py.click('join.png')
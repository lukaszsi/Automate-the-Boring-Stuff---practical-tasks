#! python3
# hangoutsBot.py - sends message to two persons from list.

import pyautogui
import time
import sys

people = ['user1', 'user2']

# Choosing people for the message.
for person in people:
    pyautogui.click(230, 176)
    pyautogui.typewrite(person)
    time.sleep(3)
    if pyautogui.locateOnScreen(person + '.png') != None:
        personImgPlace = pyautogui.locateOnScreen(person + '.png')
        personCenter = pyautogui.center(personImgPlace)
        personX, personY = personCenter
        pyautogui.click(personX - 118, personY)
    else:
        print('User ' + person + ' not found!')
        sys.exit()
    
# Sending the message.
pyautogui.click(168, 227)
time.sleep(3)
message = 'Hi, test message'
pyautogui.typewrite(message)
pyautogui.typewrite(['enter'])

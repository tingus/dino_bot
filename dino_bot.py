# from ast import If
# from pickle import FALSE
from PIL import ImageGrab
# from functools import partial
# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# https://trex-runner.com/

import pyautogui
import keyboard
import time

# mouse = pyautogui.mouse
# keyboard = pyautogui.keyboard
startingPosition = None

def checkCollision(startPos):
    # check for trees
    if startPos:
        x = startPos[0] + 40
        y = startPos[1] + 5
        toleranceAmount = 5
        # checkMarkers = [15, 35, 60]
        checkMarkers = [35, 60]
        
        for single in checkMarkers:
            # if pyautogui.pixelMatchesColor((x + single), y, (83, 83, 83), tolerance=toleranceAmount) or pyautogui.pixelMatchesColor((x + single), (y - 10), (83, 83, 83), tolerance=toleranceAmount):
            # if ImageGrab.grab().getpixel( ((x + single), y) ) == (83, 83, 83) or ImageGrab.grab().getpixel( ((x + single), y - 10) ) == (83, 83, 83):
            if ImageGrab.grab().getpixel( ((x + single), y) ) == (83, 83, 83):
                print('found a tree')
                return True
    return False

def getStartingPosition():
    # print('starting position: ' + x.item() + 'x' +  y.item())
    x, y = pyautogui.locateCenterOnScreen('dinosaur.png', confidence=0.7)
    return [x.item(), y.item()]
 
def hasGameEnded():
    findRestartSymbol = pyautogui.locateOnScreen('restart-symbol.png', confidence=0.7)
    return findRestartSymbol

try:
    while True:
        start = time.time()
        # time.sleep(.1)
        
        # get starting position
        if startingPosition == None:       
            startingPosition = getStartingPosition()
            print(startingPosition)
            # add delay, so dinosaur can catch up
            time.sleep(0.5)  
            print(startingPosition)
        else:
            # check for colliion or if game has ended
            # if checkCollision(startingPosition) or hasGameEnded():
            if checkCollision(startingPosition):
                keyboard.press('space')

        # end the game manually
        if keyboard.is_pressed('q'):
            print('Killing Dino Bot!')
            break

        end = time.time()
        total_time = end - start
        print("\n"+ str(total_time))
except Exception as e:
    print(e)
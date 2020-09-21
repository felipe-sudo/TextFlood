
import random
import pyautogui
import time

def text_flood():
    store = ("This is a hacking code","This was intended to irritate and disturb others","This was intended to annoy people who we are angry with")

    data = random.choice(store)


    pyautogui.typewrite(data)
    pyautogui.press('enter')

def pause():
    print("Starting the engine...")
    time.sleep(2)
    print("Please be patient...")
    time.sleep(2)
    print("Almost ready...")
    time.sleep(2)
    print("Starting text flooding...")
    
pause()
while True:
    text_flood()
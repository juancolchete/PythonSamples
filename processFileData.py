import time
import keyboard
print("Start copy in 5 seconds")
time.sleep(5)
with open('importCode.txt') as f:
    lines = f.readlines()
    for l in lines:
        keyboard.press_and_release("home")
        time.sleep(0.1)
        keyboard.write(l)
print("copied")
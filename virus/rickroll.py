import pyautogui as py
import os

def main_rickroll():
    with py.hold('win'):
        py.press('r')
    py.write('sndvol')
    py.press('enter')
    py.press('home')

    with py.hold('alt'):
        py.press('f4')

    os.system('test.vbs')

import pyautogui as py
import subprocess as sub

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


with py.hold('win'):
    py.press('r')

py.write('sndvol', interval=0.01)
py.press('enter')
py.press('home')

with py.hold('alt'):
    py.press('f4')

with py.hold('win'):
    py.press('r')
py.write(url, interval=0.01)
py.press('enter')

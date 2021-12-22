import pyautogui as py

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

with py.hold('win'):
    py.press('r')

for i in range(100):
    py.press('volumeup')

py.write(url, interval=0.01)
py.press('enter')

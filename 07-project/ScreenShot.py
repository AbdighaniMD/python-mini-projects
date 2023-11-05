# install: "pip install PyAutoGUI"
# install: "pip install Pillow"

from unicodedata import name
import pyautogui
import time
import tkinter as tk

def screenShot():
    time.sleep(5)
    name = time.time()
    name = 'C:/Users/ghani/OneDrive/Desktop/Projects/Mini_Python_Projects/07-project/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

#screenShot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = "Take ScreenShot", command=screenShot)
button.pack(side=tk.LEFT)

clase = tk.Button(frame, text = "EXIST", command=quit)
clase.pack(side=tk.LEFT)

root.mainloop()


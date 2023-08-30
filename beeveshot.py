from tkinter import *
from tkinter.ttk import *

from gyazo import Api
import json

import tkinter as tk
import time
import ctypes
import os
import tkinter.filedialog as fd
import numpy as np
import cv2
import pyautogui
import random
import webbrowser

client = Api(access_token='VoW8tiH8dLBj7JmEDtBsANx3DmXGIR75rX9qLC6AyC8')

ctypes.windll.user32.MessageBoxW(0, "Welcome on BeeveShot, thanks for using our services. To use BeeveShot, you just have to click on a button and it will generate an URL to your screenshot saved on Gyazo.", "BeeveShot", 0)

app = Tk()
app.title("BeeveShot")
app.geometry("300x200")
app.resizable(False, False)
app.iconbitmap("src/icons/icon.ico")

def credits():
	ctypes.windll.user32.MessageBoxW(0, "made by: miyucode and Beeve / actual version: 1.0.0", "BeeveShot - Credits", 0)

def takescreenshot():
	app.withdraw()
	ctypes.windll.user32.MessageBoxW(0, "BeeveShot will take the screenshot after one second straight after you clicked OK.", "Warning", 0)
	time.sleep(1)
	screenshot = pyautogui.screenshot()
	screenshot1 = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
	rn = random.randint(1000, 9999999)
	r = cv2.imwrite(f"Screenshots/image{rn}.png", screenshot1)
	with open(f"Screenshots/image{rn}.png", 'rb') as f:
		image = client.upload_image(f)
		# print(image.permalink_url)
		# print(client.get_oembed(image.permalink_url))
		ctypes.windll.user32.MessageBoxW(0, f"Link: {image.permalink_url} - Link will be open in your browser.", "BeeveShot", 0)
		webbrowser.open(image.permalink_url)

	app.deiconify()


navbar = Menu(app)
navbarmenu = Menu(navbar, tearoff=0)

navbarmenu.add_command(label="Credits", command=credits)

navbar.add_cascade(label="Settings", menu=navbarmenu)

tk.Label(app, text="\n", fg="white", bg="#333333").pack()
Button(app, text="Take a screenshot", command=takescreenshot).pack()

app.config(bg="#333333", menu=navbar)
app.mainloop()
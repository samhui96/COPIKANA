import pykakasi
import pyperclip
import keyboard
import tkinter as tk

def convert():
    kks = pykakasi.kakasi()
    text = pyperclip.paste()
    result = kks.convert(text)
    for item in result:
        display = item['hira']
        print(display)
    return display

keyboard.add_hotkey('ctrl + v', convert)
keyboard.wait('esc')
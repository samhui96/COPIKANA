import pykakasi
import pyperclip
import base64
import os
import tkinter as tk
from tkinter import ttk

def to_hira(): # Convert kanji to hiragana
    kks = pykakasi.kakasi()
    copied_text = pyperclip.paste() # Get text from clipboard
    result = kks.convert(copied_text)
    hira_text = ""
    for item in result: # Keep hiragana only from result
        hira_text += item["hira"] + "　"
    label.config(text=hira_text)

def change_size(x):
    size = int(float(x))
    label.config(font=("MS PGothic", size))

def update_label():
    clipboard_text = str(pyperclip.paste())
    label_text = str(label.cget("text"))
    if clipboard_text != label_text:
        to_hira()
    else:
        pass
    root.after(500, update_label)  

# Creat a window
root = tk.Tk()
root.title("COPIKANA 1.0")
root.attributes("-topmost", True)
style = ttk.Style()
style.theme_use('winnative')
style.configure("Horizontal.TScale")

try:
    from COPIKANA_logo import img
    temp = open("temp.ico", "wb+") # Create a temp file to hold icon
    temp.write(base64.b64decode(img))
    temp.close()
    root.iconbitmap("temp.ico")
    os.remove('temp.ico')
except:
    pyperclip.copy("Logo missing")
    
# Creat a silder
slider = ttk.Scale(root, from_=17, to=51, length=240, command=change_size)
slider.pack(anchor='nw', fill='x')

# Create a label
label = tk.Label(font=('MS PGothic', 17), wraplength=720)
update_label()
label.pack()

root.mainloop()